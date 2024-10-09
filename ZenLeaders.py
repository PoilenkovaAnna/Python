'''
Ввести построчно список участников некоторого соревнования на скорость неизвестно 
чего в виде Имя Фамилия Название команды часы:минуты:секунды (последняя строка 
пустая), и вывести всех, кто занял первые три места (минимальное затраченное 
неизвестно на что время; одно место может занять несколько человек, если время 
совпадает), в порядке возрастания времени, а внутри одного времени — 
лекcикографически: фамилия, имя, команда. Дополнительное условие: таблица чемпионов 
должна быть аккуратной: поля «Имя», «Фамилия», «Название команды» и «Время» должны 
начинаться в одном столбце, между ними должен быть минимум один пробел, при этом 
строки должны иметь минимально возможную длину.

'''

import re
pattern = re.compile('^(\S+) (\S+) (.+) (\d+):(\d+):(\d+)$')
MAX_name, MAX_str, MAX_team = 0, 0, 0

res = []
while(True):
    str_i = input()
    if len(str_i) == 0: break
    name, str, team, hour, min, sec = re.findall(pattern, str_i)[0]

    MAX_name = max(len(name), MAX_name)
    MAX_str =   max(len(str), MAX_str)
    MAX_team = max(len(team), MAX_team)

    res.append((name, str, team, int(hour), int(min), int(sec)))
res.sort(key = lambda x: (x[3], x[4], x[5], x[1], x[0], x[2]))

winners = [res[0]]
k = 1
for i in range(1, len(res)):
    if (res[i][3] != res[i - 1][3]) or (res[i][4] != res[i - 1][4]) or (res[i][5] != 
res[i - 1][5]):
        k += 1
    if k > 3: break
    winners.append(res[i])

for winner in winners:
    print(f'{winner[0]:{MAX_name}} {winner[1]:{MAX_str}} {winner[2]:{MAX_team}} 
{winner[3]}:{winner[4]}:{winner[5]}')


