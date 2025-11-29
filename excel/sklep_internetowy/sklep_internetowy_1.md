# Analiza sprzedaży i rentowności sklepu internetowego

## Opis zadania
W ramach tego zadania będziesz pracować jako analityk danych w sklepie internetowym, który sprzedaje produkty z różnych kategorii: Elektronika, Odzież, Artykuły sportowe, Książki, Dom i ogród oraz Zabawki. Masz dostęp do danych sprzedażowych z całego 2024 roku. Twoim zadaniem jest przeprowadzenie kompleksowej analizy, która pozwoli na zrozumienie trendów sprzedaży, sezonowości, najpopularniejszych produktów, zróżnicowania regionalnego oraz rentowności poszczególnych kategorii produktów.

## Cele zadania
1. Stworzenie modelu danych sprzedażowych z podziałem na kategorie produktów
2. Implementacja formuł warunkowych do analizy trendów sprzedaży
3. Utworzenie interaktywnego pulpitu nawigacyjnego (dashboard) z filtrami
4. Prognozowanie przyszłej sprzedaży na podstawie danych historycznych
5. Analiza rentowności sprzedaży poszczególnych kategorii produktów


## Materiały
Do wykonania zadania będziesz potrzebować następujących plików z katalogu `sklep_internetowy`:
- `sprzedaz.csv` - dane sprzedażowe za rok 2024
- `katalog_produktow_rozszerzony.csv` - rozszerzony katalog produktów zawierający dane o kosztach zakupu, marżach indywidualnych i kategoriach logistycznych
- `kategorie_logistyczne.csv` - opis kategorii logistycznych i ich kosztów
- `koszty_wspolne.csv` - dane o kosztach wspólnych w podziale na miesiące
- `klucze_alokacji.csv` - klucze alokacji kosztów wspólnych na kategorie produktów


## Zadania szczegółowe

### Część 1: Import i przygotowanie danych (30 minut)

1. **Import danych z pliku CSV:**
   - Otwórz nowy skoroszyt Excel
   - Przejdź do zakładki "Dane" na wstążce
   - Wybierz "Z tekstu/CSV"
   - Znajdź i wybierz plik `sprzedaz.csv`
   - W oknie podglądu upewnij się, że dane są prawidłowo rozdzielone (separatorem powinien być średnik, kodowanie UTF-8)
   - Kliknij "Załaduj"

   > **Podpowiedź:** W oknie importu możesz od razu określić typy danych dla poszczególnych kolumn, na przykład ustaw typ "Data" dla kolumny "Data" i typ "Liczba dziesiętna" dla kolumn zawierających wartości pieniężne.

2. **Formatowanie danych:**
   - Sformatuj dane jako tabelę (zakładka "Wstawianie" > "Tabela")
   - Nadaj tabeli nazwę "DaneSprzedazy"
   - Zastosuj odpowiednie formaty liczbowe:
     - Dla kolumn z cenami i wartościami zastosuj format walutowy (zł)
     - Dla kolumny z datą zastosuj wybrany format daty

   > **Podpowiedź:** Aby szybko sformatować kolumnę, zaznacz ją, kliknij prawym przyciskiem myszy i wybierz "Formatuj komórki".

3. **Utworzenie dodatkowych kolumn pomocniczych:**
   - Dodaj kolumnę "Miesiąc" - wyodrębnij miesiąc z daty (funkcja MIESIĄC)
   - Dodaj kolumnę "Kwartał" - oblicz kwartał na podstawie miesiąca (funkcja ZAOKR.W.GÓRĘ)
   - Dodaj kolumnę "Dzień tygodnia" - określ dzień tygodnia dla każdej transakcji (funkcja DZIEŃ.TYG)

   > **Podpowiedź:** Użyj formuły `=MIESIĄC([@Data])` dla kolumny Miesiąc oraz `=ZAOKR.W.GÓRĘ([@Miesiąc]/3;0)` dla kolumny Kwartał.

### Część 2: Analiza podstawowa (45 minut)

1. **Utworzenie arkusza "Analiza_Podstawowa":**
   - Utwórz nowy arkusz o nazwie "Analiza_Podstawowa"
   
2. **Obliczenie kluczowych wskaźników sprzedaży:**
   - Sumaryczna wartość sprzedaży (ogółem)
   - Liczba unikalnych transakcji
   - Średnia wartość zamówienia
   - Najwyższa i najniższa wartość zamówienia

   > **Podpowiedź:** Możesz użyć funkcji SUMA, LICZ.JEŻELI, ŚREDNIA, MAX, MIN lub funkcji tablicowych, np. `=SUMA(DaneSprzedazy[Calkowita_Wartosc])`

3. **Analiza sprzedaży według kategorii produktów:**
   - Utwórz tabelę przestawną pokazującą:
     - Wartość sprzedaży według kategorii
     - Liczbę sprzedanych sztuk według kategorii
     - Średnią wartość zamówienia według kategorii
   - Dodaj podsumowanie procentowe dla udziału każdej kategorii w całkowitej sprzedaży

   > **Podpowiedź:** Aby utworzyć tabelę przestawną, przejdź do zakładki "Wstawianie" > "Tabela przestawna". Dodaj pole "Kategoria" do obszaru wierszy oraz odpowiednie pola wartości do obszaru wartości.

4. **Analiza sprzedaży według regionów:**
   - Utwórz tabelę przestawną pokazującą:
     - Wartość sprzedaży według regionów
     - Liczba transakcji według regionów
   - Dodaj analizę kategorii produktów w poszczególnych regionach

   > **Podpowiedź:** Dodaj pola "Region" i "Kategoria" do obszaru wierszy tabeli przestawnej.

### Część 3: Analiza czasowa i sezonowość (45 minut)

1. **Utworzenie arkusza "Analiza_Czasowa":**
   - Utwórz nowy arkusz o nazwie "Analiza_Czasowa"

2. **Analiza sprzedaży miesięcznej:**
   - Utwórz tabelę przestawną pokazującą sprzedaż w podziale na miesiące
   - Oblicz dynamikę sprzedaży miesiąc do miesiąca (procentowa zmiana)
   - Zidentyfikuj miesiące z najwyższą i najniższą sprzedażą

   > **Podpowiedź:** W tabeli przestawnej dodaj pole "Miesiąc" do obszaru wierszy oraz sumę z "Calkowita_Wartosc" do obszaru wartości. Do obliczenia dynamiki możesz dodać obliczone pole z formułą wykorzystującą funkcję procentowej różnicy.

3. **Analiza sezonowości według kategorii:**
   - Utwórz tabelę przestawną z miesiącami w wierszach i kategoriami w kolumnach
   - Zidentyfikuj wzorce sezonowe dla różnych kategorii produktów
   - Zastosuj formatowanie warunkowe, aby wyróżnić okresy szczytowe

   > **Podpowiedź:** Użyj formatowania warunkowego typu "Paski danych" lub "Kolorowa skala" aby wizualnie podkreślić zmiany sezonowe.

4. **Analiza sprzedaży według dni tygodnia:**
   - Utwórz tabelę przestawną pokazującą sprzedaż w zależności od dnia tygodnia
   - Oblicz, który dzień tygodnia generuje najwyższą sprzedaż
   - Sprawdź, czy istnieją różnice w strukturze zakupów w zależności od dnia tygodnia

   > **Podpowiedź:** Użyj wcześniej utworzonej kolumny "Dzień tygodnia". Możesz również skorzystać z formatowania niestandardowego, aby wyświetlać nazwy dni tygodnia zamiast liczb.

### Część 4: Wizualizacja danych i tworzenie dashboardu (45 minut)

1. **Utworzenie arkusza "Dashboard":**
   - Utwórz nowy arkusz o nazwie "Dashboard"
   - Nadaj mu atrakcyjny i profesjonalny wygląd (zastosuj kolory firmowe, dodaj logo itp.)

2. **Tworzenie kluczowych wykresów:**
   - Wykres kolumnowy pokazujący sprzedaż miesięczną
   - Wykres kołowy pokazujący udział kategorii w całkowitej sprzedaży
   - Wykres słupkowy pokazujący top 5 najlepiej sprzedających się produktów
   - Mapa cieplna (lub tabela z formatowaniem warunkowym) pokazująca sezonowość sprzedaży dla kazdej kategorii

   > **Podpowiedź:** Aby utworzyć wykres, zaznacz odpowiednie dane w tabeli przestawnej i przejdź do zakładki "Wstawianie" > wybierz odpowiedni typ wykresu. Możesz również utworzyć wykres bezpośrednio z tabeli przestawnej, klikając ikonę wykresu w menu narzędzi tabeli przestawnej.

3. **Dodanie interaktywnych elementów:**
   - Dodaj fragmentatory (slicery) umożliwiające filtrowanie danych według:
     - Kategorii produktów
     - Regionów
     - Kwartałów/Miesięcy
   - Dodaj pole kombi (combo box) do wyboru produktu do szczegółowej analizy

   > **Podpowiedź:** Aby dodać fragmentator, zaznacz tabelę przestawną i przejdź do zakładki "Wstawianie" > "Fragmentator". W opcjach fragmentatora możesz dostosować jego wygląd i zachowanie.

4. **Utworzenie panelu KPI (Key Performance Indicators):**
   - Dodaj wskaźniki liczbowe pokazujące:
     - Całkowitą sprzedaż
     - Liczbę transakcji
     - Średnią wartość zamówienia
     - Dynamikę rok do roku (symulowana - porównanie drugiej połowy roku do pierwszej)

   > **Podpowiedź:** Możesz użyć kształtów i pól tekstowych, aby utworzyć efektowne wskaźniki KPI. Wartości możesz pobierać z tabel przestawnych za pomocą funkcji WEŹDANETABELI lub poprzez bezpośrednie odwołania do komórek.

### Część 5: Prognozowanie i analiza zaawansowana (15 minut)

1. **Utworzenie arkusza "Prognozy":**
   - Utwórz nowy arkusz o nazwie "Prognozy"

2. **Prognozowanie przyszłej sprzedaży:**
   - Zastosuj funkcję REGLINP lub PROGNOZA.LINIOWA lub arkusz prognozy, aby przewidzieć sprzedaż na kolejne 3 miesiące
   - Uwzględnij sezonowość w swojej prognozie (analizując wzorce sezonowe z danych historycznych)

   > **Podpowiedź:** W nowszych wersjach Excela możesz użyć arkusza prognozy (kliknij prawym przyciskiem myszy na wykres sprzedaży miesięcznej i wybierz opcję "Dodaj linię trendu"). W starszych wersjach możesz użyć funkcji REGLINP, a w nowszych PROGNOZA.LINIOWA lub utworzyć własny model prognostyczny z uwzględnieniem sezonowości.

3. **Analiza "Co jeśli":**
   - Utwórz prosty model pozwalający symulować wpływ zmian cen na sprzedaż

   > **Podpowiedź:** Możesz utworzyć formuły, które będą reagować na zmiany parametrów wprowadzanych przez użytkownika.


## Kryteria oceny

Zadanie będzie oceniane według następujących kryteriów:

1. **Poprawność wykonania (35%)**
   - Prawidłowe wykonanie wszystkich zadań
   - Poprawność formuł i obliczeń
   - Brak błędów w analizie

2. **Funkcjonalność i użyteczność (25%)**
   - Łatwość nawigacji po skoroszycie
   - Intuicyjność dashboardu
   - Praktyczna wartość analiz i rekomendacji

3. **Analiza rentowności (20%)**
   - Poprawność obliczeń rentowności
   - Dokładność alokacji kosztów
   - Jakość modelu optymalizacyjnego

4. **Estetyka i przejrzystość (10%)**
   - Profesjonalny wygląd skoroszytu
   - Czytelność wykresów i tabel
   - Spójność wizualna

5. **Innowacyjność i kreatywność (10%)**
   - Dodatkowe analizy wykraczające poza podstawowe wymagania
   - Kreatywne podejście do wizualizacji danych
   - Niestandardowe rozwiązania

## Wskazówki końcowe

1. Przed rozpoczęciem pracy zapoznaj się dokładnie ze strukturą danych i relacjami między plikami.
2. Planuj swoją pracę zgodnie z podanymi czasami realizacji poszczególnych części.
3. Regularnie zapisuj plik, aby uniknąć utraty danych.
4. Jeśli nie wiesz jak wykonać jakieś zadanie, poszukaj pomocy w systemie pomocy Excela lub zapytaj prowadzącego.
5. Pamiętaj o dokumentowaniu swojej pracy - dodawaj nazwy do zakresów, opisuj wykresy i tabele.
6. W części dotyczącej rentowności zwróć szczególną uwagę na poprawność obliczeń i logikę alokacji kosztów.

Powodzenia!