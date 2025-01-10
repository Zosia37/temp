class Pracownik:
    def __init__(self, imie_pracownika, nazwisko_pracownika, srednie_godziny):
        self.imie_pracownika = imie_pracownika
        self.nazwisko_pracownika = nazwisko_pracownika
        self.srednie_godziny = srednie_godziny

    def __str__(self):
        return self.imie_pracownika

    def przedstaw(self):
        return f"Cześć, jestem {self.imie_pracownika} {self.nazwisko_pracownika}."

    def oblicz_godziny(self, liczba_miesiecy):
        return self.srednie_godziny * liczba_miesiecy


class Informatyk(Pracownik):
    def __init__(self, imie, nazwisko, godziny_miesieczne, stawka_godzinowa):
        super().__init__(imie, nazwisko, godziny_miesieczne)
        self.stawka_godzinowa = stawka_godzinowa

    def wynagrodzenie(self):
        return self.srednie_godziny * self.stawka_godzinowa


# Testowanie:
osoba = Informatyk("Dawid", "Bigaj", 200, 50)
print(osoba)  # Dawid
print(osoba.przedstaw())  # Cześć, jestem Dawid Bigaj.
print("Godziny w 2 miesiące:", osoba.oblicz_godziny(2))  # 400
print("Miesięczne wynagrodzenie:", osoba.wynagrodzenie())  # 10000
