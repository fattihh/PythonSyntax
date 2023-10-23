liste = []
for i in range(100,999):
    for j in range(100,999):
        palindrom=i*j
        if str(palindrom)[0]==str(palindrom)[-1] and str(palindrom)[1] == str(palindrom)[-2] and str(palindrom)[2] == str(palindrom)[-3] :
            liste.append(palindrom)

en_buyuk_palindrom=max(liste)

print(en_buyuk_palindrom)