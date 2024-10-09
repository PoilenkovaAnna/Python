'''
Разбор пакета

На вход подаётся содержимое некоторого пакета данных — строка в формате base85. 
Пакет состоит из заголовка и тела. Заголовок содержит последовательность ненулевых 
байтов, заканчивающуюся нулевым. Каждый байт заголовка — число 1, -1, 2, -2, 4, -4, 
8 или -8 (других нет). Модуль этого числа описывает количество байтов в очередном 
поле записи. Тело состоит из нуля или более записей, определяемых в заголовке. Если 
число отрицательное, соответствующее поле — целое со знаком, если положительное — 
беззнаковое. Выравнивания между полями и между записями нет. Порядок байтов — 
«сетевой» (big endian). Вывести сумму всех полей пакета.
'''
def get_header(byte_string):
    byte_array = struct.unpack(len(byte_string)*'b', byte_string)
    i = 0
    res = []
    while byte_array[i]:
        res.append(byte_array[i])
        i+=1
        
    return res

def get_body(byte_string):
    flag = False
    result = []
    for b in byte_string:
        if flag:
            result.append(b)
        if not flag and b == 0:
            flag = True
        
    return bytes(result)

def split_body(byte_str, size):  
    res = []
    for i in range(0, len(byte_str), size):
        res.append(bytes(byte_str[i:i+size]))
    return res

def make_pattern(header):
    s = { 1: 'B', -1: 'b', 2: 'H', -2: 'h', 4: 'I', -4 :'i', 8:'Q', -8 :'q'}
    res = '!'
    for i in header:
        res += s[i]
    return res 

import struct
import base64

s = input()

encoded = base64.b85decode(s)

header = get_header(encoded)
body = bytes(get_body(encoded))
size = sum(abs(number) for number in header)

pattern = make_pattern(header)

all_sum = 0 
for i in split_body(body , size):
    all_sum += sum(struct.unpack(pattern, i))

print(all_sum )


