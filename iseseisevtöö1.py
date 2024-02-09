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
