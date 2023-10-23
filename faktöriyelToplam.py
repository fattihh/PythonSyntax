carpım = 1

for i in range(1,101):
    carpım *= i

print(carpım)#100 faktöriyel sayısı

liste = []
for i in str(carpım):
    liste.append(i)

toplam = 0

integer_liste = [int(x) for x in liste]

for i in integer_liste:
    toplam +=i

print(toplam)

