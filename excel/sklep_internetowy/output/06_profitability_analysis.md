# Część 6: Analiza Rentowności

## Metodologia
1.  Połączono dane sprzedażowe z katalogiem produktów (koszt zakupu) i kategoriami logistycznymi (koszt bazowy logistyki).
2.  Obliczono przychód, koszt zakupu sprzedanych towarów (COGS) i koszt logistyczny produktów dla każdej transakcji.
3.  Obliczono marżę brutto na poziomie transakcji (Przychód - COGS - Koszt Logistyczny Produktów).
4.  Zsumowano miesięczną marżę brutto i przychód dla każdej kategorii produktów.
5.  Załadowano miesięczne koszty wspólne i klucze alokacji.
6.  Przydzielono miesięczne koszty wspólne do kategorii produktów zgodnie z kluczami alokacji.
7.  Obliczono zysk netto (Marża Brutto - Przydzielone Koszty Wspólne) i rentowność sprzedaży (Zysk Netto / Przychód) dla każdej kategorii miesięcznie.

## Rentowność Miesięczna według Kategorii

|   Miesiąc | Nazwa Miesiąca   | Kategoria         |   Całkowity_Przychód |   Całkowita_Marża_Brutto |   Przydzielony_Koszt_Wspólny |   Zysk_Netto |   Rentowność_Sprzedaży (%) |
|----------:|:-----------------|:------------------|---------------------:|-------------------------:|-----------------------------:|-------------:|---------------------------:|
|         1 | Styczeń          | Artykuły sportowe |            75,467.80 |                15,773.80 |                    16,350.00 |      -576.20 |                      -0.76 |
|         1 | Styczeń          | Dom i ogród       |            79,236.20 |                19,859.20 |                    21,950.00 |    -2,090.80 |                      -2.64 |
|         1 | Styczeń          | Elektronika       |           300,765.80 |                47,223.80 |                    27,100.00 |    20,123.80 |                       6.69 |
|         1 | Styczeń          | Książki           |            11,570.65 |                 2,525.65 |                    10,000.00 |    -7,474.35 |                     -64.60 |
|         1 | Styczeń          | Odzież            |            37,954.05 |                 8,423.05 |                    17,250.00 |    -8,826.95 |                     -23.26 |
|         1 | Styczeń          | Zabawki           |            22,190.10 |                 4,724.10 |                    16,350.00 |   -11,625.90 |                     -52.39 |
|         2 | Luty             | Artykuły sportowe |            48,102.00 |                 9,989.00 |                    16,350.00 |    -6,361.00 |                     -13.22 |
|         2 | Luty             | Dom i ogród       |            78,215.15 |                19,261.15 |                    21,950.00 |    -2,688.85 |                      -3.44 |
|         2 | Luty             | Elektronika       |           290,366.00 |                45,786.00 |                    27,100.00 |    18,686.00 |                       6.44 |
|         2 | Luty             | Książki           |            10,252.81 |                 2,308.81 |                    10,000.00 |    -7,691.19 |                     -75.02 |
|         2 | Luty             | Odzież            |            34,952.75 |                 7,755.75 |                    17,250.00 |    -9,494.25 |                     -27.16 |
|         2 | Luty             | Zabawki           |            22,607.85 |                 4,774.85 |                    16,350.00 |   -11,575.15 |                     -51.20 |
|         3 | Marzec           | Artykuły sportowe |            83,397.60 |                17,436.60 |                    17,175.00 |       261.60 |                       0.31 |
|         3 | Marzec           | Dom i ogród       |            86,985.15 |                22,045.15 |                    22,850.00 |      -804.85 |                      -0.93 |
|         3 | Marzec           | Elektronika       |           308,522.00 |                48,082.00 |                    28,675.00 |    19,407.00 |                       6.29 |
|         3 | Marzec           | Książki           |            11,905.83 |                 2,628.83 |                    10,350.00 |    -7,721.17 |                     -64.85 |
|         3 | Marzec           | Odzież            |            33,761.15 |                 7,432.15 |                    18,275.00 |   -10,842.85 |                     -32.12 |
|         3 | Marzec           | Zabawki           |            25,412.00 |                 5,366.00 |                    17,175.00 |   -11,809.00 |                     -46.47 |
|         4 | Kwiecień         | Artykuły sportowe |            66,448.80 |                13,992.80 |                    16,980.00 |    -2,987.20 |                      -4.50 |
|         4 | Kwiecień         | Dom i ogród       |            83,475.00 |                20,981.00 |                    22,745.00 |    -1,764.00 |                      -2.11 |
|         4 | Kwiecień         | Elektronika       |           247,738.70 |                39,500.70 |                    28,195.00 |    11,305.70 |                       4.56 |
|         4 | Kwiecień         | Książki           |            11,659.86 |                 2,612.86 |                    10,345.00 |    -7,732.14 |                     -66.31 |
|         4 | Kwiecień         | Odzież            |            37,906.50 |                 8,390.50 |                    17,955.00 |    -9,564.50 |                     -25.23 |
|         4 | Kwiecień         | Zabawki           |            24,231.10 |                 5,122.10 |                    16,980.00 |   -11,857.90 |                     -48.94 |
|         5 | Maj              | Artykuły sportowe |            87,934.40 |                18,417.40 |                    16,980.00 |     1,437.40 |                       1.63 |
|         5 | Maj              | Dom i ogród       |            70,497.05 |                17,463.05 |                    22,745.00 |    -5,281.95 |                      -7.49 |
|         5 | Maj              | Elektronika       |           324,382.20 |                50,854.20 |                    28,195.00 |    22,659.20 |                       6.99 |
|         5 | Maj              | Książki           |            10,873.69 |                 2,333.69 |                    10,345.00 |    -8,011.31 |                     -73.68 |
|         5 | Maj              | Odzież            |            42,410.45 |                 9,225.45 |                    17,955.00 |    -8,729.55 |                     -20.58 |
|         5 | Maj              | Zabawki           |            28,925.05 |                 6,121.05 |                    16,980.00 |   -10,858.95 |                     -37.54 |
|         6 | Czerwiec         | Artykuły sportowe |            49,335.00 |                10,240.00 |                    17,730.00 |    -7,490.00 |                     -15.18 |
|         6 | Czerwiec         | Dom i ogród       |            67,654.25 |                16,977.25 |                    23,570.00 |    -6,592.75 |                      -9.74 |
|         6 | Czerwiec         | Elektronika       |           260,796.70 |                41,078.70 |                    29,620.00 |    11,458.70 |                       4.39 |
|         6 | Czerwiec         | Książki           |             8,992.43 |                 1,980.43 |                    10,670.00 |    -8,689.57 |                     -96.63 |
|         6 | Czerwiec         | Odzież            |            37,463.90 |                 8,195.90 |                    18,880.00 |   -10,684.10 |                     -28.52 |
|         6 | Czerwiec         | Zabawki           |            22,218.90 |                 4,685.90 |                    17,730.00 |   -13,044.10 |                     -58.71 |
|         7 | Lipiec           | Artykuły sportowe |           106,985.20 |                22,433.20 |                    17,640.00 |     4,793.20 |                       4.48 |
|         7 | Lipiec           | Dom i ogród       |            87,118.70 |                21,621.70 |                    23,580.00 |    -1,958.30 |                      -2.25 |
|         7 | Lipiec           | Elektronika       |           293,868.00 |                46,018.00 |                    29,340.00 |    16,678.00 |                       5.68 |
|         7 | Lipiec           | Książki           |            11,150.80 |                 2,430.80 |                    10,710.00 |    -8,279.20 |                     -74.25 |
|         7 | Lipiec           | Odzież            |            31,807.45 |                 6,978.45 |                    18,690.00 |   -11,711.55 |                     -36.82 |
|         7 | Lipiec           | Zabawki           |            23,041.25 |                 4,972.25 |                    17,640.00 |   -12,667.75 |                     -54.98 |
|         8 | Sierpień         | Artykuły sportowe |            77,372.00 |                16,078.00 |                    17,640.00 |    -1,562.00 |                      -2.02 |
|         8 | Sierpień         | Dom i ogród       |            76,547.50 |                19,248.50 |                    23,580.00 |    -4,331.50 |                      -5.66 |
|         8 | Sierpień         | Elektronika       |           303,798.50 |                48,138.50 |                    29,340.00 |    18,798.50 |                       6.19 |
|         8 | Sierpień         | Książki           |            13,313.22 |                 2,937.22 |                    10,710.00 |    -7,772.78 |                     -58.38 |
|         8 | Sierpień         | Odzież            |            36,409.10 |                 8,057.10 |                    18,690.00 |   -10,632.90 |                     -29.20 |
|         8 | Sierpień         | Zabawki           |            26,912.75 |                 5,662.75 |                    17,640.00 |   -11,977.25 |                     -44.50 |
|         9 | Wrzesień         | Artykuły sportowe |            71,959.00 |                14,973.00 |                    18,165.00 |    -3,192.00 |                      -4.44 |
|         9 | Wrzesień         | Dom i ogród       |            70,469.85 |                17,491.85 |                    24,105.00 |    -6,613.15 |                      -9.38 |
|         9 | Wrzesień         | Elektronika       |           283,137.10 |                44,483.10 |                    30,390.00 |    14,093.10 |                       4.98 |
|         9 | Wrzesień         | Książki           |            10,902.76 |                 2,422.76 |                    10,885.00 |    -8,462.24 |                     -77.62 |
|         9 | Wrzesień         | Odzież            |            36,205.75 |                 8,014.75 |                    19,390.00 |   -11,375.25 |                     -31.42 |
|         9 | Wrzesień         | Zabawki           |            26,760.60 |                 5,627.60 |                    18,165.00 |   -12,537.40 |                     -46.85 |
|        10 | Październik      | Artykuły sportowe |            73,362.20 |                15,278.20 |                    18,810.00 |    -3,531.80 |                      -4.81 |
|        10 | Październik      | Dom i ogród       |            71,224.50 |                17,963.50 |                    24,870.00 |    -6,906.50 |                      -9.70 |
|        10 | Październik      | Elektronika       |           328,506.40 |                51,520.40 |                    31,560.00 |    19,960.40 |                       6.08 |
|        10 | Październik      | Książki           |             9,849.03 |                 2,159.03 |                    11,190.00 |    -9,030.97 |                     -91.69 |
|        10 | Październik      | Odzież            |            36,938.55 |                 8,045.55 |                    20,160.00 |   -12,114.45 |                     -32.80 |
|        10 | Październik      | Zabawki           |            33,553.70 |                 7,122.70 |                    18,810.00 |   -11,687.30 |                     -34.83 |
|        11 | Listopad         | Artykuły sportowe |            80,009.80 |                16,740.80 |                    19,560.00 |    -2,819.20 |                      -3.52 |
|        11 | Listopad         | Dom i ogród       |            93,582.80 |                23,876.80 |                    25,720.00 |    -1,843.20 |                      -1.97 |
|        11 | Listopad         | Elektronika       |           222,332.90 |                35,186.90 |                    32,960.00 |     2,226.90 |                       1.00 |
|        11 | Listopad         | Książki           |             8,594.41 |                 1,893.41 |                    11,540.00 |    -9,646.59 |                    -112.24 |
|        11 | Listopad         | Odzież            |            33,738.35 |                 7,399.35 |                    21,060.00 |   -13,660.65 |                     -40.49 |
|        11 | Listopad         | Zabawki           |            22,886.80 |                 4,838.80 |                    19,560.00 |   -14,721.20 |                     -64.32 |
|        12 | Grudzień         | Artykuły sportowe |            69,502.20 |                14,454.20 |                    21,045.00 |    -6,590.80 |                      -9.48 |
|        12 | Grudzień         | Dom i ogród       |            79,519.65 |                19,815.65 |                    27,525.00 |    -7,709.35 |                      -9.69 |
|        12 | Grudzień         | Elektronika       |           275,939.00 |                43,939.00 |                    35,610.00 |     8,329.00 |                       3.02 |
|        12 | Grudzień         | Książki           |            12,545.00 |                 2,773.00 |                    12,280.00 |    -9,507.00 |                     -75.78 |
|        12 | Grudzień         | Odzież            |            34,236.80 |                 7,448.80 |                    22,795.00 |   -15,346.20 |                     -44.82 |
|        12 | Grudzień         | Zabawki           |            24,625.85 |                 5,251.85 |                    21,045.00 |   -15,793.15 |                     -64.13 |

## Analiza Rentowności Produktów (Top 5 wg Marży Brutto)

| Produkt                       |   Całkowita_Marża_Brutto |   Liczba_Sprzedanych_Sztuk |
|:------------------------------|-------------------------:|---------------------------:|
| Laptop ProBook Air            |               229,507.50 |                        355 |
| Rower górski XTerra           |               146,216.00 |                        392 |
| Smartfon Galaxy X20           |               144,326.00 |                        427 |
| Zestaw mebli ogrodowych Relax |               140,798.00 |                        445 |
| Tablet MediaPad 10            |                85,446.00 |                        423 |

## Analiza Rentowności Produktów (Najniższa Marża Brutto - Bottom 5)

| Produkt                    |   Całkowita_Marża_Brutto |   Liczba_Sprzedanych_Sztuk |
|:---------------------------|-------------------------:|---------------------------:|
| Kryminał 'Ciemna Noc'      |                 3,128.40 |                        395 |
| Powieść 'Tajemnica Gór'    |                 3,176.25 |                        363 |
| Poradnik 'Skuteczny Excel' |                 5,064.78 |                        389 |
| T-shirt BasicColor         |                 5,665.00 |                        412 |
| Puzzle 1000el. WorldMap    |                 5,967.00 |                        390 |

*Uwaga: Analiza rentowności produktu opiera się na Marży Brutto (przed alokacją kosztów wspólnych), ponieważ alokacja kosztów wspólnych na pojedynczy produkt jest często złożona i wykracza poza typowe dane wejściowe.*
