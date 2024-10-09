'''
Странный класс

Написать класс Nuts, экземпляры которого можно конструировать из любого набора 
объектов (в т. ч. из ничего) можно индексировать по чему угодно (возвращается 
объект, который использовался в индексе) в том числе позволяют присваивать и удалять 
по индексу (ничего не происходит) содержат любое поле (возвращается имя этого поля) 
в том числе позволяют присваивать и удалять поля (ничего не происходит) итерируемы 
(возвращаются строки "N", "u", "t" и "s") в виде строки представляются как "Nuts"
'''

def __delitem__(name):
    pass
    
class Nuts:
    prnt = "Nuts"
    
    def __init__(self, *arg):
        pass
    
    def __iter__(self):
        for letter in self.prnt: 
            yield letter
    
    def __getitem__(self, index):
        return index
    
    def __setitem__(self, key, value): 
        pass
    
    def __getattr__(self, name):
        return name
    
    def __str__(self, item = prnt):
        return item
    
    def __delitem__(self, name):
        return 0
    
    def __setattr__(self, name, value):
        pass
    
    def  __delattr__(self, name):
        pass  

