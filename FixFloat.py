'''
Фиксированная точность

Написать функцию-параметрический декоратор fix(n), с помощью которой все 
вещественные (как позиционные, так и именные) параметры произвольной декорируемой 
функции, а также её возвращаемое значение, округляются до n-го знака после запятой. 
Если какие-то параметры функции оказались не вещественными, или не вещественно 
возвращаемое значение, эти объекты не меняются.
'''

def fix(n):
    def dect(fun):
        def newfun(*args, **kwargs):
            a = []
            
            for arg in args:
                if type(arg) is str:
                    arg = eval(arg)
                a.append(round(arg, n))
  
            res = fun(*a, **kwargs)
                
            if type(res) is float or type(res) is int: 
                return round(res, n)
            
            return res
            
        return newfun
    return dect

