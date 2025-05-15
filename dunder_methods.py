class MyList(list):
    def __add__(self,other):
        if len(self) != len(other):
            return "Bu listeler toplanamaz"
        else:
            result = MyList()
            for i in range(len(self)):
                result.append(self[i]+other[i])
            
            return result
    
    def __sub__(self,other):
        if len(self) != len(other):
            return "Bu listeler toplanamaz"
        else:
            result = MyList()
            for i in range(len(self)):
                result.append(self[i]-other[i])
            
            return result
    

liste1=MyList([1,2,3])
liste2=MyList([4,5,6])

print(liste1+liste2)
