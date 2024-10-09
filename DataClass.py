'''
Хранилище объектов

Написать функцию sloter(fields, default), которой передаётся последовательность 
полей fields, и значение по умолчанию default, а возвращает она класс, в экземпляре 
которого все эти поля есть, равны указанному значению и способны хранить 
произвольные объекты. Попытки создать другие поля в этом экземпляре должны приводить 
к исключению AttributeError. При проходе циклом экземпляр возвращает поля в порядке 
их объявления.
'''

def sloter(fields, _default):
    
    class Clas:
        __slots__ = fields

        def __init__(self):
            for field in fields:
                object.__setattr__(self,field, _default)

        def __iter__(self):
            for slot in self.__slots__:
                yield self.__getattribute__(slot)
                
        def __delattr__(self, name ):
            object.__setattr__(self, name, _default)

            
    return Clas


