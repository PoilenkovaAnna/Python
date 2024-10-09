'''
MRO C3

Написать программу, на вход которой подаётся синтаксически верный код на ЯП Python, 
состоящий только из объявления классов верхнего уровня, без пустых строк и 
многострочных констант. В наследовании используются только уже определённые ранее в 
этом коде классы. На выходе программа должна отчитаться, допустимо ли наследование, 
которое (возможно) встретилось в коде (с точки зрения MRO C3), и вывести "Yes" или 
"No".

'''

import re 
Cls_parents, Calc_linear = {}, {}


def merge(parents):
    if not parents: return
    queues = [Calc_linear.setdefault(c, [c, *merge(Cls_parents[c])]).copy() for c in 
parents] + [parents]
 
    while queues:
        for queue in queues:
            next_cls = queue[0]
            if all(next_cls == q[0] or next_cls not in q for q in queues):
                yield next_cls 
                for q in queues:
                    if q and q[0] == next_cls:
                        del q[0]
                queues = list(filter(len, queues))
                break
        else:
            raise TypeError

while string:= input():
        
        string_with_class = re.findall('^class *([A-Za-z0-9(), ]*)' ,string)
        
        if string_with_class:
            name_class_and_parents = string_with_class[0].replace(' ', 
'').replace('(', ')').split(')')

            cls = name_class_and_parents[0]
            
            parents = name_class_and_parents[1] if len(name_class_and_parents) > 2 
else []
    
            Cls_parents[cls] = parents.split(',') if parents else []

            try:
                Calc_linear[cls] = [cls, *merge(Cls_parents[cls])]
            except TypeError:
                print('No')
                break

else:
    print('Yes')


