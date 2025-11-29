import csv
import random
from datetime import date, timedelta

# --- Configuration ---
OUTPUT_FILE = 'sprzedaz_nowa.csv'
PRODUCT_CATALOG_FILE = 'katalog_produktow.csv'
LOGISTICS_CATEGORIES_FILE = 'kategorie_logistyczne.csv'
START_DATE = date(2024, 1, 1)
END_DATE = date(2024, 12, 31)
NUMBER_OF_TRANSACTIONS = 7500
REGIONS = ['Centralny', 'Południowy', 'Wschodni', 'Zachodni', 'Północny']
# BASE_DELIVERY_COST = 15.99 # No longer used

# --- Load Logistics Costs ---
logistics_cat_base_cost = {}
try:
    with open(LOGISTICS_CATEGORIES_FILE, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                logistics_cat_base_cost[row['Kategoria_Logistyczna']] = float(row['Koszt_Bazowy'])
            except (ValueError, KeyError) as e:
                 print(f"Skipping row in logistics categories due to error ({e}): {row}")
except FileNotFoundError:
    print(f"Error: Logistics categories file '{LOGISTICS_CATEGORIES_FILE}' not found.")
    exit()
except Exception as e:
    print(f"Error reading logistics categories: {e}")
    exit()

if not logistics_cat_base_cost:
    print("Error: No logistics costs loaded. Cannot generate sales data.")
    exit()

# --- Load Product Catalog with Logistics Category ---
products = []
try:
    with open(PRODUCT_CATALOG_FILE, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                logistics_cat = row['Kategoria_Logistyczna']
                if logistics_cat not in logistics_cat_base_cost:
                    print(f"Warning: Product '{row['Produkt']}' has unknown logistics category '{logistics_cat}'. Skipping product.")
                    continue
                
                products.append({
                    'Produkt': row['Produkt'],
                    'Kategoria': row['Kategoria'],
                    'Cena_Sprzedazy': float(row['Cena_Sprzedazy']), 
                    'Kategoria_Logistyczna': logistics_cat
                })
            except ValueError:
                print(f"Skipping product row due to conversion error: {row}")
            except KeyError as e:
                print(f"Skipping product row due to missing key {e}: {row}")
except FileNotFoundError:
    print(f"Error: Product catalog file '{PRODUCT_CATALOG_FILE}' not found.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the product catalog: {e}")
    exit()

if not products:
    print("Error: No valid products loaded from the catalog. Cannot generate sales data.")
    exit()

# --- Generate Sales Data ---
sales_data = []
header = ['ID_Transakcji', 'Data', 'Kategoria', 'Produkt', 'Cena_Jednostkowa', 'Liczba_Sztuk', 'Wartosc_Zamowienia', 'Koszt_Dostawy', 'Calkowita_Wartosc', 'Region']
sales_data.append(header)

current_transaction_count = {} # To generate unique IDs per day

total_days = (END_DATE - START_DATE).days + 1

for i in range(NUMBER_OF_TRANSACTIONS):
    # Choose a random date
    random_days = random.randrange(total_days)
    transaction_date = START_DATE + timedelta(days=random_days)
    date_str = transaction_date.strftime('%Y-%m-%d')

    # Generate unique transaction ID for the day
    day_key = date_str
    if day_key not in current_transaction_count:
        current_transaction_count[day_key] = 0
    else:
        current_transaction_count[day_key] += 1
    
    transaction_id = f"T{transaction_date.strftime('%Y%m%d')}-{current_transaction_count[day_key]:03d}"

    # Choose a random product (from the valid list)
    product_info = random.choice(products)
    product_name = product_info['Produkt']
    category = product_info['Kategoria']
    unit_price = product_info['Cena_Sprzedazy'] 
    logistics_cat = product_info['Kategoria_Logistyczna']

    # Simulate quantity (mostly 1-3, occasionally more)
    quantity = random.choices([1, 2, 3, 4, 5], weights=[60, 25, 10, 3, 2], k=1)[0]

    # Choose a random region
    region = random.choice(REGIONS)

    # Determine delivery cost = base cost for the category
    delivery_cost = logistics_cat_base_cost[logistics_cat]

    # Calculate values
    order_value = round(unit_price * quantity, 2)
    total_value = round(order_value + delivery_cost, 2)

    # Add row
    sales_data.append([
        transaction_id,
        date_str,
        category,
        product_name,
        unit_price,
        quantity,
        order_value,
        delivery_cost, # Use the base cost directly
        total_value,
        region
    ])

# --- Write to CSV ---
try:
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sales_data)
    print(f"Successfully generated {NUMBER_OF_TRANSACTIONS} transactions in '{OUTPUT_FILE}' using base logistics cost for delivery.")
except IOError:
    print(f"Error: Could not write to file '{OUTPUT_FILE}'. Check permissions.")
except Exception as e:
    print(f"An unexpected error occurred while writing the file: {e}") 