numbrid = [10, 20, 30, 40, 50]

if numbrid:
    maksimum = max(numbrid)
    
    if len(numbrid) == 0:
        print("Loend on tühi")
    else:
        kasutu_number = maksimum / len(numbrid)
        
        maksimumi_indeks = numbrid.index(maksimum)
        numbrid[maksimumi_indeks] = kasutu_number
        
        print("Kasutu number:", kasutu_number)
        print("Loend pärast asendamist:", numbrid)
else:
    print("Loend on tühi")
    









from random import *
from string import * 
rida=[]
N=randint(2,25)
for i in range(N):
    rida.append(choice(ascii_uppercase))
print(rida)
kogus=int(input("Mitu elemendi vahetame oma vahel "))
if len(rida)//2>kogus:
    for i in range(kogus):
        a=rida[i]
        rida[i]=rida[len(rida)-i-1]
        rida[len(rida)-1-i]=a
print(rida)












indeksid=["Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve", 
        "Ida-Virumaa, Lääne-Virumaa, Jõgevama", "Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
        , "Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa",
       "Läänemaa, Hiiumaa, Saaremaa"]
while True:
    try:
        indeks=int(input("Sisesta oma indeks: "))
        indeks_elemendide_arv=len(str(indeks))
        if indeks_elemendide_arv==5:
            print("5numbriline indeks")
            break
        else:
            print("On vaj 5numbriline anv(Indeks)")


    except:
        print("Vale andmetüüp! ")
arv1=indeks//10000
print(arv1)
symbolid=list(str(indeks))
print(f"Sa elad piirkonnas {indeksid[int(symbolid[0])-1]}")









#from string import *
#from venv import create
##1
#vokaalid = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü', 'õ']
#konsonandid = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y']
#markid=punctuation
#v=k=m=t=0
#tekst=input("Sisesta sõna või lause: ").lower()
#tekst_list=list(tekst)
#for taht in tekst_list:
#    if taht in vokaalid:
#        v+=1
#    elif taht in konsonandid:
#        k+=1
#    elif taht in markid:
#        m+=1
#    else:
#        t+=1
#print("Vokaalid:", v)
#print("konsonandid:", k)
#print("kirjavähemärgid:", m)
#print("Tühikud:", t)

#2
#nimed=[]
#for i in range(5):
#    nimi=input("Sisestage nimi: ").capitalize()
#    nimed.append(nimi)

#print("Loetelu oli: ", nimed)
#nimed.sort()
#print("Loetelu sorteeritud: ", nimed)
#for n in range(len(nimed)):
#    print(n+1,".",nimed[n],sep=" ")

#print("Viimasena oli lisatud: ", nimed[-1])

#nimekogum = []
#for i in range(5):
#    nimi = input("Sisestage nimi: ").capitalize()
#    nimekogum.append(nimi)

#nimekogum.sort()
#print("Nimed tähestikulises järjekorras:", nimekogum)
#viimane_lisatud = nimekogum[-1]
#print("Viimati lisatud nimi:", viimane_lisatud)

#opilased = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati']
#unikaalsed_opilased = []

#for nimi in opilased:
#    if nimi not in unikaalsed_opilased:
#        unikaalsed_opilased.append(nimi)

#print("Unikaalsed nimed:", unikaalsed_opilased)

#vanused = [25, 30, 35, 40, 45]
#min_vanus = min(vanused)
#max_vanus = max(vanused)
#summa = sum(vanused)
#keskmine = summa / len(vanused)

#print("Vähim vanus:", min_vanus)
#print("Suurim vanus:", max_vanus)
#print("Vanuste kogusumma:", summa)
#print("Vanuste keskmine:", keskmine)




nimed=[]
for i in range(5):
    nimi=input("Sisestage nimi: ").capitalize()
    nimed.append(nimi)

print("Loetelu oli: ", nimed)
nimed.sort()
print("Loetelu sorteeritud: ",nimed)
for n in range(len(nimed)):
    print(n+1,".",nimed[n],sep=" ")

print("Vimasena oli lisatud: ",nimi)

opilased = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati']

nimed = []
for nimi in opilased:
    if nimi not in nimed:
        nimed.append(nimi)

print(nimed)
vanused=[]
for i in range(5):
    vanus=int(input("Sisesta vanus: "))
    vanused.append(vanus)
maksimum=max(vanused)
minimum=min(vanused)
summa=sum(vanused)
keskmine=summa/len(vanused)

print(maksimum, "," , minimum, "," , summa, "," , keskmine)
# kuva ekraanile nimi koos vnusega 

for i in range(5):
    print(nimed[i], "on", vanused[i], "aastad vana")

#3
from random import * 
arvud=[]
N=int(input("Mitu rida joonistame?"))
S=input("Sisestage sümbol mida tahate kasutada: ")
for p in range(N):
    arvud.append(randint(1, 100))
#4
for p in range(N):
    print(arvud[p]*S)

#5
indeks=["Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve", 
        "Ida-Virumaa, Lääne-Virumaa, Jõgevama", "Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
        , "Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa",
       "Läänemaa, Hiiumaa, Saaremaa"]
while True:
    try:
        indeks=int(input("Sisesta oma indeks: "))
        indeks_elemendide_arv=len(str(indeks))
        if indeks_elemendide_arv==5:
            print("5numbriline indeks")
        else:
            print("On vaj 5numbriline anv(Indeks)")

    except:
        print("Vale andmetüüp! ")

