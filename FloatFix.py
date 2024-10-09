'''
Фиксированная точка

Написать метакласс fixed с параметром ndigits (по умолчанию 3), в котором все 
возвращаемые обычными (не статическими и не методами класса) методами значения 
округляются с помощью round() до ndigits знаков после запятой, если они вещественные 
по определению модуля numbers.
'''

import decimal
import types


class fixed(type):

    # для автоматического создания пространства имён, если есть -> #ndigits 
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):  
        return super().__prepare__(name, bases, **kwds)
    
    #создаёт экземпляр объекта
    @staticmethod
    def __new__(mcs, name, bases, attrs, ndigits = 3):
    
        def notify(func, *args, **kwargs):
            def fncomposite(*args, **kwargs):
                for arg in args:
                    if isinstance(arg, decimal.Decimal):
                        return func(*args, **kwargs)
                try:
                    return round(func(*args, **kwargs),  ndigits)
                except: 
                    return func(*args, **kwargs)
            return fncomposite

        for attr, method in attrs.items():
            
            if isinstance(method, types.FunctionType):
                # оборачиваем все методы декоратором            
                attrs[attr] = notify(method)  
                
        return super().__new__(mcs, name, bases, attrs)

    # заполняет готовый класс 
    def __init__(cls, name, parents, ns, **kwds):
        res = super().__init__(name, parents, ns)
        return res 
    
    #для внесения правок при создании экземпляра класса
    def __call__(cls, *args, **kwargs):
        return super().__call__(*args , **kwargs)


