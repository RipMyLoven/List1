#from Mymodul import * #Summa as s

#b=int(input("Sisesta arv2: "))
#summa_3=Summa(3,b,int(input("Komas arv: ")))
#summa_31=Summa(100,100)

#print(summa_3)
#print(summa_31)

from Mymodul import *

tulemus = arithmetic(5, 2, '+')
print("Liitmise tulemus:", tulemus)

tulemus = arithmetic(5, 2, '-')
print("Lahutamise tulemus:", tulemus)

tulemus = arithmetic(5, 2, '*')
print("Korrutamise tulemus:", tulemus)

tulemus = arithmetic(5, 2, '/')
print("Jagamise tulemus:", tulemus)

tulemus = arithmetic(5, 0, '/')
print("Nulliga jagamise tulemus:", tulemus)

tulemus = arithmetic(5, 2, '%')
print("Tundmatu tegevuse tulemus:", tulemus)