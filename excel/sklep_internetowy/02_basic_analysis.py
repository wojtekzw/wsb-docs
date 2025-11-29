import pandas as pd
import os

# --- Configuration ---
SALES_FILE = 'sprzedaz.csv'
OUTPUT_DIR = 'output'
SUMMARY_FILE = os.path.join(OUTPUT_DIR, '02_basic_analysis.md')

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Load Data ---
try:
    df = pd.read_csv(SALES_FILE)
    print(f"Successfully loaded {SALES_FILE} for basic analysis.")
except FileNotFoundError:
    print(f"Error: Sales file '{SALES_FILE}' not found.")
    exit()
except Exception as e:
    print(f"Error loading sales data: {e}")
    exit()

# --- Calculate KPIs ---
total_sales = df['Calkowita_Wartosc'].sum()
num_transactions = len(df)
# Alternative for unique transaction IDs if needed: df['ID_Transakcji'].nunique()
avg_order_value = df['Calkowita_Wartosc'].mean()
max_order_value = df['Calkowita_Wartosc'].max()
min_order_value = df['Calkowita_Wartosc'].min()

kpi_summary = f"""## Kluczowe Wskaźniki Sprzedaży (KPIs)

-   **Sumaryczna wartość sprzedaży:** {total_sales:,.2f} zł
-   **Liczba transakcji:** {num_transactions:,}
-   **Średnia wartość zamówienia:** {avg_order_value:,.2f} zł
-   **Najwyższa wartość zamówienia:** {max_order_value:,.2f} zł
-   **Najniższa wartość zamówienia:** {min_order_value:,.2f} zł
"""

# --- Analyze Sales by Category ---
category_analysis = df.groupby('Kategoria').agg(
    Wartosc_Sprzedazy = pd.NamedAgg(column='Calkowita_Wartosc', aggfunc='sum'),
    Liczba_Sztuk = pd.NamedAgg(column='Liczba_Sztuk', aggfunc='sum'),
    Liczba_Transakcji = pd.NamedAgg(column='ID_Transakcji', aggfunc='count') # Count transactions per category
).reset_index()

# Calculate average order value per category
category_analysis['Srednia_Wartosc_Zamowienia'] = category_analysis['Wartosc_Sprzedazy'] / category_analysis['Liczba_Transakcji']

# Calculate percentage share
category_analysis['Udzial_Procentowy'] = (category_analysis['Wartosc_Sprzedazy'] / total_sales) * 100

# Sort by sales value
category_analysis = category_analysis.sort_values(by='Wartosc_Sprzedazy', ascending=False)

category_summary = f"""## Analiza Sprzedaży według Kategorii Produktów

{category_analysis.to_markdown(index=False, floatfmt=",.2f")}
"""

# --- Analyze Sales by Region ---
region_analysis = df.groupby('Region').agg(
    Wartosc_Sprzedazy = pd.NamedAgg(column='Calkowita_Wartosc', aggfunc='sum'),
    Liczba_Transakcji = pd.NamedAgg(column='ID_Transakcji', aggfunc='count')
).reset_index()

# Sort by sales value
region_analysis = region_analysis.sort_values(by='Wartosc_Sprzedazy', ascending=False)

region_summary = f"""## Analiza Sprzedaży według Regionów

{region_analysis.to_markdown(index=False, floatfmt=",.2f")}
"""

# --- Combine Summaries ---
final_summary = f"""# Część 2: Analiza Podstawowa

{kpi_summary}

{category_summary}

{region_summary}
"""

# --- Save Summary ---
try:
    with open(SUMMARY_FILE, 'w', encoding='utf-8') as f:
        f.write(final_summary)
    print(f"Successfully saved basic analysis summary to {SUMMARY_FILE}")
except Exception as e:
    print(f"Error saving summary file: {e}") 