'''
Параметры по умолчанию

Написать метакласс init, который рассчитывает на то, что методы создаваемого им 
класса полностью аннотированы. Для каждого позиционного параметра обычного метода в 
этом классе предусматривается значение по умолчанию (если оно не было задано) на 
основании типа в аннотации. Если в аннотации тип параметра простой, значение по 
умолчанию — это тип_пареметра() Если в аннотации тип параметра составной 
(тип_контейнера[ещё типы], например, list[int]), значение по умолчанию — это 
тип_контейнера() Если объект соответствующего типа нельзя создать конструктором без 
операндов, значение по умолчанию — None
'''

import decimal
import types
from inspect import signature
from inspect import Parameter

class init(type):

    # для автоматического создания пространства имён, если есть -> #ndigits 
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):  
        return super().__prepare__(name, bases, **kwds)
    
    #создаёт экземпляр объекта
    @staticmethod
    def __new__(mcs, name, bases, attrs):
        return super().__new__(mcs, name, bases, attrs)

    # заполняет готовый класс 
    def __init__(cls, name, parents, ns, **kwds):
        res = super().__init__(name, parents, ns, **kwds)
        return res 
    
    #для внесения правок при создании экземпляра класса
    def __call__(cls, *args, **kwargs):
 
        method = cls.__init__    
        sig = signature(method)
        keys = sig.parameters.keys()
        argdefs = method.__defaults__

        i = 0   
        for key in keys:
            var = sig.parameters[key]
            
            if key != 'self':
                
                    
                if not key in kwargs.keys():
                    if i < len(args): 
                        kwargs[key] = args[i]
                        i+=1            
                    else:
                        if '=' in str(var):
                            kwargs[key] = var.default 
                        else:
                            if isinstance(var.annotation, types.GenericAlias):
                                var = var.replace(default = var.annotation(), 
annotation=var.annotation)
                                kwargs[key] = var.default
                            else:
                                if str(var.annotation) == "<class 'int'>":
                                    kwargs[key] = 0
                                elif '__main__' in str(var.annotation):
                                    var = var.replace(default = var.annotation(), 
annotation=var.annotation)
                                    kwargs[key] = var.default
                                else:
                                    kwargs[key] = None                         
        return super().__call__(**kwargs)


