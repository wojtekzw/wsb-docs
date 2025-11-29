# Część 7: Optymalizacja Struktury Sprzedaży i Rekomendacje

## Analiza Struktury Sprzedaży i Rentowności Rocznej

Poniższa tabela przedstawia udział poszczególnych kategorii w całkowitych przychodach oraz ich roczną rentowność sprzedaży (na podstawie uproszczonej alokacji kosztów wspólnych proporcjonalnie do przychodów).

| Kategoria         |   Udział_w_Przychodach (%) |   Rentowność_Sprzedaży_Roczna (%) |   Całkowity_Przychód |   Zysk_Netto_Roczny |
|:------------------|---------------------------:|----------------------------------:|---------------------:|--------------------:|
| Dom i ogród       |                      15.37 |                              1.78 |           944,525.80 |           16,821.29 |
| Książki           |                       2.14 |                             -1.23 |           131,610.49 |           -1,618.21 |
| Odzież            |                       7.06 |                             -1.28 |           433,784.80 |           -5,571.41 |
| Zabawki           |                       4.94 |                             -2.08 |           303,365.95 |           -6,320.85 |
| Artykuły sportowe |                      14.49 |                             -2.39 |           889,876.00 |          -21,259.94 |
| Elektronika       |                      56.00 |                             -7.52 |         3,440,153.30 |         -258,684.53 |

## Rekomendacje Biznesowe

### Optymalizacja Struktury Sprzedaży:
-   **Promuj Kategorie Wysoko Rentowne:** Skupić działania marketingowe i promocyjne na kategoriach z najwyższą rentownością, takich jak:
    -   Dom i ogród
    -   Książki
    -   Odzież
-   **Analiza Kategorii Nisko Rentownych:** Dokładnie przeanalizować kategorie o niskiej lub ujemnej rentowności:
    -   Zabawki
    -   Artykuły sportowe
    -   Elektronika
    Rozważyć optymalizację kosztów (zakupu, logistyki), renegocjację cen lub nawet wycofanie najmniej rentownych produktów w tych kategoriach.

### Działania Natychmiastowe (Kategorie Stratne):
-   Kategorie generujące stratę netto wymagają pilnej interwencji:
    -   Książki
    -   Odzież
    -   Zabawki
    -   Artykuły sportowe
    -   Elektronika
    Należy zbadać przyczyny (wysokie koszty, niska marża, błędy w danych?) i podjąć decyzje naprawcze.

### Optymalizacja Cen i Marż:
-   Rozważyć ostrożne podniesienie cen dla produktów o niskiej elastyczności cenowej w kategoriach wysoko rentownych.
-   Przeanalizować możliwość renegocjacji cen zakupu z dostawcami dla produktów o niskiej marży brutto, szczególnie w kategoriach o dużym udziale w sprzedaży.

### Optymalizacja Kosztów:
-   **Logistyka:** Zbadać, czy koszty logistyczne (`Koszt_Bazowy`) dla poszczególnych kategorii są adekwatne i czy istnieją możliwości ich optymalizacji (np. zmiana dostawcy usług logistycznych, optymalizacja pakowania).
-   **Koszty Wspólne:** Przeanalizować strukturę kosztów wspólnych i zasadność ich alokacji. Czy klucze alokacji (`klucze_alokacji.csv`) odzwierciedlają rzeczywiste zużycie zasobów przez kategorie?

## Model Optymalizacyjny (Koncepcja)

Do dalszej optymalizacji można stworzyć model (np. w Excelu z użyciem Solver'a), który pozwoliłby symulować:
-   Zmiany w procentowym udziale sprzedaży poszczególnych kategorii.
-   Zmiany w marżach produktów.
-   Zmiany w kosztach (logistycznych, wspólnych).
Celem byłoby znalezienie kombinacji maksymalizującej całkowity zysk netto przy zadanych ograniczeniach.
