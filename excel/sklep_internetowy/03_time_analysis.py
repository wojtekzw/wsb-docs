import pandas as pd
import os
import calendar

# --- Configuration ---
SALES_FILE = 'sprzedaz.csv'
OUTPUT_DIR = 'output'
SUMMARY_FILE = os.path.join(OUTPUT_DIR, '03_time_analysis.md')

# --- Load Data ---
try:
    df = pd.read_csv(SALES_FILE)
    print(f"Successfully loaded {SALES_FILE} for time analysis.")
except FileNotFoundError:
    print(f"Error: Sales file '{SALES_FILE}' not found.")
    exit()
except Exception as e:
    print(f"Error loading sales data: {e}")
    exit()

# --- Prepare Date Column and Features ---
try:
    df['Data'] = pd.to_datetime(df['Data'])
    df['Miesiąc'] = df['Data'].dt.month
    df['Dzień tygodnia'] = df['Data'].dt.isocalendar().day # Monday=1, Sunday=7
    print("Date conversion and feature extraction successful.")
except Exception as e:
    print(f"Error during date processing: {e}")
    exit() # Exit if essential date features can't be created

# --- Analyze Monthly Sales ---
monthly_sales = df.groupby('Miesiąc')['Calkowita_Wartosc'].sum().reset_index()

# Add month names (Polish)
month_names_pl = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
monthly_sales['Nazwa Miesiąca'] = monthly_sales['Miesiąc'].apply(lambda x: month_names_pl[x-1])
monthly_sales = monthly_sales[['Miesiąc', 'Nazwa Miesiąca', 'Calkowita_Wartosc']] # Reorder

# Calculate month-over-month change (dynamics)
# Use .pct_change(), handle potential division by zero or NaN for the first month
monthly_sales['Dynamika MoM (%)'] = monthly_sales['Calkowita_Wartosc'].pct_change() * 100
monthly_sales['Dynamika MoM (%)'] = monthly_sales['Dynamika MoM (%)'].fillna(0) # Fill first month NaN with 0

# Identify best/worst months
best_month = monthly_sales.loc[monthly_sales['Calkowita_Wartosc'].idxmax()]
worst_month = monthly_sales.loc[monthly_sales['Calkowita_Wartosc'].idxmin()]

monthly_summary = f"""## Analiza Sprzedaży Miesięcznej

{monthly_sales.to_markdown(index=False, floatfmt=",.2f")}

-   **Miesiąc z najwyższą sprzedażą:** {best_month['Nazwa Miesiąca']} ({best_month['Calkowita_Wartosc']:,.2f} zł)
-   **Miesiąc z najniższą sprzedażą:** {worst_month['Nazwa Miesiąca']} ({worst_month['Calkowita_Wartosc']:,.2f} zł)
"""

# --- Analyze Seasonality by Category ---
# Pivot table: Month (rows) x Category (columns), Values = Sum of Sales
category_seasonality = pd.pivot_table(
    df,
    values='Calkowita_Wartosc',
    index='Miesiąc',
    columns='Kategoria',
    aggfunc='sum',
    fill_value=0 # Fill missing month/category combinations with 0
).reset_index()

# Add month names
category_seasonality['Miesiąc'] = category_seasonality['Miesiąc'].apply(lambda x: month_names_pl[x-1])

seasonality_summary = f"""## Analiza Sezonowości według Kategorii (Suma sprzedaży miesięcznie)

{category_seasonality.to_markdown(index=False, floatfmt=",.2f")}

*(Formatowanie warunkowe w Excelu pomogłoby tu wizualnie wyróżnić okresy szczytowe dla każdej kategorii)*
"""

# --- Analyze Sales by Day of the Week ---
dow_sales = df.groupby('Dzień tygodnia')['Calkowita_Wartosc'].sum().reset_index()

# Add day names (Polish)
day_names_pl = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
dow_sales['Nazwa Dnia'] = dow_sales['Dzień tygodnia'].apply(lambda x: day_names_pl[x-1])
dow_sales = dow_sales.sort_values(by='Dzień tygodnia')
dow_sales = dow_sales[['Dzień tygodnia', 'Nazwa Dnia', 'Calkowita_Wartosc']] # Reorder

best_dow = dow_sales.loc[dow_sales['Calkowita_Wartosc'].idxmax()]

dow_summary = f"""## Analiza Sprzedaży według Dni Tygodnia

{dow_sales.to_markdown(index=False, floatfmt=",.2f")}

-   **Dzień tygodnia z najwyższą sprzedażą:** {best_dow['Nazwa Dnia']} ({best_dow['Calkowita_Wartosc']:,.2f} zł)
"""

# --- Combine Summaries ---
final_summary = f"""# Część 3: Analiza Czasowa i Sezonowość

{monthly_summary}

{seasonality_summary}

{dow_summary}
"""

# --- Save Summary ---
try:
    with open(SUMMARY_FILE, 'w', encoding='utf-8') as f:
        f.write(final_summary)
    print(f"Successfully saved time analysis summary to {SUMMARY_FILE}")
except Exception as e:
    print(f"Error saving summary file: {e}") 