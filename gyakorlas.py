nev=input("Add meg a neved: ")
print("Udvozollek " + nev + "!")

szam=int(input("Adj meg egy szamot: "))
paros = szam%2==0
if paros==True:
    print("Ez a szam paros!")
else:
    print("Ez a szam paratlan!")

x=int(input("Add meg az x erteket: "))
y=int(input("Add meg az y erteket: "))
a=(x+y)
b=(x-y)
c=(x*y)
d=(x/y)
e=(x%y)
f=(x**y)
print(a,b,c,d,e,f)

r=int(input("Add meg a kor sugarat: "))
g=(r*r*3.14)
h=(2*r*3.14)
print(g,h)

a=int(input("Add meg az elso szamot: "))
b=int(input("Add meg a masodik szamot: "))
c=int(input("Add meg a harmadik szamot: "))
d=int(input("Add meg a negyedik szamot: "))
x=(a+b+c+d)
print(x)

import math
a=int(input("Ird be a haromszog egyik befogojat: "))
b=int(input("Ird be a haromszog masik befogojat: "))
x=((a*a)+(b*b))
math.sqrt(x)
print(math.sqrt(x))

a=int(input("Irj be egy pozitiv egesz szamot: "))
for a in range(1, a + 1):
        print(a)

print("gyakorolj, mert megbuksz!")