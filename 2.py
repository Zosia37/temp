import re

def zamiana_ag_na_ga(sekwencja):
    # Dopasowanie adeniny z guaniną i zamiana miejsc z użyciem funkcji zamiany
    def zamien(match):
        return match.group(0)[1].lower() + match.group(0)[0].lower()
    
    nowa_sekwencja = re.sub(r'AG|GA', zamien, sekwencja)
    return nowa_sekwencja

# Test:
nukleotydy = "TAGCTAGTATCG"
wynik = zamiana_ag_na_ga(nukleotydy)
print("Oryginalna sekwencja:", nukleotydy)
print("Po zamianie:", wynik)
