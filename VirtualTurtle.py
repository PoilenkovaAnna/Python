'''
Примитивная черепашка

Написать параметрическую генератор-функцию turtle(coord, direction), описывающую 
движение «черепахи» по координатной плоскости. coord — это кортеж из двух 
целочисленных начальных координат, direction описывает первоначальное направление (0 
— восток, 1 — север, 2 — запад, 3 — юг). Координаты увеличиваются на северо-восток. 
Генератор принимает три команды — "f" (переход на 1 шаг вперёд), "l" (поворот против 
часовой стрелки на 90°) и "r" (поворот по часовой стрелке на 90°) и возвращает 
текущие координаты черепахи.
'''

def turtle(coord, direction):
    
    command = yield
    while command:
        if command == "f":
            if direction == 0:
                coord = (coord[0] + 1, coord[1])
            elif direction == 1:
                coord = (coord[0], coord[1]+1)
            elif direction == 2:
                coord = (coord[0] - 1, coord[1])
            elif direction == 3:
                coord = (coord[0], coord[1]-1)
        elif  command == "l":
            direction = (direction + 1)%4
        elif  command == "r":
            direction = (direction - 1)%4


        command = yield (coord[0], coord[1])

