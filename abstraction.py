from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def run(self): pass
     
class Bird(Animal):
    pass

#Abstraction classtan nesne olusuturlamaz
#abstract methodlar child sınıfta kullanılmak zorundadır.