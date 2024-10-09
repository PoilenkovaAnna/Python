'''
Известно, что любое натуральное число можно представить в виде суммы не более чем 
четырех квадратов неотрицательных целых чисел (теорема Лагранжа). Ввести натуральное 
N⩽100000 и найти для него такие целые неотрицательные x,y,z и t, чтобы 
x²+y²+z²+t²=N. Вывести все такие четвёрки в следующем формате: x,y,z и t — через 
пробел, и упорядочены по убыванию, а сами четвёрки — лексикографически по 
возрастанию (без повторений).
'''
N = int(input())

import math
for x in range(int(math.sqrt(N)//2), int(math.sqrt(N)) + 1):
    
    N1 = N - x*x
    
    for y in range(int(math.sqrt(N1)//2), min(x + 1, int(math.sqrt(N1)) + 1)):
        
        N2 = N1 - y*y
        
        for z in range(int(math.sqrt(N2)//2), min(y + 1, int(math.sqrt(N2)) + 1)):
            
            N3 = N2 - z*z
            
            for t in range(int(math.sqrt(N3)//2), min(z + 1, int(math.sqrt(N3)) + 
1)):
                
                if (N3 == t*t):
                    print(x, y, z, t)


