def przesun_pierwsza_literke(tekst):
    if not tekst:
        return tekst  # Zwróć pusty tekst, jeśli wejściowy tekst jest pusty.

    tekst_lista = list(tekst)  # Konwertuj tekst na listę znaków.

    pierwsza_literka = tekst_lista[0]  # Zapisz pierwszą literkę.

    for i in range(1, len(tekst_lista)):
        tekst_lista[i - 1] = tekst_lista[i]  # Przesuń każdą literkę o jedno miejsce w lewo.

    tekst_lista[-1] = pierwsza_literka  # Wstaw zapisaną pierwszą literkę na koniec.

    nowy_tekst = ''.join(tekst_lista)  # Połącz listę w nowy tekst.
    return nowy_tekst

# Przykład użycia:
tekst = input("Podaj wyraz zbudowany z liter A, B, C i D: ")
nowy_tekst = przesun_pierwsza_literke(tekst)
print(f"Wyraz przed przesunięciem: {tekst}")
print(f"Wyraz po przesunięciu: {nowy_tekst}")
