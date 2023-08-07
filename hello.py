print("Hello World")
print("Hello World")
x=10
print(x)

y=5
a=x+y
b=x-y
c=x*y
e=x/y
f=x%y
g=x**y
print(a,b,c,e,f,g)
# ez egy comment
# nev=input("Add meg a neved: ")
# print("Hello," + nev + "!")
szam=int(input("Adj meg egy szamot: "))
paros = szam%2==0
if paros==True:
    print("A szam paros")
else:
    print("A szam paratlan")

for i in range(5):
    print(i)