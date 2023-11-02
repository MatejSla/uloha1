cislo = int(input("Zadaj číslo: "))
pocet_cifier = 0
originalne_cislo = cislo

# Zistíme počet cifier v čísle
while cislo > 0:
    cislo //= 10
    pocet_cifier += 1

cislo = originalne_cislo

if pocet_cifier % 2 == 1:
    # Nepárny počet cifier, vrátime strednú cifru
    for _ in range(pocet_cifier // 2):
        cislo //= 10
    stredna_cifra = cislo % 10
    print(f"Stredná cifra: {stredna_cifra}")
else:
    # Párny počet cifier, vrátime priemer dvoch stredných cifier
    for _ in range(pocet_cifier // 2 - 1):
        cislo //= 10
    stredna1 = cislo % 10
    cislo //= 10
    stredna2 = cislo % 10
    priemer = (stredna1 + stredna2) / 2
    print(f"Priemer dvoch stredných cifier: {priemer}")
