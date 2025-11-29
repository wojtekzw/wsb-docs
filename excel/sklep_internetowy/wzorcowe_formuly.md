# Wzorcowe formuły i rozwiązania

Ten dokument zawiera przykładowe formuły i rozwiązania dla kluczowych elementów zadania "Analiza sprzedaży sklepu internetowego". Dokument ten jest przeznaczony dla prowadzącego zajęcia jako pomoc w ocenie prac studentów.

## Część 1: Import i przygotowanie danych

### Formuły dla kolumn pomocniczych:

```
Miesiąc: =MIESIĄC([@Data])
Kwartał: =ZAOKR.W.GÓRĘ([@Miesiąc]/3;0)
Dzień tygodnia: =DZIEŃ.TYG([@Data];2)  # 2 oznacza, że poniedziałek jest pierwszym dniem tygodnia (wartość 1)
```

## Część 2: Analiza podstawowa

### Kluczowe wskaźniki sprzedaży:

```
Sumaryczna wartość sprzedaży: =SUMA(DaneSprzedazy[Calkowita_Wartosc])
Liczba unikalnych transakcji: =LICZ(DaneSprzedazy[ID_Transakcji])
Średnia wartość zamówienia: =ŚREDNIA(DaneSprzedazy[Calkowita_Wartosc])
Najwyższa wartość zamówienia: =MAX(DaneSprzedazy[Calkowita_Wartosc])
Najniższa wartość zamówienia: =MIN(DaneSprzedazy[Calkowita_Wartosc])
```

### Udział procentowy kategorii w sprzedaży:

Formuła w tabeli przestawnej lub poza nią:
```
=B4/SUMA($B$4:$B$9)  # gdzie B4:B9 to wartości sprzedaży dla poszczególnych kategorii
```

## Część 3: Analiza czasowa i sezonowość

### Dynamika sprzedaży miesiąc do miesiąca:

Metoda 1 - Bezpośrednie obliczenie dla drugiego i kolejnych miesięcy:
```
=(B5-B4)/B4  # gdzie B4 i B5 to wartości sprzedaży dla stycznia i lutego
```

Metoda 2 - Jako pole obliczeniowe w tabeli przestawnej:
```
=([Calkowita_Wartosc] - PRZESUNIĘCIE([Calkowita_Wartosc];-1;0))/PRZESUNIĘCIE([Calkowita_Wartosc];-1;0)
```

## Część 4: Wizualizacja danych i dashboard

### Formuła do pobierania danych z tabeli przestawnej do KPI:

```
=WEŹDANETABELI("Suma z Calkowita_Wartosc";"TabelaPrzestawna1";"Całość";"Całość")
```

### Formuła do obliczenia dynamiki (procentowej zmiany) rok do roku:

```
=(SUMA(JEŻELI(DaneSprzedazy[Miesiąc]>6;DaneSprzedazy[Calkowita_Wartosc];0))/SUMA(JEŻELI(DaneSprzedazy[Miesiąc]<=6;DaneSprzedazy[Calkowita_Wartosc];0))-1)
```

## Część 5: Prognozowanie i analiza zaawansowana

### Prosta formuła do prognozy liniowej:

```
=REGLINP(13;TabMiesięczna[Miesiąc];TabMiesięczna[Wartość];PRAWDA)
```

lub dla nowszych wersji Excela:

```
=PROGNOZA.LINIOWA(13;TabMiesięczna[Miesiąc];TabMiesięczna[Wartość])
```

### Prognoza z uwzględnieniem sezonowości:

Dla prognozy na styczeń 2025 (miesiąc 13), przy założeniu podobnej sezonowości jak w roku poprzednim:
```
=REGLINP(13;TabMiesięczna[Miesiąc];TabMiesięczna[Wartość];PRAWDA) * (TabMiesięczna[@Wartość]{1} / ŚREDNIA(TabMiesięczna[Wartość]))
```

lub dla nowszych wersji Excela:

```
=PROGNOZA.LINIOWA(13;TabMiesięczna[Miesiąc];TabMiesięczna[Wartość]) * (TabMiesięczna[@Wartość]{1} / ŚREDNIA(TabMiesięczna[Wartość]))
```

Gdzie:
- `TabMiesięczna[Miesiąc]` to liczby od 1 do 12 oznaczające miesiące
- `TabMiesięczna[Wartość]` to wartości sprzedaży w tych miesiącach
- `TabMiesięczna[@Wartość]{1}` to wartość sprzedaży ze stycznia 2024

### Model "Co jeśli" do symulacji wpływu zmiany cen:

```
=SprzedażBazowa * (1 + ElastycznośćCenowa * (1 - ZmianaCeny))
```

Gdzie:
- `SprzedażBazowa` to aktualna wartość sprzedaży
- `ElastycznośćCenowa` to parametr określający wrażliwość sprzedaży na zmiany cen (np. -0.7)
- `ZmianaCeny` to procentowa zmiana ceny (np. 0.1 dla wzrostu o 10%)

## Wskazówki dotyczące formatowania warunkowego

### Formatowanie warunkowe dla analizy sezonowości:

1. Zaznacz zakres danych z wartościami sprzedaży miesięcznej
2. Przejdź do zakładki "Narzędzia główne" > "Formatowanie warunkowe" > "Kolorowa skala"
3. Wybierz skalę kolorów, np. od czerwonego (najniższe wartości) do zielonego (najwyższe wartości)

### Formatowanie warunkowe dla KPI:

1. Zaznacz komórkę z dynamiką sprzedaży
2. Przejdź do zakładki "Narzędzia główne" > "Formatowanie warunkowe" > "Reguły wyróżniania komórek" > "Większe niż..."
3. Ustaw wartość 0 i wybierz formatowanie zielone
4. Dodaj kolejną regułę "Mniejsze niż..." z wartością 0 i formatowaniem czerwonym

## Przykładowe wykresy

### Wykres kolumnowy sprzedaży miesięcznej:

1. Zaznacz tabelę przestawną z danymi sprzedaży miesięcznej
2. Przejdź do zakładki "Wstawianie" > "Kolumnowy" > wybierz typ wykresu kolumnowego 2-W
3. Dostosuj tytuł, etykiety danych i legendę
4. Dodaj linię trendu: kliknij prawym przyciskiem myszy na serię danych > "Dodaj linię trendu" > wybierz typ "Liniowa"

### Wykres kołowy udziału kategorii w sprzedaży:

1. Zaznacz tabelę przestawną z danymi kategorii i wartościami sprzedaży
2. Przejdź do zakładki "Wstawianie" > "Kołowy"
3. Dodaj etykiety danych: kliknij prawym przyciskiem myszy na wykres > "Dodaj etykiety danych"
4. Dostosuj format etykiet: kliknij prawym przyciskiem myszy na etykiety > "Format etykiet danych" > zaznacz "Wartość" i "Procent"

## Fragmentatory (slicery) do dashboardu

Aby dodać fragmentator:
1. Zaznacz dowolną tabelę przestawną
2. Przejdź do zakładki "Analiza tabel przestawnych" > "Filtr" > "Wstaw fragmentator"
3. Wybierz pola do filtrowania (np. Kategoria, Region, Kwartał)
4. Dostosuj wygląd fragmentatora: 
   - Przejdź do zakładki "Opcje fragmentatora"
   - Dostosuj układ kolumn, wysokość przycisków, kolory i styl
5. Połącz fragmentator z wieloma tabelami przestawnymi:
   - Przejdź do zakładki "Opcje fragmentatora" > "Połączenia raportów"
   - Zaznacz wszystkie tabele przestawne, które mają być filtrowane przez ten fragmentator

## Wskazówki dotyczące optymalizacji pracy w Excelu

### Nazwy zakresów:

Definiowanie nazw dla często używanych zakresów poprawia czytelność formuł i ułatwia ich modyfikację:
1. Zaznacz zakres danych
2. W polu Nazwa (lewy górny róg arkusza) wpisz nazwę (np. "SprzedażMiesięczna")
3. Naciśnij Enter

### Łącza między arkuszami:

1. Kliknij prawym przyciskiem myszy na zakładkę arkusza
2. Wybierz "Wstaw hiperłącze"
3. Wybierz "Miejsce w tym dokumencie"
4. Wybierz arkusz docelowy

### Kondensowanie danych na dashboardzie:

1. Użyj formuły INDEKS/PODAJ.POZYCJĘ do wyświetlania top N pozycji:
```
=INDEKS(DaneSprzedazy[Produkt];PODAJ.POZYCJĘ(N;TOP_N_Sprzedaż;"";0))
```

2. Użyj formatowania warunkowego w panelu KPI, aby szybko przekazać status wartości:
   - Ikony warunkowe (strzałki, znaczniki) 
   - Paski danych
   - Zestawy ikon (3 symbole)

## Uwagi końcowe

Powyższe formuły i wskazówki są przykładami rozwiązań i mogą wymagać dostosowania do konkretnej struktury skoroszytu utworzonego przez studenta. Zawsze oceniaj podejście studenta do rozwiązania, nie tylko zgodność z tymi wzorcami.

Pamiętaj, że w Excelu często istnieje wiele sposobów osiągnięcia tego samego rezultatu, więc bądź otwarty na alternatywne rozwiązania, które również prowadzą do poprawnych wyników.
