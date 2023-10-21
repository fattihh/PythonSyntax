istenensayi= int(input("Faktoriyelini almak istediğiniz sayıyı giriniz : "))

faktoriyel=1

for i in range(1,istenensayi+1):
    faktoriyel *= i

print(f"{istenensayi}! : {faktoriyel}")

