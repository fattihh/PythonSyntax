class calisan:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        self.email= name+surname+"@sirket.com"

    def bilgileri_goster(self):
        return f"isim {self.name}, soyisim {self.surname}"

class Yazilimci(calisan):
    def __init__(self, name, surname,age):
        #Kalıtım alınan sınıfın üzerine yeni bir özellik ekleme
        super().__init__(name, surname)
        self.age=age
    
    def bilgileri_goster(self):
        info = super().bilgileri_goster()
        print(info + f"{self.age}")

    zam_orani=1.2

class Yonetici(calisan):
    def __init__(self, name, surname,calisanlar=None):
        super().__init__(name, surname)
        if calisanlar == None:
            self.calisanlar=[]
        else:
            self.calisanlar=calisanlar
    
    def bilgileri_goster(self):
        info= super().bilgileri_goster()
        print(info + self.calisanlar)

    def calisan_ekle(self,calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)
    
    def calisan_sil(self,calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)
    
    def calisanlari_goster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgileri_goster())


yazilimci1= Yazilimci("Fatih","Ucar",20)
yazilimci2 = Yazilimci("Yakup","Cinar",19)

yonetici1=Yonetici("İcardi","Riverio")

yonetici1.calisan_ekle(yazilimci1)
yonetici1.calisan_ekle(yazilimci2)

yonetici1.calisanlari_goster()


