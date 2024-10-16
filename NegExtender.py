'''
Больше, чем минус

Написать класс NegExt, расширяющий унарный минус по следующей схеме: Производный 
класс должен конструироваться с помощью class потомок(NegExt, родитель): Если для 
родителя можно вызвать унарный минус, -потомок() возвращает то же, что и -родитель() 
Если для родителя унарный минус не работает, но работает операция секционирования, 
-потомок() возвращает собственную секцию [1:-1] В противном случае возвращается сам 
потомок Результат нужно преобразовать к типу потомка
'''

class NegExt:
    def __neg__(self):
        cl = self.__class__
        try:  
            return cl(super().__neg__())
        except: pass  
            
        try:      
            var = self.__getitem__(slice(1, -1, None))
            return cl(self.__getitem__(slice(1, -1, None)))
        except:
            return cl(self)

