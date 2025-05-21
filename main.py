import math as m

retka_matrica = True

def formiraj_talon(retka_matrica):
    retka_matrica = True
    matrica = [(10, 0, 0), (10, 1, 0), (10, 2, 0)]
    return retka_matrica, matrica

def u_retkoj(vrsta, kolona, matrica):
    for i in range(len(matrica)):
        if matrica[i][0] == vrsta and matrica[i][1] == kolona:
            return matrica[i][2]
    return 0

def ispisi_talon(matrica, retka_matrica):
    if retka_matrica:
        for i in range(11):
            print('{:5^} | {:5^} | {:5^}'.format(u_retkoj(i, 0, matrica), u_retkoj(i, 1, matrica), u_retkoj(i, 2, matrica)))
            if i == 5:
                sume = [0, 0, 0]
                for i in range(3):
                    for j in range(6):
                        sume[i] += u_retkoj(j, i, matrica)
                print('{:5^} | {:5^} | {:5^}'.format(sume[0], sume[1], sume[2]))
    else:
        for i in range(11):
            print('{:5^} | {:5^} | {:5^}'.format(matrica[i][0], matrica[i][1], matrica[i][2]))
            if i == 5:
                sume = [0, 0, 0]
                for i in range(3):
                    for j in range(6):
                        sume[i] += matrica[i][j]
                print('{:5} | {:5} | {:5}'.format(sume[0], sume[1], sume[2]))
    print('')

def transformisi_matricu(matrica_retka):
    matrica_normalna = []
    for i in range(11):
        matrica_normalna.append([0 for i in range(3)])
    for i in range(len(matrica_retka)):
        vrsta = matrica_retka[i][0]
        kolona = matrica_retka[i][1]
        vrednost = matrica_retka[i][2]
        matrica_normalna[vrsta][kolona] = vrednost
    return matrica_normalna, False

def popuni_polje(vrsta, kolona, vrednost, matrica, retka_matrica):
    if retka_matrica:
        if vrsta == 10:
            matrica[-3+kolona] = (vrsta, kolona, matrica[-3+kolona][2] + vrednost)
            return matrica, retka_matrica
        matrica.append((vrsta, kolona, vrednost))
        if len(matrica) == 11:
            return transformisi_matricu(matrica)
        matrica = sorted(matrica, key = lambda a: (a[0], a[1]))
        return matrica, retka_matrica
    else:
        if vrsta == 10:
            matrica[vrsta][kolona] += vrednost
            return matrica, retka_matrica
        matrica[vrsta][kolona] = vrednost
        return matrica, retka_matrica

def lkg(u):
    return 1664525 * u + 1013904223

def random(u):
    u = lkg(u)
    random_number = u%4294967296/4294967296
    random_number =  m.ceil(random_number*6)
    return u, random_number

def baci_kocke(kocke_za_bacanje, kocke, u):
    for kocka in kocke_za_bacanje:
        u, kocke[kocka] = random(u)
    return u

def prazno_polje(matrica, retka_matrica, vrsta, kolona):
    if retka_matrica:
        if u_retkoj(vrsta, kolona, matrica) == 0:
            return True
        return False
    else:
        if matrica[vrsta][kolona] == 0:
            return True
        return False

def prazna_polja(matrica, retka_matrica, kolona):
    prazna_polja = []
    if kolona == 0:
        for i in range(10):
            if prazno_polje(matrica, retka_matrica, i, kolona):
                prazna_polja.append(i)
                break
    elif kolona == 1:
        for i in range(9, -1, -1):
            if prazno_polje(matrica, retka_matrica, i, kolona):
                prazna_polja.append(i)
                break
    else:
        for i in range(10):
            if prazno_polje(matrica, retka_matrica, i, kolona):
                prazna_polja.append(i)
    return prazna_polja

def ispravan_potez(kocke, bacanje, vrsta, kolona):
    if kolona == 2 and bacanje != 1:
        return 0
    izbrojeno = [kocke.count(broj) for broj in set(kocke)]
    if vrsta in range(0, 6):
        vrednost = kocke.count(vrsta+1) * (vrsta+1)
        return vrednost
    elif vrsta == 6:
        if len(set(kocke)) == 5:
            if 2 in kocke and 3 in kocke and 4 in kocke and 5 in kocke:
                return 76 - bacanje*10
    elif vrsta == 7:
        if 3 in izbrojeno and 2 in izbrojeno:
            return 30
    elif vrsta == 8:
        if 4 in izbrojeno:
            return 40
    else:
        if 5 in izbrojeno:
            return 50
    return 0

def pomoc_prijatelja(matrica, retka_matrica, kocke):
    kocke_za_bacanje = [0, 1, 2, 3, 4]
    baci_kocke()

u = 8
kocke = [0, 0, 0, 0, 0]
while True:
    print('1: Stvori prazan talon')
    print('2: Ispisi talon i trenutni broj bodova')
    print('3: Odigraj potez')
    print('4: Pomoc prijatelja')
    print('0: Zavrsi igru\n')
    print('Unesite zeljenu opciju:')
    while True:
        try:
            izbor = int(input())
            if izbor not in range(0, 5):
                raise ValueError
            break
        except ValueError:
            print('Uneta vrednost mora biti broj od 0 do 4!')
    if izbor == 0:
        print('Hvala Vam sto ste igrali nasu igru! <3')
        exit(0)
    elif izbor == 1:
        retka_matrica, matrica = formiraj_talon(retka_matrica)
    elif izbor == 2:
        ispisi_talon(matrica, retka_matrica)
    elif izbor == 3:
        kocke_za_bacanje = [0,1,2,3,4]
        bacanje = 1
        while True:
            u = baci_kocke(kocke_za_bacanje, kocke, u)
            print('Dobili ste sledece vrednosti na kockama: ')
            print(*kocke)
            if bacanje == 3:
                break
            print('\nUnesite brojeve kocki koje zelite da sacuvate:')
            while True:
                try:
                    izbor = set([int(broj)-1 for broj in input().split()])
                    for broj in izbor:
                        if broj not in range(0, 5):
                            raise ValueError
                    break
                except ValueError:
                    print('Unete vrednosti moraju biti brojevi izmedju 1 i 6!')
            if len(izbor) == 5:
                break
            else:
                bacanje += 1
                kocke_za_bacanje = [i for i in [0,1,2,3,4] if i not in izbor]
        while True:
            print('\nOdaberite kolonu koju zelite da popunite!')
            print('1: Na dole')
            print('2: Na gore')
            print('3: Rucna')
            while True:
                try:
                    kolona = int(input()) - 1
                    if kolona not in range(0, 3):
                        raise ValueError
                    break
                except ValueError:
                    print('Uneta vrednost mora biti broj od 1 do 3!')
            mogucnosti = prazna_polja(matrica, retka_matrica, kolona)
            print('\nOdaberite vrstu koju zelite da popunite!')
            brojac = 1
            if 0 in mogucnosti:
                print(str(brojac)+': Jedinice')
                brojac += 1
            if 1 in mogucnosti:
                print(str(brojac)+': Dvojke')
                brojac += 1
            if 2 in mogucnosti:
                print(str(brojac)+': Trojke')
                brojac += 1
            if 3 in mogucnosti:
                print(str(brojac)+': Cetvorke')
                brojac += 1
            if 4 in mogucnosti:
                print(str(brojac)+': Petice')
                brojac += 1
            if 5 in mogucnosti:
                print(str(brojac)+': Sestice')
                brojac += 1
            if 6 in mogucnosti:
                print(str(brojac)+': Kenta')
                brojac += 1
            if 7 in mogucnosti:
                print(str(brojac)+': Ful')
                brojac += 1
            if 8 in mogucnosti:
                print(str(brojac)+': Poker')
                brojac += 1
            if 9 in mogucnosti:
                print(str(brojac)+': Jamb')
            while True:
                try:
                    izbor = int(input()) - 1
                    if izbor not in range(0, brojac):
                        raise ValueError
                    vrsta = mogucnosti[izbor]
                    break
                except ValueError:
                    print('Uneta vrednost mora biti broj od 1 do 10!')
            vrednost = ispravan_potez(kocke, bacanje, vrsta, kolona)
            if vrednost != 0:
                matrica, retka_matrica = popuni_polje(vrsta, kolona, vrednost, matrica, retka_matrica)
                matrica, retka_matrica = popuni_polje(10, kolona, vrednost, matrica, retka_matrica)
                break
            else:
                while True:
                    print('Uslovi za popunjavanje nisu ispunjeni!')
                    print('Ovo polje ce biti precrtano')
                    print('Jeste li sigurni da zelite da nastavite?')
                    komanda = input()
                    if komanda == 'da':
                        popuni_polje(vrsta, kolona, 'X', matrica, retka_matrica)
                        break
                    elif komanda == 'ne':
                        break
                if komanda == 'da':
                    break