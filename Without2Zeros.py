'''
Написать функцию No_2Zero(N, K), которая вычисляет количество N-значных чисел в 
системе счисления с основанием K, таких что их запись не содержит двух подряд идущих 
нулей. Лидирующие нули не допускаются. Для EJudge N⩽33.
'''


def No_2Zero(n, k):
    a = 1
    b = k - 1
    for i in range(2, n + 1):
        c = (a + b) * (k - 1)
        a, b = b, c
    return b


exec(input())

