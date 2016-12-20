#Warcaby
![Screen](https://www.dropbox.com/s/0hzqe72gg7ifbob/Warcaby.PNG?raw=1)

##1. Ogólny opis programu.
Program jest komputerową adaptacją popularnej gry planszowej "Warcaby" [[Wikipedia](https://pl.wikipedia.org/wiki/Warcaby#Zasady_gry)] w języku python. 
Program implementuje sztuczną inteligencje korzystając z algorytmu minmax oraz używa modułu pygame w celu obsługi grafiki oraz urządzeń wejścia.
##2. Uruchomienie programu
Program napisany jest w języku python2.7 wymaga więc działającego interpretatora tego języka. Aby uruchomić program należy urchomić w interpretatorze plik Main.py, program do pracy wymaga też modułu [pygame](http://pygame.org/)
##3. Ogólny opis zawartości plików
- Main.py - główny plik zawiera główną fukncję programu "main()", inicjalizuje biblitekę pygame, ładuje tło gry(tlo.png) po czym inicjalizuje "glowna_rozgrywka" obiekt klasy "Rozgrywka" odpowiedzialny za wszelkie operacje rozgrywające się na planszy. Główna pętla while przekazuje obiektowi glowna_rogrywka informacje o kursorze

- rozgrywka.py - zawiera definicję klasy Rozgrywka która jest obiektem obsługująca całą zawartość planszy. Główną metodą klasy Rozgrywka jest metoda on_click wywoływana przez z pliku Main.py przy każdym kliknięciu planszy lub podniesieniu klikniętego przycisku gdziekolwiek. Do on_click przekazywana są koordynaty kliknięcia.

- pionek.py - zawiera definicję klasy Pionek. Klasa ta odwzorowuje każdy pionek na planszy, dziedziczy on z klasy Sprite z moduły pygame
- ruch.py - zawiera funkcje ruch zwracającą możliwe ruchy dla podanego pionka na danej planszy. Wartości są zwracane w formacie słownika
dict[docelowy_cord] = zbity_pion
jeśli dla danego ruchu nie ma możliwości bicia zbity_pion przyjmuje wartość 0

- oznaczenie.py - zawiera definicje klasy Oznaczenie.  Klasa ta odwzorowuje każde oznaczenie podświetlające pola na których można odłożyć podniesiony pionek.

- AI.py - zawiera realizację algorytmu minMax dla warcab
  [[Polska Wikipedia](https://pl.wikipedia.org/wiki/Algorytm_min-max)]
  [[Angielska Wikipedia](https://en.wikipedia.org/wiki/Minimax)]

- tools.py - zawiera zbiór narzędzi pomocniczych nie powiązanych ściśle z żadną konkretną częścią programu lub względem siebie.
