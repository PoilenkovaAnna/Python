'''
Ввести две строки и проверить, содержится ли вторая в первой, с учётом того, что 
символы второй строки могут находиться в первой на некотором равном расстоянии друг 
от друга. Вывести YES или NO.

'''

main = input()
st = input()


if (len(st) >= 2 ) and (st[0] in main) and (st[1] in main):
    
    index_1 = 0
    st_in_main = False 
    enum = False 
    
    while not st_in_main and not enum:
        index_1 += main[index_1:].index(st[0])
        index_2 = main[index_1:].index(st[1]) 

        st_in_main = st in main[index_1:len(main):index_2]
        
        while not st_in_main and not enum:
            ind = index_2 + index_1 + 1
            if (st[1] in main[ind:]):
                index_2 = ind + main[ind:].index(st[1]) - 1
                st_in_main = st in main[index_1:len(main):(index_2 - index_1)]
            else: 
                 enum = True
        
        index_1 += 1
        if not st_in_main and st[0] in main[index_1:]:
            enum = False 
        else: 
            enum = True 
     
    if st_in_main:
        print("YES")
    else: 
        print("NO")               
                
elif len(st) == 1:
    if st[0] in main:
        if main.index(st[0]):
            print("YES")
    else: 
        print("NO")
elif len(st) == 0:
    print("YES")
else:
    print("NO")
