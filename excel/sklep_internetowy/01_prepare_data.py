import pandas as pd
import os

# --- Configuration ---
SALES_FILE = 'sprzedaz.csv'
OUTPUT_DIR = 'output'
SUMMARY_FILE = os.path.join(OUTPUT_DIR, '01_data_preparation_summary.md')

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Load Data ---
try:
    df = pd.read_csv(SALES_FILE)
    print(f"Successfully loaded {SALES_FILE}")
except FileNotFoundError:
    print(f"Error: Sales file '{SALES_FILE}' not found.")
    exit()
except Exception as e:
    print(f"Error loading sales data: {e}")
    exit()

# --- Data Preparation ---
# Convert 'Data' to datetime
try:
    df['Data'] = pd.to_datetime(df['Data'])
except Exception as e:
    print(f"Error converting 'Data' column to datetime: {e}")
    # Continue if possible, but date features might fail
    
# Add time-based columns
if 'Data' in df.columns and pd.api.types.is_datetime64_any_dtype(df['Data']):
    df['Miesiąc'] = df['Data'].dt.month
    df['Kwartał'] = df['Data'].dt.quarter
    # Monday=0, Sunday=6. Add 1 to match Excel's Monday=1 convention if needed.
    # Let's use ISO standard (Monday=1, Sunday=7) like Excel's option 2 (DZIEŃ.TYG([@Data];2))
    df['Dzień tygodnia'] = df['Data'].dt.isocalendar().day 
    print("Added time-based columns: Miesiąc, Kwartał, Dzień tygodnia (ISO).")
else:
     print("Skipping time-based columns due to issues with 'Data' column.")
     
# --- Generate Summary ---
summary_content = f"""# Część 1: Podsumowanie Przygotowania Danych

## Źródło danych
- Plik: `{SALES_FILE}`

## Wykonane kroki
1.  Załadowano dane sprzedażowe.
2.  Przekonwertowano kolumnę 'Data' na format daty i czasu.
3.  Dodano kolumny pomocnicze:
    -   `Miesiąc`: Numer miesiąca (1-12).
    -   `Kwartał`: Numer kwartału (1-4).
    -   `Dzień tygodnia`: Numer dnia tygodnia (1=Poniedziałek, 7=Niedziela, zgodnie z ISO 8601 / Excel DZIEŃ.TYG z typem 2).

## Podstawowe informacje o danych po przygotowaniu
-   Liczba transakcji (wierszy): {df.shape[0]}
-   Liczba kolumn: {df.shape[1]}
-   Zakres dat: {df['Data'].min().strftime('%Y-%m-%d') if 'Data' in df.columns else 'N/A'} do {df['Data'].max().strftime('%Y-%m-%d') if 'Data' in df.columns else 'N/A'}

## Pierwsze 5 wierszy przetworzonych danych:
```
{df.head().to_markdown(index=False)}
```
"""

# --- Save Summary ---
try:
    with open(SUMMARY_FILE, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    print(f"Successfully saved data preparation summary to {SUMMARY_FILE}")
except Exception as e:
    print(f"Error saving summary file: {e}")

# Optional: Save the processed dataframe if needed for subsequent scripts
# PROCESSED_FILE = os.path.join(OUTPUT_DIR, 'sprzedaz_processed.csv')
# df.to_csv(PROCESSED_FILE, index=False, encoding='utf-8')
# print(f"Processed data saved to {PROCESSED_FILE}") 