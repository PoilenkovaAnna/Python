'''
Очередь с фильтром

Напишите класс FilterQueue со следующими свойствами: Это потомок asyncio.Queue В 
экземпляре класса атрибут очередь.window содержит первый элемент очереди, или None, 
если очередь пуста С помощью операции фильтр in очередь можно определить, 
присутствуют ли в очереди такие элементы, что выражение фильтр(элемент) истинно 
Метод .later() синхронно переставляет первый элемент очереди в её конец, или 
вызывает исключение asyncio.QueueEmpty, если очередь пуста Метод .get() содержит 
необязательный параметр фильтр. Вызов очередь.get(фильтр) работает так: Если в 
очереди нет элементов, на которых фильтр(элемент) истинно, работает как обычный 
.get(). Если в очереди есть элементы, на которых фильтр(элемент) истинно, 
переставляет первый элемент очереди в её конец до тех пор, пока фильтр(элемент) не 
истинно, а затем выполняет обычный .get(). Разрешается воспользоваться внутренним 
представлением Queue
'''

from collections import deque
import asyncio

class FilterQueue(asyncio.Queue): 
    
    @property
    def window(self):
        if self.empty():
            return None
        else:
            windows = self._queue[0]
            return windows

    def later(self):
        if self.empty():
            raise asyncio.QueueEmpty
        else:
            first = self._queue[0]
            super().get_nowait()
            self._queue.append(first)
            
    async def get(self, f = lambda n: n % 1):
        return self.get_nowait(f)
           

    def get_nowait(self, f = lambda n: n % 1): 
        if not super().empty():
            filter_list = list(filter(f, self._queue))
            
            if len(filter_list) == 0:
                    return super().get_nowait()
            else:
                while(filter_list[0] != self._queue[0]):
                    self.later()
                    
                return super().get_nowait()

