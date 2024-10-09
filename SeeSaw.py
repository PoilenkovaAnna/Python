'''
Чёт-нечет

Написать генератор-функцию seesaw(sequence), которой на вход передаётся итерируемая 
целочисленная последовательность, а конструируемый ею генератор возвращает 
поочерёдно то чётный, то нечётный элемент последовательности в порядке следования. 
Если элементы одного типа заканчиваются, возвращаются только элементы другого.
'''

from itertools import tee, filterfalse, zip_longest

        
def seesaw(sequence):
    two_sequence = tee(sequence, 2)
    even_sequence = filterfalse(lambda x: x%2, two_sequence[0]) 
    odd_sequence = filterfalse(lambda x:  not x%2,two_sequence[1]) 
    a = zip_longest(even_sequence , odd_sequence, fillvalue = None )
    
    for typle in a:
        for i in typle:
            if i != None:
                yield i

