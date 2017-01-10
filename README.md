#Warcaby
![Screen](https://www.dropbox.com/s/0hzqe72gg7ifbob/Warcaby.PNG?raw=1)

##1. Ogólny opis programu.
Program jest komputerową adaptacją popularnej gry planszowej "Warcaby" [[Wikipedia](https://pl.wikipedia.org/wiki/Warcaby#Zasady_gry)] w języku Python. Program implementuje uproszczone zasady warcab. Każdy z graczy musi wykonać ruch przesuwając swój pionek diagonalnie lub jeśli ma taką możliwość, bijąc pionek przeciwnika przeskaując go. Po tym zaczyna się ruch przeciwnika. Gra kończy się w momencie w którym jeden z graczy nie może już wykonać żadnego ruchu, zwycięzcą zostaje gracz z większą ilością pionków na planszy.
Program implementuje sztuczną inteligencje korzystając z algorytmu minmax oraz używa modułu pygame w celu obsługi grafiki oraz urządzeń wejścia.
##2. Uruchomienie programu
Program napisany jest w języku python2.7 wymaga więc działającego interpretatora tego języka. Aby uruchomić program należy uruchomić w interpretatorze plik Main.py, program do pracy wymaga też modułu [pygame](http://pygame.org/)
##3. Ogólny opis zawartości plików
- Main.py - główny plik zawiera główną funkcję programu "main()", inicjalizuje bibliotekę pygame, ładuje tło gry(tlo.png) po czym inicjalizuje "glowna_rozgrywka" obiekt klasy "Rozgrywka" odpowiedzialny za wszelkie operacje rozgrywające się na planszy. Główna pętla while przekazuje obiektowi glowna_rogrywka informacje o kursorze.

- rozgrywka.py - zawiera definicję klasy Rozgrywka, która jest obiektem obsługująca całą zawartość planszy. Główną metodą klasy Rozgrywka jest metoda on_click wywoływana przez z pliku Main.py przy każdym kliknięciu planszy lub podniesieniu klikniętego przycisku gdziekolwiek. Do on_click przekazywana są koordynaty kliknięcia.

- pionek.py - zawiera definicję klasy Pionek. Klasa ta odwzorowuje każdy pionek na planszy, dziedziczy on z klasy Sprite z moduły pygame.
- ruch.py - zawiera funkcje ruch zwracającą możliwe ruchy dla podanego pionka na danej planszy. Wartości są zwracane w formacie słownika.
dict[docelowy_cord] = zbity_pion
jeśli dla danego ruchu nie ma możliwości bicia zbity_pion przyjmuje wartość 0

- oznaczenie.py - zawiera definicje klasy Oznaczenie. Klasa ta odwzorowuje każde oznaczenie podświetlające pola na których można odłożyć podniesiony pionek.

- AI.py - zawiera realizację algorytmu minMax dla warcab.
funkcji ai(lista_bialych, lista_czarnych) oblicza wszystkie możliwe ruchy czarnego gracza dla podanej listy pionkó po czym dla każdego możliwego ruchu uruchamia funkcje ruch_rek(lista_bialych, lista_czarnych, color, deep) budującą metodą rekurencyjną drzewo wszelkich możliwych ruchów którego kolejne pokolenia reprezentują na przemian ruchy białego i czarnego gracza. Po osiągnięciu odpowiedniej głębokości drzewa algorytm oblicza heurystyczną wartość liścia porównując ilość pionków obu graczy na planszy. Następnie algorytm zaczyna zwracać obliczoną wartość "w górę drzewa"([animacja](https://en.wikipedia.org/wiki/Minimax#/media/File:Plminmax.gif)). Zakładając, że zarówno gracz biały, jak i czarny będą podejmować najlepsze dla nich decyzje funkcja ruch_rek jest w stanie policzyć jaki wynik może przynieś jej przesunięcia pionka na dane pole.
[[Polska Wikipedia](https://pl.wikipedia.org/wiki/Algorytm_min-max)]
[[Angielska Wikipedia](https://en.wikipedia.org/wiki/Minimax)]

- tools.py - zawiera zbiór narzędzi pomocniczych niepowiązanych ściśle z żadną konkretną częścią programu lub względem siebie.
