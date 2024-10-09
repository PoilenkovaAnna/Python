'''
Морзянка

Написать класс morse("строка"), экземпляр которого переводит арифметические 
выражения в морзянку! В выражении «+» — это точка, «-» — тире, а «~» — промежуток 
между буквами (бывает только между буквами и только один, проверять не надо). 
Параметр — строка, состоящая либо из символов, либо из слов. Строка состоит из слов, 
если в ней есть хотя бы один пробел (в этом случае между словами стоит ровно один 
пробел) Если в строке три элемента, они задают точку, точку на конце передаваемой 
буквы (традиционно обозначается другим слогом) и тире Два элемента задают точку и 
тире, а точка на конце буквы совпадает с обычной Если элемента четыре, четвёртый — 
это то, что выводится в конце сообщения По умолчанию: Если параметров нет, это слова 
"di", "dit" и "dah". Если параметры — слова: в конце сообщения выводится ".", 
разделители при выводе: пробел между сигналами и ", " между буквами. Если параметры 
— символы: непуст только разделитель между буквами (это пробел).
'''
class morse:
    point = ''
    end_point = ''
    fl_end_point = True
    dash = ''
    end = '.'
    space = ','
    space_between_words = ' '
    
    res_srt = ''
    
    def __init__(self, string =  "di dit dah"):
        if ' ' in string: # слова 
            arr_words = string.split(' ')
            self.point, self.end_point, self.dash = arr_words[0], arr_words[1], 
arr_words[2]
            if len(arr_words) == 4:
                self.end = arr_words[3] 
        else:             # элементы
            self.space_between_words = ''
            self.space = ' '
            self.end = ''
            
            if len(string) == 3:
                self.point = string[0]
                self.end_point = string[1]
                self.dash = string[2]
            elif len(string) == 2:
                self.point  = self.end_point = string[0]
                self.dash = string[1]
            elif len(string) == 4:
                self.point = string[0]
                self.end_point = string[1]
                self.dash = string[2]
                self.end = string[3]
    
    def __neg__(self):
        self.res_srt = self.space_between_words + self.dash + self.res_srt
        if self.fl_end_point:
            self.fl_end_point = False
        return self
        
    def __pos__(self):
        if (self.fl_end_point):
            self.res_srt = self.space_between_words + self.end_point  + self.res_srt
            self.fl_end_point = False
        else:
            self.res_srt = self.space_between_words + self.point + self.res_srt
        return self
        
    def __invert__(self):
        self.res_srt =  self.space + self.res_srt
        self.fl_end_point = True
        return self
    
    def __str__(self):
        if len(self.space_between_words) == 1: # если фраза из слов удаляем первый 
пробел
            self.res_srt = self.res_srt[1:]
        return self.res_srt + self.end
