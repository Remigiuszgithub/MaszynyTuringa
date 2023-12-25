class MaszynaTuringa:
    def __init__(self):
        self.tasma = []
        self.glowica = 0
        self.stan = 'q0'

    def wczytaj_tasme(self, tekst):
        self.tasma = list(tekst)

    def krok(self):
        symbol = self.tasma[self.glowica] if self.glowica < len(self.tasma) else ' '
        if self.stan == 'q0':
            if symbol == 'A':
                self.tasma[self.glowica] = 'C'
                self.glowica += 1
            elif symbol in 'BCD':
                self.glowica += 1
            elif symbol == ' ':
                self.stan = 'qf'

    def uruchom(self):
        while self.stan != 'qf':
            self.krok()

    def pobierz_wynik(self):
        return ''.join(self.tasma)

maszyna = MaszynaTuringa()

# Użytkownik podaje tekst
tekst = input("Podaj tekst z literami A, B, C i D: ")

maszyna.wczytaj_tasme(tekst)
maszyna.uruchom()
nowy_tekst = maszyna.pobierz_wynik()

print(f"Tekst przed zamianą: {tekst}")
print(f"Tekst po zamianie liter A na C: {nowy_tekst}")
