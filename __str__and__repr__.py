class Futbolcu:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
    
    #KULLANICI İCİN PRİNT
    def __str__(self):
        return f"futbolcu isim soyisim ve yas {self.name}, {self.surname}, {self.age}"


    #GELİŞTİRİCİLER İCİN PRİNT
    def __repr__(self):
        return f"Futbolcu({self.name},{self.surname},{self.age})"

futbolcu1=Futbolcu("Fatih","Ucar",20)
print(futbolcu1)
print(futbolcu1.__repr__())