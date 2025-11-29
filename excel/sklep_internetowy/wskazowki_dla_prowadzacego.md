# Wskazówki dla prowadzącego: Analiza sprzedaży sklepu internetowego

## Informacje ogólne

Ten dokument zawiera wskazówki dla prowadzącego zajęcia, dotyczące zadania "Analiza sprzedaży sklepu internetowego". Znajdziesz tu:
- Opis danych wejściowych
- Spodziewane wyniki dla każdej części zadania
- Typowe problemy i błędy studentów
- Propozycje oceny zadania

## Opis danych

Plik `sprzedaz.csv` zawiera dane transakcyjne sklepu internetowego z roku 2024. Dane obejmują:
- Ponad 10000 transakcji
- 6 kategorii produktów (Elektronika, Odzież, Artykuły sportowe, Książki, Dom i ogród, Zabawki)
- 5 regionów (Północny, Południowy, Wschodni, Zachodni, Centralny)
- Pełne informacje o cenach, ilościach, wartościach zamówień

Dane zostały wygenerowane z uwzględnieniem sezonowości dla poszczególnych kategorii produktów, co powinno być widoczne w analizach studentów.

## Spodziewane wyniki i wskazówki dotyczące poszczególnych części zadania

### Część 1: Import i przygotowanie danych

**Poprawnie wykonane zadanie powinno zawierać:**
- Prawidłowo zaimportowane dane z zachowaniem struktury i typów danych
- Tabelę z formatowaniem walutowym dla kolumn cenowych
- Dodatkowe kolumny: Miesiąc, Kwartał, Dzień tygodnia z poprawnymi formułami

**Typowe błędy:**
- Nieprawidłowy import danych (np. problem z separatorami)
- Brak formatowania walutowego
- Błędy w formułach dla kolumn pomocniczych, szczególnie dla kolumny Kwartał

**Wskazówki dla prowadzącego:**
- Sprawdź formułę dla kolumny Kwartał - powinna być `=ZAOKR.W.GÓRĘ([@Miesiąc]/3;0)`
- Sprawdź, czy studenci nie pominęli formatowania danych jako tabeli (jest to kluczowe dla późniejszych odniesień)

### Część 2: Analiza podstawowa

**Poprawnie wykonane zadanie powinno zawierać:**
- Arkusz "Analiza_Podstawowa" z poprawnymi obliczeniami wskaźników
- Tabele przestawne pokazujące:
  - Wartość sprzedaży według kategorii (ok. 12,9 mln zł całkowitej sprzedaży)
  - Elektronika powinna mieć najwyższą wartość sprzedaży (ok. 4,2-4,4 mln zł)
  - Książki najniższą wartość sprzedaży (ok. 1,1-1,2 mln zł)
- Analiza regionalna powinna pokazywać dość równomierny rozkład między regionami

**Typowe błędy:**
- Nieprawidłowe tworzenie tabel przestawnych
- Pominięcie analizy udziału procentowego
- Błędy w obliczeniach (sumy, średnie, itp.)

**Wskazówki dla prowadzącego:**
- Sprawdź, czy studenci poprawnie zastosowali funkcje agregujące w tabelach przestawnych
- Zwróć uwagę na formatowanie procentowe przy analizie udziałów

### Część 3: Analiza czasowa i sezonowość

**Poprawnie wykonane zadanie powinno zawierać:**
- Arkusz "Analiza_Czasowa" z odpowiednimi tabelami przestawnymi
- Wyraźne wzorce sezonowe:
  - Elektronika - szczyt sprzedaży w listopadzie i grudniu
  - Dom i ogród - szczyt sprzedaży w maju i czerwcu
  - Zabawki - wyraźny szczyt w grudniu
- Prawidłową analizę dni tygodnia (nie powinno być dużych różnic)

**Typowe błędy:**
- Niepoprawne obliczenie dynamiki miesiąc do miesiąca
- Pominięcie formatowania warunkowego dla podkreślenia sezonowości
- Błędna interpretacja wzorców sezonowych

**Wskazówki dla prowadzącego:**
- Sprawdź, czy studenci zauważyli i prawidłowo zinterpretowali wzorce sezonowe
- Zwróć uwagę na zastosowanie formatowania warunkowego
- Miesiąc z najwyższą sprzedażą to grudzień (ok. 1,56 mln zł), a z najniższą - luty (ok. 0,72 mln zł)

### Część 4: Wizualizacja danych i tworzenie dashboardu

**Poprawnie wykonane zadanie powinno zawierać:**
- Arkusz "Dashboard" z profesjonalnie wyglądającym interfejsem
- Co najmniej 4 różne typy wykresów
- Interaktywne elementy (fragmentatory lub inne filtry)
- Panel KPI z kluczowymi wskaźnikami

**Typowe błędy:**
- Nieczytelne lub źle dobrane wykresy
- Brak lub nieprawidłowe działanie elementów interaktywnych
- Chaotyczny układ dashboardu
- Niewystarczająca liczba wskaźników KPI

**Wskazówki dla prowadzącego:**
- Oceniaj zarówno funkcjonalność, jak i estetykę dashboardu
- Sprawdź, czy wykresy są odpowiednio opisane (tytuły, etykiety osi, legendy)
- Przetestuj działanie fragmentatorów - powinny filtrować wszystkie powiązane tabele przestawne i wykresy

### Część 5: Prognozowanie i analiza zaawansowana

**Poprawnie wykonane zadanie powinno zawierać:**
- Arkusz "Prognozy" z modelami prognozowania
- Uwzględnienie sezonowości w prognozach
- Prosty model "Co jeśli" z możliwością symulacji

**Typowe błędy:**
- Nieuwzględnienie sezonowości w prognozach
- Zbyt uproszczone podejście do modelowania
- Brak elementów interaktywnych w analizie "Co jeśli"

**Wskazówki dla prowadzącego:**
- Ta część jest najtrudniejsza i studenci mogą mieć z nią problemy
- Zwróć szczególną uwagę na kreatywność podejścia
- Prognoza na kolejne 3 miesiące powinna wykazywać podobne trendy sezonowe jak analogiczne miesiące z danych historycznych

## Skala ocen

Proponowana skala ocen (maksymalna liczba punktów: 100):

- 91-100 punktów: Bardzo dobry (5.0)
- 81-90 punktów: Dobry plus (4.5)
- 71-80 punktów: Dobry (4.0)
- 61-70 punktów: Dostateczny plus (3.5)
- 51-60 punktów: Dostateczny (3.0)
- 0-50 punktów: Niedostateczny (2.0)

## Podział punktów:

1. **Część 1: Import i przygotowanie danych** - 15 punktów
   - Poprawny import danych - 5 pkt
   - Odpowiednie formatowanie - 5 pkt
   - Dodatkowe kolumny - 5 pkt

2. **Część 2: Analiza podstawowa** - 20 punktów
   - Poprawne wskaźniki sprzedaży - 5 pkt
   - Analiza kategorii produktów - 7 pkt
   - Analiza regionalna - 8 pkt

3. **Część 3: Analiza czasowa i sezonowość** - 25 punktów
   - Sprzedaż miesięczna - 8 pkt
   - Analiza sezonowości - 10 pkt
   - Analiza dni tygodnia - 7 pkt

4. **Część 4: Wizualizacja danych i dashboard** - 25 punktów
   - Układ i estetyka dashboardu - 7 pkt
   - Wykresy - 8 pkt
   - Elementy interaktywne - 5 pkt
   - Panel KPI - 5 pkt

5. **Część 5: Prognozowanie i analiza zaawansowana** - 15 punktów
   - Prognozy sprzedaży - 8 pkt
   - Analiza "Co jeśli" - 7 pkt

## Uwagi końcowe

- W ocenie uwzględnij zarówno poprawność merytoryczną, jak i estetykę wykonania.
- Doceniaj kreatywne podejścia i rozwiązania wykraczające poza podstawowe wymagania.
- Zwracaj uwagę na praktyczną użyteczność stworzonych analiz i dashboardów.
- Pamiętaj, że niektórzy studenci mogą używać różnych wersji Excela, co może wpływać na dostępność pewnych funkcji.
