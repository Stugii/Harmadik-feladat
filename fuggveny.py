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