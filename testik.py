# def get_word(word):
#     list_letters = list(word)
#     return list_letters

# def get_vowels(letters):
#     vowels = ['a', 'y', 'i', 'o', 'e','u']
#     list_vowels = [letter for letter in letters if letter is vowels]
#     result = ''.join(list_vowels)
#     return result
# my_word = input('enter:')
# print(get_vowels(get_word(my_word)))

# def get_string_length(word):
#     a = len(word)
#     return a
# print(get_string_length('iskhak'))

# def get_type(a, b):
#     print(f'{type(a)}\n{type(b)}')
# get_type('a', 9)
# str_='kuma'
# print(str_[::-1])

# def multiply_list(x):
#     pro=1
#     for i in x:
#         pro*=i
#     return pro
# print(multiply_list([1, 2, 3, 4, 5, 6])) 
   
# def  sum_digits(a):
#     w = 0
#     digits = [int(i) for i in str(a)]
#     for i in digits:
#         w += i
#     return w
# print(sum_digits(123))  
# Создать функцию func11, которая будет принимать 3 числа в качестве аргументов,
# функция должна возвращать сумму первых двух чисел разделенную на третье число
# нужно реализовать проверку на то, что третье число не является нулем, 
# если это ноль, то просто возвратить результат сложения первого и второго числа
def func11(a,b,c):
    try:
        if c==0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        return a+b
    else:
        return (a+b)*c
print(func11(1,3,0))


# def func12(a):
#     a.lower()
#     return(a)
# print(func12('ISKHAK'))