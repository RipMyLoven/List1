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
nimed=[]
for i in range(5):
    nimi=input("Sisestage nimi: ").capitalize()
    nimed.append(nimi)

print("Loetelu oli: ", nimed)
nimed.sort()
print("Loetelu sorteeritud: ", nimed)
for n in range(len(nimed)):
    print(n+1,".",nimed[n],sep=" ")

print("Viimasena oli lisatud: ", nimed[-1])

nimekogum = []
for i in range(5):
    nimi = input("Sisestage nimi: ").capitalize()
    nimekogum.append(nimi)

nimekogum.sort()
print("Nimed tähestikulises järjekorras:", nimekogum)
viimane_lisatud = nimekogum[-1]
print("Viimati lisatud nimi:", viimane_lisatud)

opilased = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati']
unikaalsed_opilased = []

for nimi in opilased:
    if nimi not in unikaalsed_opilased:
        unikaalsed_opilased.append(nimi)

print("Unikaalsed nimed:", unikaalsed_opilased)

vanused = [25, 30, 35, 40, 45]
min_vanus = min(vanused)
max_vanus = max(vanused)
summa = sum(vanused)
keskmine = summa / len(vanused)

print("Vähim vanus:", min_vanus)
print("Suurim vanus:", max_vanus)
print("Vanuste kogusumma:", summa)
print("Vanuste keskmine:", keskmine)

