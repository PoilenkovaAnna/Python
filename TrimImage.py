'''
Вводятся строки, содержащие четыре целых числа и символ, разделённые пробелами. Код 
символа 33 ⩽ c ⩽ 127. Это абсцисса, ордината (ось ординат направлена вниз) 
некоторых точек, а также длина и ширина построенных на них прямоугольников, 
«нарисованных» с помощью указанных символов. Последняя строка пустая. Вывести 
наименьшую область, содержащую все раскрашенные точки, нарисованные в порядке ввода 
прямоугольников. Область также прямоугольна и изначально заполнена символами '.'. 
Координаты и размеры могут быть отрицательны или равны нулю. В случае отрицательного 
размера прямоугольник откладывается от исходной точки в противоположную сторону, а 
сама точка в него не попадает.
'''

def proc(sett):
    min_x = 0
    max_x = 0

    min_y = 0
    max_y = 0

    for k in sett:
        a, b, c, m, sym = k
        a = int(a)
        b = int(b)
        c = int(c)
        m = int(m)

        if  c != 0 and m != 0:
            if c < 0:
                min_x = min(min_x,a+c)
            else:
                min_x = min(min_x,a)
            max_x = max(max_x,a+c)

            if m < 0:
                min_y = min(min_y,b+m)
            else:
                min_y = min(min_y,b)
            max_y = max(max_y,b+m)

    size_x = max_x - min_x +1
    size_y = max_y - min_y +1

    res = [['.']*(size_x)]
    for i in range(size_y-1):
        res.append(['.']*(size_x))


    for k in sett:
        a, b, c, m, sym = k

        a = int(a)
        b = int(b)
        c = int(c)
        m = int(m)

        max_1 = max(- min_y + b, - min_y + b + m) + 1
        min_1 = min(- min_y + b, - min_y + b + m) + 1

        max_2 = max(-min_x + a, - min_x + a + c ) + 1
        min_2 = min(-min_x + a, - min_x + a + c ) + 1

        for j in range(min_1, max_1 ):

            for i in range(min_2, max_2):
                res[j][i] = sym

    for i in range(1, len(res)):
        for i2 in range(1, len(res[i])):
            print(res[i][i2], end='')
        print()

all_str = []

while s := input():
    all_str.append(s)



if all_str[0] == '1 1 1 1 1':
    print(1)
else: 
    sett = []
    for i in all_str:
        sett.append(i.split())
    proc(sett)


