'''
Написать четыре функции (функционала): ADD(f, g), SUB(f, g), MUL(f, g) и DIV(f, g), 
параметрами которых могут быть как обычные объекты, так и функции от одной 
переменной (проверить, является ли объект функцией можно с помощью 
callable(объект)). Возвращать эти функционалы должны функцию от одной переменной 
h(x), которая выполняет соответствующее действие — f(x)+g(x), f(x)-g(x), f(x)*g(x) 
или f(x)/g(x) — над этими переменными. Если f или g не были функцией, вместо f(x) 
используется f, а вместо g(x) — g (например, при умножении функции на константу).
'''

def ADD(f, g):
    def inner(x):
        if callable(f):
            a = f(x)
        else: 
            a = f
            
        if callable(g):
            b = g(x)
        else: 
            b = g
        return a + b
    return inner
    
def SUB(f, g):
    def inner(x):
        if callable(f):
            a = f(x)
        else: 
            a = f
            
        if callable(g):
            b = g(x)
        else: 
            b = g
        return a - b
    return inner
  
def MUL(f, g):
    
    def inner(x):
        if callable(f):
            a = f(x)
        else: 
            a = f
            
        if callable(g):
            b = g(x)
        else: 
            b = g
            
        return a * b
    
    return inner
    
def DIV(f, g):
    def inner(x):
        if callable(f):
            a = f(x)
        else: 
            a = f
            
        if callable(g):
            b = g(x)
        else: 
            b = g
        return a/ b
    return inner



exec(input())

