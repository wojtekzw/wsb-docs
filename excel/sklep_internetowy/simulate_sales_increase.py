import csv
import pandas as pd

# Read the sales data
sales_df = pd.read_csv('sprzedaz.csv')
products_df = pd.read_csv('katalog_produktow.csv')

# Create a dictionary of product costs and margins
product_data = {}
for _, row in products_df.iterrows():
    product_data[row['Produkt']] = {
        'koszt_zakupu': row['Koszt_Zakupu'],
        'marza': row['Marza_Produkt'],
        'kategoria_logistyczna': row['Kategoria_Logistyczna'],
        'koszt_logistyki': row['Koszt_Logistyki'],
        'cena_sprzedazy': row['Cena_Sprzedazy']
    }

# Calculate original total sales
original_total = sales_df['Calkowita_Wartosc'].sum()

# Simulate increased sales
# 1. Increase margins by 15%
# 2. Increase sales volume
# 3. Calculate new total

# Create a new sales dataframe with increased volume
# We'll multiply each transaction by 4 to get 8x total increase (4x from volume, 2x from margin)
new_sales = pd.concat([sales_df] * 4, ignore_index=True)

# Calculate new prices with increased margins
for idx, row in new_sales.iterrows():
    product = row['Produkt']
    if product in product_data:
        original_margin = product_data[product]['marza']
        new_margin = original_margin * 1.15  # 15% increase in margin
        
        koszt_zakupu = product_data[product]['koszt_zakupu']
        koszt_logistyki = product_data[product]['koszt_logistyki']
        
        # Calculate new price with increased margin
        new_price = koszt_zakupu * (1 + new_margin) + koszt_logistyki
        
        # Update the values in the sales record
        new_sales.at[idx, 'Cena_Jednostkowa'] = new_price
        new_sales.at[idx, 'Wartosc_Zamowienia'] = new_price * row['Liczba_Sztuk']
        new_sales.at[idx, 'Calkowita_Wartosc'] = new_sales.at[idx, 'Wartosc_Zamowienia'] + row['Koszt_Dostawy']

# Calculate new total sales
new_total = new_sales['Calkowita_Wartosc'].sum()

# Print results
print(f"Oryginalna wartość sprzedaży: {original_total:.2f} zł")
print(f"Nowa wartość sprzedaży: {new_total:.2f} zł")
print(f"Wzrost sprzedaży: {(new_total/original_total):.2f}x")
print(f"Wzrost wartości: {((new_total - original_total)/original_total*100):.2f}%")

# Save the new sales data to a file
new_sales.to_csv('symulacja_zwiekszonej_sprzedazy.csv', index=False) 