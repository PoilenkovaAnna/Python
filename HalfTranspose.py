'''
Условие - https://uneex.org/LecturesCMC/PythonIntro2022/Homework_HalfTranspose

'''
first_str = list(eval(input()))
mas = [first_str]

for i in range(1, len(first_str)):
    item = list(eval(input()))
    mas.append(item)

        
print(mas[0][0])

for k in range(1, len(mas)):
        res = list()
        res.append(mas[k][0])
        
        for i in range(1,k+1):
            res.append(mas[k][i])
            
        for j in range(k-1,0,-1):
            res.append(mas[j][k])
            
        res.append(mas[0][k])
        
        print(*res, sep=',')
