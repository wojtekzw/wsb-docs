import pandas as pd
import os
import calendar

# --- Configuration ---
SALES_FILE = 'sprzedaz.csv'
OUTPUT_DIR = 'output'
SUMMARY_FILE = os.path.join(OUTPUT_DIR, '05_forecasting_summary.md')

# --- Load Data ---
try:
    df = pd.read_csv(SALES_FILE)
    df['Data'] = pd.to_datetime(df['Data'])
    df['Miesiąc'] = df['Data'].dt.month
    print(f"Successfully loaded {SALES_FILE} for forecasting summary.")
except Exception as e:
    print(f"Error loading or processing sales data: {e}")
    exit()

# --- Prepare Monthly Sales Data (Input for Forecasting) ---
monthly_sales = df.groupby('Miesiąc')['Calkowita_Wartosc'].sum().reset_index()
month_names_pl = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
monthly_sales['Nazwa Miesiąca'] = monthly_sales['Miesiąc'].apply(lambda x: month_names_pl[x-1])
monthly_sales = monthly_sales[['Miesiąc', 'Nazwa Miesiąca', 'Calkowita_Wartosc']]

monthly_data_table = monthly_sales[['Miesiąc', 'Calkowita_Wartosc']].to_markdown(index=False, floatfmt=",.2f")

# --- Generate Summary Content ---
summary_content = f"""# Część 5: Prognozowanie i Analiza Zaawansowana (Podsumowanie Koncepcyjne)

Ta część obejmuje prognozowanie przyszłej sprzedaży oraz analizę "Co jeśli". Poniżej przedstawiono koncepcje i dane wejściowe, które można wykorzystać do tych analiz w Excelu lub innych narzędziach.

## Prognozowanie Przyszłej Sprzedaży

Celem jest przewidzenie sprzedaży na kolejne miesiące (np. 3) na podstawie danych historycznych.

### Dane wejściowe (Sprzedaż miesięczna z `{SALES_FILE}`):

{monthly_data_table}

### Metody Prognozowania (wg instrukcji):

1.  **Prognoza Liniowa:**
    -   Wykorzystuje trend liniowy z danych historycznych.
    -   Formuła Excel: `=PROGNOZA.LINIOWA(Miesiąc_Docelowy; Znane_Wartości_Y; Znane_Wartości_X)` lub starsza `REGLINP`.
    -   *Przykład:* Prognoza dla miesiąca 13 (Styczeń 2025) na podstawie danych z 12 miesięcy 2024.

2.  **Prognoza z Uwzględnieniem Sezonowości:**
    -   Prognoza liniowa jest korygowana wskaźnikiem sezonowości dla danego miesiąca.
    -   Wskaźnik sezonowości można obliczyć jako stosunek sprzedaży w danym miesiącu do średniej sprzedaży miesięcznej z poprzedniego roku.
    -   *Przykład:* Prognoza liniowa na Styczeń 2025 * (Sprzedaż Styczeń 2024 / Średnia miesięczna sprzedaż 2024).

3.  **Arkusz Prognozy (Nowsze Wersje Excela):**
    -   Automatyczne narzędzie w Excelu, które wykrywa trendy i sezonowość.

## Analiza "Co jeśli" (Symulacja Zmiany Cen)

Celem jest symulacja wpływu zmiany cen na przychody lub zysk, biorąc pod uwagę elastyczność cenową popytu (jak zmiana ceny wpływa na ilość sprzedaną).

### Koncepcja Modelu (wg instrukcji):

-   Potrzebne są parametry:
    -   `SprzedażBazowa` (np. aktualna wartość sprzedaży lub ilość)
    -   `ElastycznośćCenowa` (współczynnik określający reakcję popytu na zmianę ceny, np. -1.5 oznacza, że 10% wzrost ceny spowoduje 15% spadek popytu)
    -   `ZmianaCeny` (procentowa zmiana ceny, np. 0.1 dla wzrostu o 10%)

-   Przykładowa formuła wpływu na *ilość* sprzedaży:
    `NowaIlość = IlośćBazowa * (1 + ElastycznośćCenowa * ZmianaCeny)`
    *(Uwaga: formuła z instrukcji wydaje się uproszczona; powyższa jest bardziej standardowa dla ilości)*

-   Przykładowa formuła wpływu na *wartość* sprzedaży (zakładając stały koszt):
    `NowyPrzychód = NowaIlość * NowaCena`
    `NowaCena = CenaBazowa * (1 + ZmianaCeny)`

-   W Excelu można użyć formantów (np. suwaków) do łatwej zmiany parametrów `ElastycznośćCenowa` i `ZmianaCeny` i obserwacji wyników.

*Implementacja tych analiz w Pythonie wymagałaby użycia bibliotek statystycznych (np. `statsmodels` dla regresji/prognoz) lub bardziej złożonego kodowania modeli symulacyjnych.*
"""

# --- Save Summary ---
try:
    with open(SUMMARY_FILE, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    print(f"Successfully saved forecasting and advanced analysis summary to {SUMMARY_FILE}")
except Exception as e:
    print(f"Error saving summary file: {e}") 