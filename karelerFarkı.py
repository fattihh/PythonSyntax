toplam1=0
yuzsayının_toplamı=0


for i in range(1,101):
    toplam1 += i*i
for i in range(1,101):
    yuzsayının_toplamı+=i

yuzsayının_toplamı = yuzsayının_toplamı*yuzsayının_toplamı
print(yuzsayının_toplamı-toplam1)
