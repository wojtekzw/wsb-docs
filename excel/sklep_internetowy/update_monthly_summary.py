import csv
from collections import defaultdict
import calendar

# --- Configuration ---
SALES_FILE = 'sprzedaz.csv'
MONTHLY_SUMMARY_FILE = 'sprzedaz_miesieczna.csv'
CATEGORIES = ['Elektronika', 'Odzież', 'Artykuły sportowe', 'Książki', 'Dom i ogród', 'Zabawki'] # Needed for header order

# --- Calculate Monthly Totals ---
monthly_totals = defaultdict(float) # Store only total per month
# Format: monthly_totals[month_number] = total_value

try:
    with open(SALES_FILE, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                date_parts = row['Data'].split('-')
                month = int(date_parts[1])
                value = float(row['Calkowita_Wartosc'])
                monthly_totals[month] += value
            except (ValueError, IndexError, KeyError) as e:
                print(f"Skipping row due to error ({e}): {row}")
except FileNotFoundError:
    print(f"Error: Sales file '{SALES_FILE}' not found.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the sales file: {e}")
    exit()

# --- Prepare Data for CSV ---
output_data = []
header = ['Miesiąc'] + CATEGORIES + ['Razem']
output_data.append(header)

grand_total = 0

# Using Polish names for consistency with original file format
month_names_pl = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]

for i in range(1, 13):
    month_name = month_names_pl[i-1]
    month_total_value = round(monthly_totals[i], 2)
    # Create row with month name, zeros for categories, and the calculated total
    row_data = [month_name] + [0.00] * len(CATEGORIES) + [month_total_value]
    output_data.append(row_data)
    grand_total += month_total_value

# Add totals row
# Zeros for categories, grand total for the 'Razem' column
totals_row = ['Razem'] + [0.00] * len(CATEGORIES) + [round(grand_total, 2)]
output_data.append(totals_row)

# --- Write Updated Monthly Summary ---
try:
    with open(MONTHLY_SUMMARY_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output_data)
    print(f"Successfully updated '{MONTHLY_SUMMARY_FILE}' with monthly totals only.")
except IOError:
    print(f"Error: Could not write to file '{MONTHLY_SUMMARY_FILE}'. Check permissions.")
except Exception as e:
    print(f"An unexpected error occurred while writing the monthly summary file: {e}") 