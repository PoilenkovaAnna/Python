'''
Условие - https://uneex.org/LecturesCMC/PythonIntro2022/Homework_ChudnPi
'''
from decimal import *
getcontext().prec = 10000

def PiGen():
    pi = Decimal(13591409)
    w = Decimal(1)
    m = Decimal(Decimal(10005).sqrt()/4270934400)
    k = 1
    while True:
        w *= - Decimal((6*k-5)*(2*k-1)*(6*k-1))/Decimal(k**3*26680*640320*640320)
        pi += ( 13591409 + 545140134*k) * w
        k += 1
        yield (pi * m)**(-1)
