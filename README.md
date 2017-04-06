#Warcaby
![Screen](https://www.dropbox.com/s/0hzqe72gg7ifbob/Warcaby.PNG?raw=1)

##1. Ogólny opis programu.
Program jest komputerową adaptacją popularnej gry planszowej "Warcaby" [[Wikipedia](https://pl.wikipedia.org/wiki/Warcaby#Zasady_gry)] w języku Python. Każdy z graczy musi wykonać ruch przesuwając swój pionek diagonalnie lub jeśli ma taką możliwość, bijąc pionek przeciwnika przeskaując go. Po tym zaczyna się ruch przeciwnika. Gra kończy się w momencie w którym jeden z graczy nie może już wykonać żadnego ruchu, zwycięzcą zostaje gracz z większą ilością pionków na planszy.
Program implementuje sztuczną inteligencje korzystając z algorytmu minmax oraz używa modułu pygame w celu obsługi grafiki oraz urządzeń wejścia.
##2. Uruchomienie programu
Program napisany jest w języku python2.7 wymaga więc działającego interpretatora tego języka. Aby uruchomić program należy uruchomić w interpretatorze plik Main.py, program do pracy wymaga też modułu [pygame](http://pygame.org/)
##3. Opis działania algorytmu AI
funkcji ai(lista_bialych, lista_czarnych) oblicza wszystkie możliwe ruchy czarnego gracza dla podanej listy pionkó po czym dla każdego możliwego ruchu uruchamia funkcje ruch_rek(lista_bialych, lista_czarnych, color, deep) budującą metodą rekurencyjną drzewo wszelkich możliwych przyszłych układów. Po osiągnięciu odpowiedniej głębokości drzewa algorytm oblicza heurystyczną wartość liścia porównując ilość pionków obu graczy na planszy. Następnie algorytm zaczyna zwracać obliczoną wartość "w górę drzewa"([animacja](https://en.wikipedia.org/wiki/Minimax#/media/File:Plminmax.gif)). Zakładając, że zarówno gracz biały, jak i czarny będą podejmować najlepsze dla nich decyzje funkcja ruch_rek jest w stanie policzyć jaki wynik może przynieś jej przesunięcia pionka na dane pole.
[[Polska Wikipedia](https://pl.wikipedia.org/wiki/Algorytm_min-max)]
[[Angielska Wikipedia](https://en.wikipedia.org/wiki/Minimax)]
