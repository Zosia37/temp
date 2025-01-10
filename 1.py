import re

def znajdz_lata_i_roznice(sciezka_do_pliku):
    with open(sciezka_do_pliku, 'r') as plik:
        zawartosc = plik.read()
    
    # Wyłuskanie lat z tekstu
    lata = re.findall(r'\b\d{4}\b', zawartosc)
    lata = [int(rok) for rok in lata]
    
    # Obliczanie różnicy między najstarszym a najnowszym rokiem
    najstarszy = min(lata)
    najnowszy = max(lata)
    roznica = najnowszy - najstarszy
    
    return lata, roznica

# Użycie:
sciezka = "dane.txt"
lista_lat, roznica_lat = znajdz_lata_i_roznice(sciezka)
print("Lata znalezione w pliku:", lista_lat)
print("Różnica między najstarszym a najnowszym wydarzeniem:", roznica_lat)
