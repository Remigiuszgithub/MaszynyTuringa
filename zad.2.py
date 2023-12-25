class MaszynaTuringa:
    def __init__(self, tabela_przejsc):
        self.tabela_przejsc = tabela_przejsc
        self.stan = 'q0'
        self.pozycja_glowicy = 0
        self.taśma = []

    def wczytaj_tasme(self, wejsciowe_slowo):
        self.taśma = list(wejsciowe_slowo + 'B')  # Dodajemy pole B na końcu taśmy

    def uruchom(self):
        while self.stan != 'qf':
            symbol = self.taśma[self.pozycja_glowicy]

            if (self.stan, symbol) in self.tabela_przejsc:
                nowy_stan, nowy_symbol, kierunek = self.tabela_przejsc[(self.stan, symbol)]

                self.taśma[self.pozycja_glowicy] = nowy_symbol

                if kierunek == 'R':
                    self.pozycja_glowicy += 1
                elif kierunek == 'L':
                    self.pozycja_glowicy -= 1

                self.stan = nowy_stan
            else:
                break

        # Obliczenie ilości "1" w słowie
        ilosc_jedynek = self.taśma.count('1')
        return ilosc_jedynek

# Przykład użycia:
tabela_przejsc = {
    ('q0', '1'): ('q0', '1', 'R'),
    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', 'B'): ('qf', 'B', 'S'),  # Zakończenie obliczeń
}

maszyna = MaszynaTuringa(tabela_przejsc)

wejsciowe_slowo = input("Podaj słowo binarne: ")
maszyna.wczytaj_tasme(wejsciowe_slowo)
ilosc_jedynek = maszyna.uruchom()

print(f"Ilość wystąpień '1' w słowie: {ilosc_jedynek}")
