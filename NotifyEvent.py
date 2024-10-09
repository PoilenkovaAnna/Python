'''
Оповещения

Написать класс NotifyEvent (унаследованный от asyncio.Event) со следующими 
свойствами В методе оповещение.set(имя) присутствует строка-имя адресата 
уведомления, но по умолчанию это None Перед каждым оповещение.set() (кроме самого 
первого) требуется вызов оповещение.clear() Метод await оповещение.wait() возвращает 
имя адресата уведомления (но в остальном работает как event.wait()) Написать также 
сопрограмму task(имя, оповещение) со следующими свойствами: Если уведомление «своё» 
— адресат уведомления совпадает с именем, — выводится имя, количество принятых 
«своих» уведомлений и количество принятых «чужих» уведомлений Если вместо имени 
await оповещение.wait() вернул None, работа завершается Использовать внутреннюю 
реализацию asyncio.Event в этой задаче нельзя
'''

import asyncio

class NotifyEvent(asyncio.Event):
    def __init__(self):
        super().__init__()
        self._name = None
        self._my_event = asyncio.Event()
        self._my_event.set()

    def set(self, name=None):
        self._name = name
        super().set()

    async def wait(self) -> str:
        await self._my_event.wait()
        await super().wait()
        self._my_event.clear()
        return self._name

    def clear(self):
        self._my_event.set()
        return super().clear()

async def task(name, notify_event):
    mine = 0
    others = 0

    a = await notify_event.wait()
    if(a == name):
        mine += 1
    else:
        others += 1
    if a == name:
        print (str(name) + ": " + str(mine) + " / " + str(others))
    while a is not None:
        a = await notify_event.wait()
        if a is not None :
            if(a == name):
                mine += 1
            else:
                others += 1
            if a == name:
                print (str(name) + ": " + str(mine) + " / " + str(others))
