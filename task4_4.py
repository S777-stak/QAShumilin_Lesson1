1 есть строка с именами разделенная пробелами "john marta james Morgan Adam Maria huang" 
преобразовать строку таким образом что бы каждое имя однозначно начиналось с большой буквы.

string = "john marta james Morgan Adam Maria huang" 
capitalized_string = string.title()
print('Capitalized String:', capitalized_string)


2 есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"] 

выведите в консоль имена, каждое с новой строки 
выровняв по правой стороне 
используя метод строки и форматирование через f string. 

Так же над именами первой строкой выведити заговловок Names 
где слово names должно быть посредине а остальное пространство заполнено скажем символом "*"

names = ["John", "Marta", "James", "Amanda", "Marianna"] 
for name in names:
    if not name:
        print("Names".center(50, '*'))
    print(f"{name:>10}")


3 есть строка переданная в качестве квери параметров 
"     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             ". 
Преобразовать эту строку в словарь 
где ключем должно быть значение перед = 
а значение пары значение после = {name: Amanda......}

cookie = "name=Amanda=sssss&age=32&&salary=1500&currency=quro"
pairs = cookie.split('&')
for pair in pairs:
   new_dict = dict([pair.split('=', maxsplit=1)])


4 у вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"] 
преобразовать его в список имен переменных для пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"]

import re

name = ["FirstItem", "FriendsList", "MyTuple"]
name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print(name)

5 у вас есть текст разбейте текст по предложениям. 
В качестве результата вы должны получить список из предложений.
import re

text = """\
Adam Jones Jr. thinks he didn't. In any case, this isn't true... 
"""
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

for stuff in sentences:
        print(stuff)    