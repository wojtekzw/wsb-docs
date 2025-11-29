import pandas as pd
import os
import calendar

# --- Configuration ---
SALES_FILE = 'sprzedaz.csv'
PRODUCT_CATALOG_FILE = 'katalog_produktow.csv'
LOGISTICS_CATEGORIES_FILE = 'kategorie_logistyczne.csv'
COMMON_COSTS_FILE = 'koszty_wspolne.csv'
ALLOCATION_KEYS_FILE = 'klucze_alokacji.csv'
OUTPUT_DIR = 'output'
SUMMARY_FILE = os.path.join(OUTPUT_DIR, '06_profitability_analysis.md')

# --- Load Data ---
print("Loading data...")
try:
    df_sales = pd.read_csv(SALES_FILE)
    df_catalog = pd.read_csv(PRODUCT_CATALOG_FILE)
    df_logistics = pd.read_csv(LOGISTICS_CATEGORIES_FILE)
    df_common_costs = pd.read_csv(COMMON_COSTS_FILE)
    df_alloc_keys = pd.read_csv(ALLOCATION_KEYS_FILE)
except FileNotFoundError as e:
    print(f"Error loading file: {e}. Please ensure all required CSV files are present.")
    exit()
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

print("Data loaded successfully.")

# --- Data Preparation and Merging ---
print("Preparing and merging data...")
# Convert sales date
df_sales['Data'] = pd.to_datetime(df_sales['Data'])
df_sales['Miesiąc'] = df_sales['Data'].dt.month

# Select relevant columns and merge catalog data with sales
df_catalog_subset = df_catalog[['Produkt', 'Kategoria_Logistyczna', 'Koszt_Zakupu']]
df_sales = pd.merge(df_sales, df_catalog_subset, on='Produkt', how='left')

# Select relevant columns and merge logistics base cost
df_logistics_subset = df_logistics[['Kategoria_Logistyczna', 'Koszt_Bazowy']]
df_sales = pd.merge(df_sales, df_logistics_subset, on='Kategoria_Logistyczna', how='left')

# Handle potential missing data after merges
missing_catalog = df_sales['Koszt_Zakupu'].isnull().sum()
missing_logistics = df_sales['Koszt_Bazowy'].isnull().sum()
if missing_catalog > 0 or missing_logistics > 0:
    print(f"Warning: Missing data after merging. Catalog: {missing_catalog}, Logistics: {missing_logistics}. Rows with missing data will be excluded from calculations.")
    df_sales.dropna(subset=['Koszt_Zakupu', 'Koszt_Bazowy'], inplace=True)

print("Data merged.")

# --- Calculate Profitability Metrics per Transaction ---
print("Calculating per-transaction metrics...")
df_sales['Przychód'] = df_sales['Cena_Jednostkowa'] * df_sales['Liczba_Sztuk'] # Revenue based on actual unit price * quantity
df_sales['Koszt_Zakupu_Produktow'] = df_sales['Koszt_Zakupu'] * df_sales['Liczba_Sztuk']
df_sales['Koszt_Logistyczny_Produktow'] = df_sales['Koszt_Bazowy'] * df_sales['Liczba_Sztuk'] # Base cost per unit sold
# Note: This is different from Koszt_Dostawy which is per order. Instrukcja is a bit ambiguous here.
# Let's calculate Gross Margin based on Revenue - COGS - Product Logistics Cost
df_sales['Marża_Brutto_Transakcji'] = df_sales['Przychód'] - df_sales['Koszt_Zakupu_Produktow'] - df_sales['Koszt_Logistyczny_Produktow']

# --- Aggregate Monthly Gross Margin by Category ---
print("Aggregating monthly gross margin by category...")
monthly_profitability = df_sales.groupby(['Miesiąc', 'Kategoria']).agg(
    Całkowity_Przychód = pd.NamedAgg(column='Przychód', aggfunc='sum'),
    Całkowita_Marża_Brutto = pd.NamedAgg(column='Marża_Brutto_Transakcji', aggfunc='sum')
).reset_index()

# --- Allocate Common Costs (Revised Logic) ---
print("Allocating common costs (Revised Logic)...")

# Prepare common costs: Pivot to have cost types as columns
df_common_costs_pivot = df_common_costs.pivot_table(
    index='Miesiąc', 
    columns='Typ_Kosztu', 
    values='Wartość'
).reset_index().fillna(0)

# Prepare allocation keys: Set Kategoria as index for easy lookup
df_alloc_keys.set_index('Kategoria', inplace=True)
# Create a dictionary for faster lookup: {Kategoria: {Typ_Kosztu_Klucz: KeyValue}}
alloc_keys_dict = df_alloc_keys.to_dict(orient='index')

# Define mapping from common cost column name to allocation key column name
# Adjust key names based on the actual header found in klucze_alokacji.csv
cost_type_to_key_col = {
    'Koszty osobowe': 'Klucz_Koszty_Osobowe', 
    'Koszty informatyczne': 'Klucz_Koszty_Informatyczne', 
    'Koszty działalności': 'Klucz_Koszty_Dzialalnosci', 
    'Koszty marketingowe': 'Klucz_Koszty_Marketingowe', 
    'Koszty administracyjne': 'Klucz_Koszty_Administracyjne' # Check exact name from file header if needed
}

# Calculate allocated costs per month and category
allocated_costs_list = []
for month in df_common_costs_pivot['Miesiąc'].unique():
    monthly_costs = df_common_costs_pivot[df_common_costs_pivot['Miesiąc'] == month].iloc[0]
    for category, keys in alloc_keys_dict.items():
        category_allocated_cost = 0
        for cost_type, key_col_name in cost_type_to_key_col.items():
            if cost_type in monthly_costs and key_col_name in keys:
                category_allocated_cost += monthly_costs[cost_type] * keys[key_col_name]
            else:
                # Handle cases where cost type or key might be missing for robustness
                # print(f"Warning: Missing cost type '{cost_type}' or key '{key_col_name}' for month {month}, category {category}")
                pass 
        allocated_costs_list.append({
            'Miesiąc': month,
            'Kategoria': category,
            'Przydzielony_Koszt_Wspólny': category_allocated_cost
        })

df_allocated_costs = pd.DataFrame(allocated_costs_list)

# Merge allocated costs into the main profitability table
monthly_profitability = pd.merge(
    monthly_profitability, 
    df_allocated_costs, 
    on=['Miesiąc', 'Kategoria'], 
    how='left'
)
monthly_profitability['Przydzielony_Koszt_Wspólny'] = monthly_profitability['Przydzielony_Koszt_Wspólny'].fillna(0)

# --- Calculate Net Profit and Rentowność ---
print("Calculating net profit and rentowność...")
monthly_profitability['Zysk_Netto'] = monthly_profitability['Całkowita_Marża_Brutto'] - monthly_profitability['Przydzielony_Koszt_Wspólny']
# Ensure Przychód column exists and handle division by zero
if 'Całkowity_Przychód' in monthly_profitability.columns:
    # Replace 0 with NA temporarily to avoid division by zero error, then fill NA result with 0
    monthly_profitability['Rentowność_Sprzedaży (%)'] = (monthly_profitability['Zysk_Netto'] / monthly_profitability['Całkowity_Przychód'].replace(0, pd.NA)) * 100
    monthly_profitability['Rentowność_Sprzedaży (%)'] = monthly_profitability['Rentowność_Sprzedaży (%)'].fillna(0)
else:
    print("Warning: 'Całkowity_Przychód' column not found for Rentowność calculation.")
    monthly_profitability['Rentowność_Sprzedaży (%)'] = 0.0

# Add Polish month names
month_names_pl = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
monthly_profitability['Nazwa Miesiąca'] = monthly_profitability['Miesiąc'].apply(lambda x: month_names_pl[x-1])

# Select and reorder columns for final table
monthly_profitability_final = monthly_profitability[[
    'Miesiąc', 'Nazwa Miesiąca', 'Kategoria', 
    'Całkowity_Przychód', 'Całkowita_Marża_Brutto', 'Przydzielony_Koszt_Wspólny', 
    'Zysk_Netto', 'Rentowność_Sprzedaży (%)'
]]

# --- Identify Top/Bottom Products (Based on Gross Margin) ---
print("Identifying top/bottom products by gross margin...")
product_profitability = df_sales.groupby('Produkt').agg(
    Całkowita_Marża_Brutto = pd.NamedAgg(column='Marża_Brutto_Transakcji', aggfunc='sum'),
    Liczba_Sprzedanych_Sztuk = pd.NamedAgg(column='Liczba_Sztuk', aggfunc='sum')
).reset_index()

most_profitable_products = product_profitability.sort_values(by='Całkowita_Marża_Brutto', ascending=False).head(5)
least_profitable_products = product_profitability.sort_values(by='Całkowita_Marża_Brutto', ascending=True).head(5)

# --- Generate Summary ---
summary_content = f"""# Część 6: Analiza Rentowności

## Metodologia
1.  Połączono dane sprzedażowe z katalogiem produktów (koszt zakupu) i kategoriami logistycznymi (koszt bazowy logistyki).
2.  Obliczono przychód, koszt zakupu sprzedanych towarów (COGS) i koszt logistyczny produktów dla każdej transakcji.
3.  Obliczono marżę brutto na poziomie transakcji (Przychód - COGS - Koszt Logistyczny Produktów).
4.  Zsumowano miesięczną marżę brutto i przychód dla każdej kategorii produktów.
5.  Załadowano miesięczne koszty wspólne i klucze alokacji.
6.  Przydzielono miesięczne koszty wspólne do kategorii produktów zgodnie z kluczami alokacji.
7.  Obliczono zysk netto (Marża Brutto - Przydzielone Koszty Wspólne) i rentowność sprzedaży (Zysk Netto / Przychód) dla każdej kategorii miesięcznie.

## Rentowność Miesięczna według Kategorii

{monthly_profitability_final.to_markdown(index=False, floatfmt=",.2f")}

## Analiza Rentowności Produktów (Top 5 wg Marży Brutto)

{most_profitable_products.to_markdown(index=False, floatfmt=",.2f")}

## Analiza Rentowności Produktów (Najniższa Marża Brutto - Bottom 5)

{least_profitable_products.to_markdown(index=False, floatfmt=",.2f")}

*Uwaga: Analiza rentowności produktu opiera się na Marży Brutto (przed alokacją kosztów wspólnych), ponieważ alokacja kosztów wspólnych na pojedynczy produkt jest często złożona i wykracza poza typowe dane wejściowe.*
"""

# --- Save Summary ---
try:
    with open(SUMMARY_FILE, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    print(f"Successfully saved profitability analysis summary to {SUMMARY_FILE}")
except Exception as e:
    print(f"Error saving summary file: {e}") 