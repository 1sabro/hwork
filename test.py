'=================================================================================================================='
#            Чтобы удалить пустые кортежи в списке: [i for i in tuples if i]


# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8] 
# number = 8
# if list_ == number: 
#     print('Oshjeh') 
# else: 
#     print(list_.count(number))



# a = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# v = int
# c = 0
# for i in a:
#     if i.isdigit():
#         c += i
# print(c)

# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# list_ = [k for k in dict_ if k]


# str_list = ['abc', 'xyz', 'aba', '1221']
# new = []
# num=-1
# for i in str_list:
#     num+=1
#     if i[0]==i[-1]:
#         new.append(num)
       
# print(new)

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = max(lists, key=len)
# min_list = min(lists, key=len)
# print('max_list',max_list)
# print('max_list',min_list)

#  a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
#  dict_ = [i for i in a, ]

# num1 = int(input(''))
# num2 = int(input(''))
# try:
#     num3 = num1 + num2
# except (ValueError):
#     print('Введите число!')



#генерация какой то последовательности в одну строку используя цикл for (синтаксический сахар)

# for переменная  in диапазон:
#     тело

"""синтаксис"""

# результат for  элемент in интерируемый объект

# результат for  элемент in интерируемый объект if фильтрация

# list:

# упрощает процесс создания списков

# list_=[] 
# for i in 'hello':
#     list_.append(i)
# print(list_)

# list1=[i for i in 'hello']
# print(list1)

# list1=[i for i in range(1,11) if i%2==0]
# print(list1)

# [элемент if условие else элемент 2 for i in итерируемый объект]

# print(['четное' if i%2==0 else 'нечетное' for i in range(1,11)])

#set: 

# list0=[1,2,23,4,2,5,23,]
# set1={i for i in list0}
# print(set1)

#dict:

# dict0={1:'a',2:'b',3:'c'}
# dict1={v: k for k,v in dict0.items()}
# print(dict0)
# print(dict1)
# print(dict1['a'])

# dict_={i:i**2 for i in range(1,11)}
# print(dict_)

# list_=[1,2,3,4,5,6,7,8,9,0]

# list1=[1,2,3,4,5,6,7,8,9,0]
# list2=[0,9,8,7,6,5,4,3,2,1]
# dict1={list1[i] : list2[i] for i in range (len(list1))}
# print(dict1)

'''========= вложенные comprehension========='''

# dct={i:[j for j in range(i+1)] for i in range(1,6)}
# print(dct)

# list1=[['hello world' for i in range(5)] for i in range(3)]
# print(list1)

# employees = {
#     'id1': {
#         'first name': 'Александр',
#         'last name' : 'Иванов',
#         'age': 30,
#         'job':'программист'
#             },
#     'id2': {
#         'first name': 'Ольга',
#         'last name' : 'Петрова',
#         'age': 35,
#         'job':'ML-engineer'
#             }
# }

# dct={key:{k:float(v) 
#           if k=='age' 
#           else v for k,v in 
#           value.items()} 
#           for key,value in 
#           employees.items()}
# print(dct)


# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# dict_ = {key: inner_dict[key] for key, inner_dict in my_dict.items()}
# print(dict_)



"""
1) Дан словарь my_dict значениями в котором являются другие словари.

Создайте новый словарь dict_, оставив те же ключи, но заменив значения, значениями внутренних словарей.

Например:
my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 

Результат:
dict_ = {'first': 1, 'second': 2} 

Нужно использовать comprehension.
"""
'''MADE'''

"""
2) Создайте список list_ из чётных целых чисел в промежутке от 1 до 25.

Нужно использовать comprehension.
"""
'''MADE'''
# list_=[i for i in range(1,25) if i%2==0]
# print(list_)
"""
3) Запросите у пользователя сумму cash которая у него сейчас есть в бумажнике. Если он введёт сумму, меньшую чем 0, то выбросите исключение ValueError с текстом:

Сумма не может быть отрицательной! 

иначе распечатайте сумму.
"""
'''MADE'''
# try:
#   cash=int(input('Введите сумму: '))
#   if cash<0:
#     raise ValueError
#   else: 
#     print(cash)
# except ValueError:
#   print('Сумма не может быть отрицательной! ')
"""
4) Напишите программу, которая будет получать через input 2 числа num1, num2 и будет печатать их сумму.

Обработайте ошибку, которая возникнет, если пользователь введёт что-то кроме числа и выведите сообщение, например:

Введите число!
"""
'''MADE'''
# try:
#   num1=int(input('Введите перове число: '))
#   num2=int(input('Введите второе число: '))
#   print(f'{num1} + {num2} =',num1+num2)
# except ValueError:
#   print('Введите число!')
#   num1=int(input('Введите перове число: '))
#   num2=int(input('Введите второе число: '))
#   print(f'{num1} + {num2} =',num1+num2)
  
"""
5) Создайте функцию get_string_length() которая будет принимать строку. Функция должна возвращать длину этой строки.

Например:
print(get_string_length('hello')) 

Вывод:
5
"""
'''MADE'''
# def get_string_length(x:str):
#   res=len(x)
#   return res
# print(get_string_length('Jumadil')) 
"""
6) Создайте функцию sum_digits(), которая принимает целое число и возвращает сумму всех его цифр.

Например:
print(sum_digits(105)) 

Вывод:
6

так как 1+0+5 = 6
"""
'''MADE'''
# def sum_digits(x):
#   z=str(x)
#   nums=[int(i) for i in z]
#   return(sum(nums))

# print(sum_digits(900001))
"""
7) Дана строка string. Вам необходимо вернуть словарь dict1, где ключами будут символы в этой строке, а значениями - числа, сколько раз встречается этот символ в строке.

Например:
string = 'text'

Вывод:

dict1 = {'t': 2, 'e': 1, 'x': 1}

Нужно использовать comprehension.
"""