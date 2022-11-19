#Adott egy lista, mely október havi napi középhőmérséklet értékeket tartalmazza. homerseklet= [0,12,13,9,2,7].

#Az első érték október 1.  A program írja ki, melyik napon csökkent az előző naphoz képest  a hőmérséklet több, mint 3 fokot?

def homerseklet():
    okt = [0, 12, 13, 9, 2, 7]
    i = 1
    while i < len(okt):
        if okt[i-1] - okt[i] > 3:
            print(f"{i+1} napra")
        i += 1

def homerseklet2():
    okt = [0, 12, 13, 9, 2, 7]
    i = 0
    while i < len(okt) - 1:
        if (okt[i] - okt[i+1] > 3):
            print(f" {i+2}. napra")
            #elágazás vége
        i += 1
            #ciklus vége

#Kérj be a felhasználótól egy szöveget.  Alakítsd nagybetűssé!
def nagybetu():
    x = input("adj meg egy szöveget")
    szoveg = x.upper()
    print(szoveg)
    hosszabb(szoveg) #meghívjuk a hosszabba a szoveget, így már a main-be nem kell beimportálni

#Az előző szövegről döntsd el, hogy 10 karakternél hosszabb-e? Ha igen, akkor írd ki a hosszát!
def hosszabb(szoveg):
    if len(szoveg) > 10:
        print(f"A szöveg hossza: {len(szoveg)}")
    else:
        print("A szöveg hossza rövidebb, mint 10 karakter")

#Kérj be egy legalább 3 betűs szót a felhasználótól. A szavakat addig kérd be, amíg a hossza legalább 3!
def harom():
    x = input("adj meg egy szöveget")
    while len(x) <= 3:
        x = input("három betűst")
    print("na végre sikerült")

#Kérj be a felhasználótól egy szöveget. Keresd meg benne az első "a" betűt.
def elsoa():
    szoveg = input("adj meg egy szöveget")
    i = 0
    while i < len(szoveg) and szoveg[i].upper() != 'A':
        i +=1
    if i < len(szoveg):
        print(f"van a betű a szövegben {i+1}. karekteren")
    else:
         print("nincs a betű a szövegben")

#Hány "a" betű van a bekért szövegben?
def mennyi():
