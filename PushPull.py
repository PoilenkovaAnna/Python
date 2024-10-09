'''
Тяни-толкай

Написать класс Pushpull, при создании экземпляра которого задаётся целое число (по 
умолчанию — 0) — положение тянитолкая, измеряемое в шагах от столба (отрицательное 
число — влево, положительное — вправо, ноль — тянитолкай у столба). Класс обладает 
следующими свойствами:

имеет метод push(n), перемещение тянитолкая вправо на n шагов (по умолчанию 1)
имеет метод pull(n), перемещение тянитолкая влево.
экземпляр класса итерируем, при этом возвращается последовательность чисел от 0 до 
текущего положения тянитолкая (не включая само положение)
преобразование в строку выглядит так: "<слева<", "<0>" и ">справа>"
все экземпляры этого класса задают положение/перемещают одного и того же тянитолкая.
'''

class Pushpull():
    current_n = 0
    
    def __init__(self, n = 0):
        Pushpull.current_n = n
    
    def pull(self, shift = 1):
        Pushpull.current_n -= shift
    
    def push(self, shift = 1):
        Pushpull.current_n += shift
    
    def __str__(self):
        if  Pushpull.current_n > 0:
            st = '>'+str(Pushpull.current_n)+'>'
        elif Pushpull.current_n < 0:
            st = '<'+str(-Pushpull.current_n)+'<'
        else:
            st = '<0>'

        return st
        
    def __iter__(self):
        if Pushpull.current_n != 0:
            for i in range(0,Pushpull.current_n, 
Pushpull.current_n//abs(Pushpull.current_n)):
                yield i 
    
    def __getitem__(self, index):
            return index

