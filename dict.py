# dict_ = {}
# print(type(dict_))


# my_list = [['m',7],['k',2],['f',5]]
# my_dict = dict(my_list, a = 8, m = 9)
# print(my_dict)


'''=====ПОЛУЧИТЬ ЗНАЧЕНИЮ ПО КЛЮЧУ======'''
# my_list = {
#     'sam':'white',
#     'juma': 'gay',
#     'aydin': 'ochkoshnik'
# }
# print(my_list['juma'])

'''======ЗАМЕНА ЗНАЧЕНИЯ======'''
# my_list = {
#     'sam':'white',
#     'juma': 'gay',
#     'aydin': 'ochkoshnik'
# }   
# my_list['juma']='negay'
'''======ДОБАВЛЕНИЯ НОВОГО ЭЛЕМЕНТА======'''
# my_list['isa']= 'harosh'
# print(my_list)

'''========= МЕТОДЫ =========='''

# get(key,None) -> ДАЕТ ЗНАЧЕНИЕ ИЗ СЛОВАРЯ (ЕСЛИ НЕТ ТО (NONE))

# dict_ = {2:'isa',1:'ni',3:'uu'}
# print(dict_.get(1))

# clear() -> ОЧИЩАЕТ СЛОВАРЬ 

# my_dict = {1:'f', 2:'r'}
# my_dict.clear()
# print(my_dict)

# copy -> СОЗДАЕТ КОПИЮ СЛОВАРЯ
# my_dict = {1:'tom',2:'bella',3:'era'}
# my_dict2 = my_dict.copy()
# print(my_dict2)

# pop(key,default) -> УДАЛИТЬ ЗНАЧЕНИЕ ПО КЛЮЧУ
# my_dict = {1:'tom',2:'bella',3:'era'}
# my_dict.pop(1, 'no such key')
# print(my_dict)

# popitem() -> УДАЛИТЬ ПОСЛЕДНЕЕ ЗНАЧЕНИЕ
# my_dict = {1:'tom',2:'bella',3:'era'}
# my_dict.popitem()
# print(my_dict)

# setdefault(key, default) -> ВЫВЕДИ ЗНАЧЕНИЕ А ЕСЛИ НЕТ ТО ДОБАВЬ
# dict_ = dict(a = 1, b = 2, c = 3)
# print(dict_.setdefault('a', 5))
# print(dict_)

# update() -> ДЕЛАЕТ ИЗ 2 СЛОВАРЕЙ 1
# my_dict = {1:'tom',2:'bella',3:'era'}
# my_dict1 = {1:'tom',2:'bella',4:'eba'}
# my_dict.update(my_dict1)
# print(my_dict)

# fromkeys(seq, value) -> 
# numbers = [1,2,3,4,5]
# new_dict = dict.fromkeys(numbers,'juma')
# print(new_dict)

'''====== Методы словарей ======'''
# items(), keys(), values()
# contacts = {
#     'iskhak':'123456789',
#     'beka':'123456789',
#     'juma':'987654321'
# }
# for key in contacts.keys():
#     print(key)


# 1
# a = {'x': 1, 'y': 2, 'z': 1}
# b = list(a.keys())
# c = b[0]
# print(c)

# 2
# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.pop('a')
# print(b)

# 3
# a = {'a': 1, 'b': 2, 'c': 1}
# a['f'] = 55
# print(a)

# 4
# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

# 5
# a = {'a': 1, 'b': 2, 'c': 1}
# b = list(a.keys())
# print(b)

# 6 eazy

# 7
# a = {'a': 1, 'b': 2, 'c': 1}
# for key in a.keys():
#     print(key)

# 8
# a = {'a': 1, 'b': 2, 'c': 1}
# for values in a.values():
#     print(values)

# 9
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {}
# for k,v in a.items():
#     if v % 2 ==0:
#         v = 2 
#         b[k]=v
#     else:
#         b[k]=v
# print(b)

# 10


# 11
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# for k,v in a.items():
#     d = v / 5
#     a[k]= d
# print(a)
    
# 12
# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# list_=[]
# for key,value in a.items():
#     if value % 2 == 0:
#         list_.append(key)
# for i in list_:
#     a.pop(i)
# print(a)

# 13
# a = {'a': 1, 'b': 2, 'c': 3} 
# b = {}
# for k,v in a.items():
#     b[v] = k
# print(b)

# 14
# a = {'a': 3, 'b': 2}
# s = 0
# for v in a.values():
#     s+=v
# print(s)

# 15

# a1 ={'a':3}
# a2 =dict(a = 8)
# a3 = {} 
# for k,v in a1.items(): 
#     a3.setdefault(k, v) 
# print(a1) 
# print(a2) 
# print(a3)

# 17
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# for k,v in dict_.items():
#     if v == v:
#         v = 0
#         print(v)

# dict_ = {'a': 1, 'b': 2, 'c': 1}
# dict_item = dict[dict_]
# print(dict_item)

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# for k,v in dict_.items:
#     if k[0] > k[1]:
#         print(k)

dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21} 
print(max(dict_.values()))