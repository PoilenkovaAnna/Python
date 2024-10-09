'''
Написать функцию moar(a, b, n) от трёх параметров — целочисленных 
последовательностей a и b, и натурального числа n. Функция возвращает True, если в a 
больше чисел, кратных n, чем в b, и False в противном случае.
'''

def moar(a, b, n):
    count_in_a = 0
    count_in_b = 0
    if type(a) == int:
        a = [a]
    if type(b) == int:
        b = [b]
        
    for i in a: 
        if i%n == 0:
            count_in_a+=1
    for i in b: 
        if i%n == 0:
            count_in_b+=1
    return count_in_a > count_in_b

exec(input()) 

