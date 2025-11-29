import csv

# --- Configuration ---
SALES_FILE = 'sprzedaz.csv'
PRODUCT_CATALOG_FILE = 'katalog_produktow.csv'
LOGISTICS_CATEGORIES_FILE = 'kategorie_logistyczne.csv'
TOLERANCE = 0.20 # 20%

# --- Load Mappings ---
product_to_logistics_cat = {}
try:
    with open(PRODUCT_CATALOG_FILE, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product_to_logistics_cat[row['Produkt']] = row['Kategoria_Logistyczna']
except FileNotFoundError:
    print(f"Error: Product catalog file '{PRODUCT_CATALOG_FILE}' not found.")
    exit()
except Exception as e:
    print(f"Error reading product catalog: {e}")
    exit()

logistics_cat_base_cost = {}
try:
    with open(LOGISTICS_CATEGORIES_FILE, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                logistics_cat_base_cost[row['Kategoria_Logistyczna']] = float(row['Koszt_Bazowy'])
            except ValueError:
                 print(f"Skipping row in logistics categories due to conversion error: {row}")
except FileNotFoundError:
    print(f"Error: Logistics categories file '{LOGISTICS_CATEGORIES_FILE}' not found.")
    exit()
except Exception as e:
    print(f"Error reading logistics categories: {e}")
    exit()

# --- Validate Delivery Costs ---
out_of_range_transactions = []
transactions_checked = 0
missing_product_data = 0
missing_logistics_data = 0

try:
    with open(SALES_FILE, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions_checked += 1
            try:
                transaction_id = row['ID_Transakcji']
                product = row['Produkt']
                delivery_cost_actual = float(row['Koszt_Dostawy'])

                # Get logistics category for the product
                if product not in product_to_logistics_cat:
                    missing_product_data += 1
                    # Optionally report this specific transaction
                    # print(f"Warning: Product '{product}' (ID: {transaction_id}) not found in catalog.")
                    continue # Skip validation if product data is missing
                
                logistics_cat = product_to_logistics_cat[product]

                # Get base cost for the logistics category
                if logistics_cat not in logistics_cat_base_cost:
                    missing_logistics_data += 1
                    # Optionally report this specific transaction
                    # print(f"Warning: Logistics category '{logistics_cat}' (Product: {product}, ID: {transaction_id}) not found in logistics costs.")
                    continue # Skip validation if logistics cost data is missing
                
                base_cost = logistics_cat_base_cost[logistics_cat]

                # Calculate tolerance range
                lower_bound = base_cost * (1 - TOLERANCE)
                upper_bound = base_cost * (1 + TOLERANCE)

                # Check if actual cost is within range
                if not (lower_bound <= delivery_cost_actual <= upper_bound):
                    out_of_range_transactions.append({
                        'ID': transaction_id,
                        'Produkt': product,
                        'Kat_Logistyczna': logistics_cat,
                        'Koszt_Dostawy_Aktualny': delivery_cost_actual,
                        'Koszt_Bazowy': base_cost,
                        'Zakres_Oczekiwany': f"{lower_bound:.2f} - {upper_bound:.2f}"
                    })

            except ValueError:
                print(f"Skipping row in sales data due to conversion error: {row}")
            except KeyError as e:
                 print(f"Skipping row in sales data due to missing key {e}: {row}")

except FileNotFoundError:
    print(f"Error: Sales file '{SALES_FILE}' not found.")
    exit()
except Exception as e:
    print(f"An error occurred while processing sales data: {e}")
    exit()

# --- Report Results ---
print(f"\n--- Validation Report: Delivery Cost vs. Base Logistics Cost (+/- {TOLERANCE*100}%) ---")
print(f"Total transactions checked: {transactions_checked}")
if missing_product_data > 0:
    print(f"Warning: Skipped {missing_product_data} transactions due to missing product data in catalog.")
if missing_logistics_data > 0:
     print(f"Warning: Skipped {missing_logistics_data} transactions due to missing logistics category data.")

if not out_of_range_transactions:
    print("\nAll checked transactions have delivery costs within the expected range.")
else:
    print(f"\nFound {len(out_of_range_transactions)} transactions with delivery costs outside the expected range:")
    # Print details for a few examples
    max_to_print = 15
    for i, tx in enumerate(out_of_range_transactions):
        if i < max_to_print:
             print(f"  - ID: {tx['ID']}, Produkt: {tx['Produkt']}, Kat. Log: {tx['Kat_Logistyczna']}, Koszt akt: {tx['Koszt_Dostawy_Aktualny']}, Koszt baz: {tx['Koszt_Bazowy']}, Zakres oczek: {tx['Zakres_Oczekiwany']}")
        elif i == max_to_print:
             print(f"  ... (and {len(out_of_range_transactions) - max_to_print} more)")
             break 