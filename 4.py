def zagniezdz(lista):
    zagniezdzone = []
    for liczba in lista:
        zagniezdzenie = liczba
        for _ in range(liczba - 1):
            zagniezdzenie = [zagniezdzenie]
        zagniezdzone.append([zagniezdzenie])  # Dodajemy dodatkowy poziom zagnieżdżenia
    return zagniezdzone

# Testowanie:
wejscie = [1, 1, 3, 2]
wynik = zagniezdz(wejscie)
print("Wejściowa lista:", wejscie)
print("Zagnieżdżona lista:", wynik)
