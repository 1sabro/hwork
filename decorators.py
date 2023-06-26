# def outer(x):                 #
#         def inner(y):         #
#                 return x+y    #
#         return inner          #
# inner_func = outer(2)         #
# print(inner_func(10))


# def test_func(func):
#     def inner_test_func():
#         func()
#     return inner_test_func

# def hello(func):
#     # тело
#     pass

'''
Декоратор ->функция высшего порядка ( в качестве аргумента принимаеи
и возвращает функцию), которая оборачивает другую функцию для
расширения ее функционала, при этом не изменяя код
'''


# def test(func):
#     func()
#     print('hello')


# def a():
#     print("привет")
    

# test(a)

# def benchmark(func):
#     import time
#     start = time.time()
#     func()
#     end = time.time()
#     print(f'время работы функции{func.__name__}заняло ,{end - start}')
# def loop():
#     i = 0
#     while i < 1000000:
#         print(i)
#         i += 1

# # benchmark(loop)
# def test_for_loop():
#     for i in range(1000000):
#         print(i)
# benchmark(test_for_loop)

# def decorator(func):
#     def wrapper():
#         print('Функция обертка')
#         print(f'оборачиваем функцию {func.__func__}')
#         func()
#         print('выходим из обертки')
#     return(wrapper)

# def say_hi():
#     print('hiiiiiiiiiiiii')

# say_hi = decorator(say_hi)
# (say_hi)

'''
как работает "@decorator" под капотом  
тут как в функции замыкания  
say_hi = decorator(say_hi)
say_hi

@ - > синтакситечкий сахар позволяет нам явно указать какой декоратор применяется для функции

вызывает функция decorator и результат выполнения этой функции сохраняет в переменной с точной таким же названием как и обернутая функция
'''
# def uppercase_decorator(func):
#     def wrapper():
#         func_ = func()
#         upper_str = func_.upper()
#         return upper_str
#     return wrapper

# @uppercase_decorator
# def inp_str():
#     str_ = input('')
#     return str_

# print(inp_str())


# def benchmark(func: callable)-> None:
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'время работы функции{func.__name__}заняло ,{end - start}')
#     return wrapper
# @benchmark
# def loop():
#     i = 0
#     while i < 1000000:
#         print(i)
#         i += 1
# loop()

