# Część 1: Podsumowanie Przygotowania Danych

## Źródło danych
- Plik: `sprzedaz.csv`

## Wykonane kroki
1.  Załadowano dane sprzedażowe.
2.  Przekonwertowano kolumnę 'Data' na format daty i czasu.
3.  Dodano kolumny pomocnicze:
    -   `Miesiąc`: Numer miesiąca (1-12).
    -   `Kwartał`: Numer kwartału (1-4).
    -   `Dzień tygodnia`: Numer dnia tygodnia (1=Poniedziałek, 7=Niedziela, zgodnie z ISO 8601 / Excel DZIEŃ.TYG z typem 2).

## Podstawowe informacje o danych po przygotowaniu
-   Liczba transakcji (wierszy): 7500
-   Liczba kolumn: 13
-   Zakres dat: 2024-01-01 do 2024-12-31

## Pierwsze 5 wierszy przetworzonych danych:
```
| ID_Transakcji   | Data                | Kategoria   | Produkt                    |   Cena_Jednostkowa |   Liczba_Sztuk |   Wartosc_Zamowienia |   Koszt_Dostawy |   Calkowita_Wartosc | Region    |   Miesiąc |   Kwartał |   Dzień tygodnia |
|:----------------|:--------------------|:------------|:---------------------------|-------------------:|---------------:|---------------------:|----------------:|--------------------:|:----------|----------:|----------:|-----------------:|
| T20241104-000   | 2024-11-04 00:00:00 | Zabawki     | Puzzle 1000el. WorldMap    |               72.3 |              2 |                144.6 |              12 |               156.6 | Północny  |        11 |         4 |                1 |
| T20240601-000   | 2024-06-01 00:00:00 | Odzież      | Kurtka zimowa męska Alpine |              378.4 |              2 |                756.8 |              20 |               776.8 | Centralny |         6 |         2 |                6 |
| T20240428-000   | 2024-04-28 00:00:00 | Elektronika | Laptop ProBook Air         |             4036.5 |              1 |               4036.5 |              40 |              4076.5 | Centralny |         4 |         2 |                7 |
| T20241209-000   | 2024-12-09 00:00:00 | Odzież      | Sukienka letnia Sunshine   |              160.2 |              2 |                320.4 |              12 |               332.4 | Wschodni  |        12 |         4 |                1 |
| T20240702-000   | 2024-07-02 00:00:00 | Odzież      | Sukienka letnia Sunshine   |              160.2 |              1 |                160.2 |              12 |               172.2 | Północny  |         7 |         3 |                2 |
```
