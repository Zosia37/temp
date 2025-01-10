class Zwierze:
    def __init__(self, nazwa, srodowisko, waga):
        self.nazwa = nazwa
        self.srodowisko = srodowisko
        self.waga = waga

    def __str__(self):
        return self.nazwa

    def opis(self):
        return f"to jest {self.nazwa}, zyje w {self.srodowisko}, wazy okolo {self.waga} kg."

class Ssak(Zwierze): 
    def __init__(self, nazwa, srodowisko, waga, gatunek):
        super().__init__(nazwa, srodowisko, waga)
        self.gatunek = gatunek

    def szczegoly_gatunku(self):
        return f"{self.nazwa} to ssak z gatunku {self.gatunek}."

t = Ssak("Slon", "sawanna", 6000, "Loxodonta africana")
print(t)  # Slon
print(t.opis())  # to jest Slon, zyje w sawanna, wazy okolo 6000 kg.
print(t.szczegoly_gatunku())  # Slon to ssak z gatunku Loxodonta africana.
