import pandas as pd
import matplotlib.pyplot as plt
import os
import calendar

# --- Configuration ---
SALES_FILE = 'sprzedaz.csv'
OUTPUT_DIR = 'output'
SUMMARY_FILE = os.path.join(OUTPUT_DIR, '04_visualization_summary.md')
MONTHLY_SALES_PLOT = os.path.join(OUTPUT_DIR, '04_monthly_sales.png')
CATEGORY_SHARE_PLOT = os.path.join(OUTPUT_DIR, '04_category_share.png')
TOP_PRODUCTS_PLOT = os.path.join(OUTPUT_DIR, '04_top_products.png')

# --- Load Data ---
try:
    df = pd.read_csv(SALES_FILE)
    df['Data'] = pd.to_datetime(df['Data']) # Ensure date is datetime
    df['Miesiąc'] = df['Data'].dt.month
    print(f"Successfully loaded {SALES_FILE} for visualization summary.")
except FileNotFoundError:
    print(f"Error: Sales file '{SALES_FILE}' not found.")
    exit()
except Exception as e:
    print(f"Error loading or processing sales data: {e}")
    exit()

# Polish month names
month_names_pl = ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze", "Lip", "Sie", "Wrz", "Paź", "Lis", "Gru"]

# --- Prepare Data for Plots ---
# 1. Monthly Sales
monthly_sales = df.groupby('Miesiąc')['Calkowita_Wartosc'].sum()
monthly_sales = monthly_sales.reindex(range(1, 13), fill_value=0) # Ensure all months are present
monthly_sales.index = month_names_pl # Use Polish abbreviations

# 2. Category Share
category_share = df.groupby('Kategoria')['Calkowita_Wartosc'].sum()
category_share = category_share.sort_values(ascending=False)

# 3. Top 5 Products by Sales Value
top_products = df.groupby('Produkt')['Calkowita_Wartosc'].sum().nlargest(5)

# --- Generate Plots ---
plt.style.use('seaborn-v0_8-whitegrid') # Use a clean style

# 1. Monthly Sales Plot
try:
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    monthly_sales.plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_title('Miesięczna Wartość Sprzedaży', fontsize=14)
    ax1.set_xlabel('Miesiąc', fontsize=10)
    ax1.set_ylabel('Wartość Sprzedaży (zł)', fontsize=10)
    ax1.tick_params(axis='x', rotation=45)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',').replace(',', ' ')))
    plt.tight_layout()
    plt.savefig(MONTHLY_SALES_PLOT)
    plt.close(fig1)
    print(f"Generated plot: {MONTHLY_SALES_PLOT}")
except Exception as e:
    print(f"Error generating monthly sales plot: {e}")

# 2. Category Share Plot
try:
    fig2, ax2 = plt.subplots(figsize=(7, 7))
    ax2.pie(category_share, labels=category_share.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax2.set_title('Udział Kategorii w Całkowitej Sprzedaży', fontsize=14)
    plt.tight_layout()
    plt.savefig(CATEGORY_SHARE_PLOT)
    plt.close(fig2)
    print(f"Generated plot: {CATEGORY_SHARE_PLOT}")
except Exception as e:
    print(f"Error generating category share plot: {e}")

# 3. Top 5 Products Plot
try:
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    top_products.sort_values().plot(kind='barh', ax=ax3, color='lightcoral') # Horizontal bar chart
    ax3.set_title('Top 5 Produktów (wg Wartości Sprzedaży)', fontsize=14)
    ax3.set_xlabel('Całkowita Wartość Sprzedaży (zł)', fontsize=10)
    ax3.set_ylabel('Produkt', fontsize=10)
    ax3.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',').replace(',', ' ')))
    plt.tight_layout()
    plt.savefig(TOP_PRODUCTS_PLOT)
    plt.close(fig3)
    print(f"Generated plot: {TOP_PRODUCTS_PLOT}")
except Exception as e:
    print(f"Error generating top products plot: {e}")

# --- Calculate KPIs for Dashboard ---
total_sales = df['Calkowita_Wartosc'].sum()
num_transactions = len(df)
avg_order_value = df['Calkowita_Wartosc'].mean()

# Simulate YoY dynamics (comparing H2 vs H1)
h1_sales = df[df['Miesiąc'] <= 6]['Calkowita_Wartosc'].sum()
h2_sales = df[df['Miesiąc'] > 6]['Calkowita_Wartosc'].sum()
yoy_dynamics = ((h2_sales - h1_sales) / h1_sales) * 100 if h1_sales else 0

kpi_values = f"""## Kluczowe Wskaźniki (KPIs) dla Dashboardu

-   **Całkowita sprzedaż:** {total_sales:,.2f} zł
-   **Liczba transakcji:** {num_transactions:,}
-   **Średnia wartość zamówienia:** {avg_order_value:,.2f} zł
-   **Dynamika H2 vs H1 (symulacja YoY):** {yoy_dynamics:.2f} %
"""

# --- Generate Summary ---
summary_content = f"""# Część 4: Podsumowanie Wizualizacji i Dashboardu

Wygenerowano dane i wizualizacje kluczowych aspektów sprzedaży. Te elementy mogą posłużyć do budowy interaktywnego dashboardu w Excelu.

## Wygenerowane Wykresy

1.  **Sprzedaż Miesięczna:** Pokazuje rozkład sprzedaży w poszczególnych miesiącach.
    ![Wykres sprzedaży miesięcznej]({os.path.basename(MONTHLY_SALES_PLOT)})

2.  **Udział Kategorii:** Przedstawia procentowy udział każdej kategorii w całkowitej wartości sprzedaży.
    ![Wykres udziału kategorii]({os.path.basename(CATEGORY_SHARE_PLOT)})

3.  **Top 5 Produktów:** Wskazuje produkty generujące najwyższą wartość sprzedaży.
    ![Wykres top 5 produktów]({os.path.basename(TOP_PRODUCTS_PLOT)})

*(Pliki PNG zostały zapisane w katalogu `{OUTPUT_DIR}`)*

{kpi_values}

## Elementy Interaktywne (Do zaimplementowania w Excelu)

-   **Fragmentatory (Slicers):** Umożliwiające filtrowanie danych na wykresach i wskaźnikach KPI według:
    -   Kategorii produktów
    -   Regionów
    -   Kwartałów/Miesięcy
-   **Dodatkowe Wykresy:** Można dodać wykres sezonowości (mapa cieplna) lub inne analizy wg potrzeb.
"""

# --- Save Summary ---
try:
    with open(SUMMARY_FILE, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    print(f"Successfully saved visualization summary to {SUMMARY_FILE}")
except Exception as e:
    print(f"Error saving summary file: {e}") 