import csv

total_costs = 0

with open('koszty_wspolne.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_costs += float(row['Wartość'])

print(f"Całkowita wartość kosztów wspólnych: {total_costs:.2f} zł") 