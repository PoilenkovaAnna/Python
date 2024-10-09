'''
Размер архива

Написать программу, которой на стандартный ввод подаётся tar-архив в виде 
шестнадцатеричного дампа (последовательность шестнадцатеричных цифр, возможно, 
разделённых пробелами и переводами строки), а на выходе она показывает количество и 
суммарный объём хранящихся в нём файлов, если их распаковать.
'''


import tarfile
import io
import binascii
import fileinput

hex_string = ''
for line in fileinput.input():
    hex_string += line

bytes_string = bytes.fromhex(hex_string)
# fileobj - альтернатива файловому объекту, открытому в двоичном режиме для имени. 
Он должен быть в позиции 0.
    
# Now we have a bytes string, convert that into a stream
stream = io.BytesIO(bytes_string)
    
count = 0 
size = 0 
    
with tarfile.open(fileobj = stream , mode = 'r') as archive:
    count = sum(1 for one in archive if one.isreg())
    size = sum(one.size for one in archive if one.isreg())
    
print(size, count)

