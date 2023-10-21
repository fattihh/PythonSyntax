istenensayi= int(input("Bir sayı giriniz : "))

asalMi=True

for i in range(2,istenensayi):
    if istenensayi % i == 0:
        asalMi=False
        break
if asalMi==True:
    print(f"{istenensayi} asaldır.")
else:
    print("Sayı asal değildir")
