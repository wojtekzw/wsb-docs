import pandas as pd
import os

# --- Configuration ---
SALES_FILE = 'sprzedaz.csv' # Needed for Revenue Mix calculation
PROFITABILITY_SCRIPT = '06_profitability_analysis.py' # To get category profitability
OUTPUT_DIR = 'output'
SUMMARY_FILE = os.path.join(OUTPUT_DIR, '07_optimization_summary.md')

# --- Load Data ---
print("Loading data for optimization summary...")
try:
    # Rerun parts of profitability script logic to get necessary dataframes
    # Load base sales data
    df_sales = pd.read_csv(SALES_FILE)
    df_sales['Data'] = pd.to_datetime(df_sales['Data'])
    df_sales['Miesiąc'] = df_sales['Data'].dt.month
    
    # Load other necessary files
    df_catalog = pd.read_csv('katalog_produktow.csv')
    df_logistics = pd.read_csv('kategorie_logistyczne.csv')
    df_common_costs = pd.read_csv('koszty_wspolne.csv')
    df_alloc_keys = pd.read_csv('klucze_alokacji.csv')

    # --- Recalculate Category Totals (simplified from script 06) ---
    # Merge
    df_catalog_subset = df_catalog[['Produkt', 'Kategoria_Logistyczna', 'Koszt_Zakupu']]
    df_sales = pd.merge(df_sales, df_catalog_subset, on='Produkt', how='left')
    df_logistics_subset = df_logistics[['Kategoria_Logistyczna', 'Koszt_Bazowy']]
    df_sales = pd.merge(df_sales, df_logistics_subset, on='Kategoria_Logistyczna', how='left')
    df_sales.dropna(subset=['Koszt_Zakupu', 'Koszt_Bazowy'], inplace=True)

    # Calculate metrics
    df_sales['Przychód'] = df_sales['Cena_Jednostkowa'] * df_sales['Liczba_Sztuk']
    df_sales['Koszt_Zakupu_Produktow'] = df_sales['Koszt_Zakupu'] * df_sales['Liczba_Sztuk']
    df_sales['Koszt_Logistyczny_Produktow'] = df_sales['Koszt_Bazowy'] * df_sales['Liczba_Sztuk']
    df_sales['Marża_Brutto_Transakcji'] = df_sales['Przychód'] - df_sales['Koszt_Zakupu_Produktow'] - df_sales['Koszt_Logistyczny_Produktow']

    # Aggregate by Category for the whole year
    category_totals = df_sales.groupby('Kategoria').agg(
        Całkowity_Przychód = pd.NamedAgg(column='Przychód', aggfunc='sum'),
        Całkowita_Marża_Brutto = pd.NamedAgg(column='Marża_Brutto_Transakcji', aggfunc='sum')
    ).reset_index()

    # --- Allocate Common Costs Annually (Simplified approach for overall picture) ---
    total_common_costs = df_common_costs['Wartość'].sum()
    df_alloc_keys.set_index('Kategoria', inplace=True)
    alloc_keys_dict = df_alloc_keys.to_dict(orient='index')

    # Rough annual allocation - assumes keys apply to total cost. 
    # More precise would be allocating monthly then summing.
    # Using average keys if they varied monthly, but they don't seem to.
    def calculate_annual_allocated(row):
        category = row['Kategoria']
        keys = alloc_keys_dict.get(category, {})
        # Average key across cost types for simplicity (crude but gives an idea)
        avg_key = sum(keys.values()) / len(keys) if keys else 0
        # A better approach might be using revenue share as allocation key if others are complex
        # For this example, let's use revenue share as a proxy if keys are problematic
        return total_common_costs * (row['Całkowity_Przychód'] / category_totals['Całkowity_Przychód'].sum())
        
    # Using revenue share for simplicity in this script
    total_revenue = category_totals['Całkowity_Przychód'].sum()
    category_totals['Przydzielony_Koszt_Wspólny_Roczny'] = (category_totals['Całkowity_Przychód'] / total_revenue) * total_common_costs
    
    # Calculate Annual Net Profit and Rentowność
    category_totals['Zysk_Netto_Roczny'] = category_totals['Całkowita_Marża_Brutto'] - category_totals['Przydzielony_Koszt_Wspólny_Roczny']
    category_totals['Rentowność_Sprzedaży_Roczna (%)'] = (category_totals['Zysk_Netto_Roczny'] / category_totals['Całkowity_Przychód'].replace(0, pd.NA)) * 100
    category_totals['Rentowność_Sprzedaży_Roczna (%)'] = category_totals['Rentowność_Sprzedaży_Roczna (%)'].fillna(0)

    # Calculate Sales Mix
    category_totals['Udział_w_Przychodach (%)'] = (category_totals['Całkowity_Przychód'] / total_revenue) * 100

    # Sort for presentation
    category_summary_final = category_totals.sort_values(by='Rentowność_Sprzedaży_Roczna (%)', ascending=False)
    category_summary_table = category_summary_final[['Kategoria', 'Udział_w_Przychodach (%)', 'Rentowność_Sprzedaży_Roczna (%)', 'Całkowity_Przychód', 'Zysk_Netto_Roczny']].to_markdown(index=False, floatfmt=",.2f")

    print("Profitability data calculated.")

except Exception as e:
    print(f"Error processing data for optimization summary: {e}")
    # Create a placeholder summary if data processing fails
    category_summary_table = "Błąd podczas przetwarzania danych rentowności."
    category_summary_final = pd.DataFrame() # Empty dataframe

# --- Formulate Recommendations --- 
recommendations = []
recommendations.append("## Rekomendacje Biznesowe")

if not category_summary_final.empty:
    highly_profitable = category_summary_final[category_summary_final['Rentowność_Sprzedaży_Roczna (%)'] > category_summary_final['Rentowność_Sprzedaży_Roczna (%)'].median()]
    less_profitable = category_summary_final[category_summary_final['Rentowność_Sprzedaży_Roczna (%)'] <= category_summary_final['Rentowność_Sprzedaży_Roczna (%)'].median()]
    negative_profit = category_summary_final[category_summary_final['Zysk_Netto_Roczny'] < 0]

    recommendations.append("\n### Optymalizacja Struktury Sprzedaży:")
    recommendations.append("-   **Promuj Kategorie Wysoko Rentowne:** Skupić działania marketingowe i promocyjne na kategoriach z najwyższą rentownością, takich jak:")
    for cat in highly_profitable['Kategoria'].head(3).tolist():
        recommendations.append(f"    -   {cat}")
    recommendations.append("-   **Analiza Kategorii Nisko Rentownych:** Dokładnie przeanalizować kategorie o niskiej lub ujemnej rentowności:")
    for cat in less_profitable['Kategoria'].tolist():
        recommendations.append(f"    -   {cat}")
    recommendations.append("    Rozważyć optymalizację kosztów (zakupu, logistyki), renegocjację cen lub nawet wycofanie najmniej rentownych produktów w tych kategoriach.")

    if not negative_profit.empty:
        recommendations.append("\n### Działania Natychmiastowe (Kategorie Stratne):")
        recommendations.append("-   Kategorie generujące stratę netto wymagają pilnej interwencji:")
        for cat in negative_profit['Kategoria'].tolist():
            recommendations.append(f"    -   {cat}")
        recommendations.append("    Należy zbadać przyczyny (wysokie koszty, niska marża, błędy w danych?) i podjąć decyzje naprawcze.")

    recommendations.append("\n### Optymalizacja Cen i Marż:")
    recommendations.append("-   Rozważyć ostrożne podniesienie cen dla produktów o niskiej elastyczności cenowej w kategoriach wysoko rentownych.")
    recommendations.append("-   Przeanalizować możliwość renegocjacji cen zakupu z dostawcami dla produktów o niskiej marży brutto, szczególnie w kategoriach o dużym udziale w sprzedaży.")

    recommendations.append("\n### Optymalizacja Kosztów:")
    recommendations.append("-   **Logistyka:** Zbadać, czy koszty logistyczne (`Koszt_Bazowy`) dla poszczególnych kategorii są adekwatne i czy istnieją możliwości ich optymalizacji (np. zmiana dostawcy usług logistycznych, optymalizacja pakowania).")
    recommendations.append("-   **Koszty Wspólne:** Przeanalizować strukturę kosztów wspólnych i zasadność ich alokacji. Czy klucze alokacji (`klucze_alokacji.csv`) odzwierciedlają rzeczywiste zużycie zasobów przez kategorie?")

else:
    recommendations.append("\nNie udało się wygenerować rekomendacji z powodu błędu przetwarzania danych.")

# Join recommendations into a single string *before* the f-string
recommendations_text = '\n'.join(recommendations)

# --- Generate Summary File --- 
summary_content = f"""# Część 7: Optymalizacja Struktury Sprzedaży i Rekomendacje

## Analiza Struktury Sprzedaży i Rentowności Rocznej

Poniższa tabela przedstawia udział poszczególnych kategorii w całkowitych przychodach oraz ich roczną rentowność sprzedaży (na podstawie uproszczonej alokacji kosztów wspólnych proporcjonalnie do przychodów).

{category_summary_table}

{recommendations_text}

## Model Optymalizacyjny (Koncepcja)

Do dalszej optymalizacji można stworzyć model (np. w Excelu z użyciem Solver'a), który pozwoliłby symulować:
-   Zmiany w procentowym udziale sprzedaży poszczególnych kategorii.
-   Zmiany w marżach produktów.
-   Zmiany w kosztach (logistycznych, wspólnych).
Celem byłoby znalezienie kombinacji maksymalizującej całkowity zysk netto przy zadanych ograniczeniach.
"""

# --- Save Summary ---
try:
    with open(SUMMARY_FILE, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    print(f"Successfully saved optimization summary and recommendations to {SUMMARY_FILE}")
except Exception as e:
    print(f"Error saving summary file: {e}") 