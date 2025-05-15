class calisan:
    def __init__(self,name,surname,age,money):
        self.name=name #global
        self.surname=surname
        self.age=age
        self.__money=money #private
    
    #GET SET GLOBAL FONK
    def getMoney(self):
        return self.__money

    def setMoney(self,amount):
        self.__money = amount
    
    #PRİVATE FONK
    def __increase(self):
        self.__money = self .__money + 500

    
    def show_info(self):
        print(f"İsim {self.name} , Soyisim {self.surname}, Yas {self.age}, para{self.__money}")

calisan1=calisan("Fatih","Ucar",20,5000)
calisan1.show_info()



