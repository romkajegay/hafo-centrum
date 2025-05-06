def vytvor_utulek():
    return {}

# 2. Přidání zvířete do útulku
def pridej_zvire(utulek, jmeno, druh, vek):
    utulek[jmeno] = {"druh": druh, "vek": vek}

# 3. Výpis všech zvířat
def vypis_zvirata(utulek):
    for jmeno, info in utulek.items():
        print(f"{jmeno} je {info['druh']} a je jí/mu {info['vek']} let.")

# 4. Výpis podle druhu
def vypis_podle_druhu(utulek, druh):
    for jmeno, info in utulek.items():
        if info["druh"] == druh:
            print(f"{jmeno} je {info['druh']} a je jí/mu {info['vek']} let.")

# 5. Přidání zvířete přes vstup uživatele
def pridej_zvire_od_uzivatele(utulek):
    jmeno = input("Zadej jméno zvířete: ")
    druh = input("Zadej druh zvířete: ")
    vek = int(input("Zadej věk zvířete: "))
    pridej_zvire(utulek, jmeno, druh, vek)
    print(f"Přidal jsi {jmeno}, je to {druh} a je mu/jí {vek} let.")

utulek = vytvor_utulek()
pridej_zvire(utulek, "romka", "činčila", 3)
pridej_zvire(utulek, "eliška", "fretka", 5)
pridej_zvire(utulek, "stepan", "kocour", 7)
pridej_zvire(utulek, "kiki", "myška", 2)
pridej_zvire(utulek, "tonda", "tygr", 6)
pridej_zvire(utulek, "vítek", "kocour", 6)

pridej_zvire_od_uzivatele(utulek)

print("\nVšechna zvířata v útulku:")
vypis_zvirata(utulek)