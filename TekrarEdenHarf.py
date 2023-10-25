string = "AabBcCdecdKlKKlMMMNNSsSsAaASasaSDas"
bosListe=[]
kucukstring=string.lower()

for harf in kucukstring:
    if harf not in bosListe:
        bosListe.append(harf)
    else:
        continue

print(len(bosListe))
