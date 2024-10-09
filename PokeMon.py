'''
Покемоны

Участники некоторой карточной игры владеют несколькими колодами, из которых они 
составляют свой уникальный игровой набор. Каждая колода имеет номер; колоды с 
одинаковыми номерами содержат совпадающие наборы карт. Ввести строки вида "имя 
игрока / номер колоды" (колода принадлежит игроку) или "номер колоды / название 
карты" (карта входит в колоду); последняя строка пустая. Вывести в алфавитном 
порядке имена игроков, которые могут составить игровой набор из наибольшего числа 
различных карт.
'''

players = {}
carts = {}

while s := input():
    s = s.split(' / ')

    if s[0].isdigit():
        key = int(s[0])
        carts.setdefault(key)
        if carts[key] is None :
            carts[key] = {s[1]}
        else:
            carts[key].add(s[1])
    else: 
        val = int(s[1])
        players.setdefault(s[0])
        if players[s[0]] is None :
            players[s[0]] = {val}
        else:
            players[s[0]].add(val)
res = {}
for key in players:
    sets = set() 
    for i in players[key]:
        if not carts.get(i) is None:
            sets.update(carts.get(i))
    
    res.setdefault(len(sets))
    if res[len(sets)] is None :
        res[len(sets)] = {key}
    else:
        res[len(sets)].add(key )

if len(res) > 0:
    res = sorted(res[max(res.keys())])
    for i in res:
        print(i)

