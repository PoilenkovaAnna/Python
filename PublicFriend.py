'''
Знаком со всеми

Вводятся в столбик пары натуральных чисел через запятую. Каждая пара M, N обозначает 
взаимное знакомство людей под номерами M и N. Ввод заканчивается парой 0, 0 (не 
учитывается, и вообще человек N считается незнакомым с человеком N ;) ). Вывести 
через пробел в порядке возрастания номера тех, кто знаком со всеми остальными, или 
пустую строку, если таких нет.
'''

x = {}
a,b = eval(input())
while a != 0 or b != 0:
    x.setdefault(b)
    x.setdefault(a)
    
    if x[b] is None :
        x[b] = {a}
    else:
        x[b].add(a)
    
    if x[a] is None:
        x[a] = {b}
    else:
        x[a].add(b)
    
    a,b = eval(input())

keys = x.keys()
res = []
for key in x:
    x[key].add(key)
    
    if x[key] == keys:
        res.append(key)
res.sort()
print(*res)

