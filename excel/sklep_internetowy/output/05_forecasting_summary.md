# Część 5: Prognozowanie i Analiza Zaawansowana (Podsumowanie Koncepcyjne)

Ta część obejmuje prognozowanie przyszłej sprzedaży oraz analizę "Co jeśli". Poniżej przedstawiono koncepcje i dane wejściowe, które można wykorzystać do tych analiz w Excelu lub innych narzędziach.

## Prognozowanie Przyszłej Sprzedaży

Celem jest przewidzenie sprzedaży na kolejne miesiące (np. 3) na podstawie danych historycznych.

### Dane wejściowe (Sprzedaż miesięczna z `sprzedaz.csv`):

|   Miesiąc |   Calkowita_Wartosc |
|----------:|--------------------:|
|      1.00 |          538,632.60 |
|      2.00 |          494,576.56 |
|      3.00 |          562,007.73 |
|      4.00 |          481,879.96 |
|      5.00 |          577,470.84 |
|      6.00 |          456,853.18 |
|      7.00 |          565,619.40 |
|      8.00 |          546,013.07 |
|      9.00 |          511,047.06 |
|     10.00 |          565,466.38 |
|     11.00 |          471,933.06 |
|     12.00 |          507,356.50 |

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
