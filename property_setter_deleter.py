class Kisi:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    
    @property #Bir fonksiyonu nesnenin özelliğiymiş gibi kullanmamızı sağlar
    def adsoyad(self):
        return f"{self.name},{self.surname}"
    
    def email(self):
        return f"{self.name}.{self.surname}@sirket.com"
    
    @adsoyad.setter #Property ile dönüstürdügümüz fonksiyona degisken atamak icin kullanılır.
    def adsoyad(self,isim):
        ad,soyad=isim.split(" ")
        self.ad=ad
        self.soyad=soyad

    @adsoyad.deleter #özelliği silmemize yarar
    def adsoyad(self):
        print("silindi")

kisi1=Kisi("Fatih","Ucar")
print(kisi1.adsoyad)
del kisi1.adsoyad