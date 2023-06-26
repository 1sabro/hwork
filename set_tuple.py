''' Метод ADD'''

# guests = {'isa', 'beka', 'esen'}
# guests.add('yiman')
# print(guests)

'''Метод UPDATE'''
# makers1 = {1,2,3,4,5}
# makers2 = {6,7,8,9}
# makers1.update(makers2)
# print(makers1)

''' Метод remove '''''' Метод discard без ошибок'''''' Метод pop рандом'''
# guests = {'amin', 'beka', 'isa', 'esen'}
# guests.remove('isa')
# print(guests)

''' Метод Intersection &'''
# a = {'isa', 'yiman'}
# b = {'isa', 'esen'}
# print(a.intersection(b))

''' Метод Union | '''
# a = {'isa', 'yiman'}
# b = {'isa', 'esen'}
# print(a.union(b))

''' Метод Difference'''
# a = {'isa', 'yiman'}
# b = {'isa', 'esen'}
# print(a.difference(b))

''' Метод Symmetric Difference'''
# a = {'isa', 'yiman'}
# b = {'isa', 'esen'}
# print(a.symmetric_difference(b))

''' Метод isdisjoint'''
# num1 = {1,2,3,4,5}
# num2 = {6,7,8,9,10}
# print(num1.isdisjoint(num2))

''' Метод intersection_update '''
# num1 = {1,2,3,4,5,6,7,8}
# num2 = {6,7,8,9,10}
# num1.intersection_update(num2)
# print(num1)

'''issuperset, issubset'''
'''===================TUPLE======================'''
'''count'''
# my_tuple = (1,2,3,2,2,4)
# print(my_tuple.count(2))
'''index'''
# my_tuple = ('isa','bed', 'amin', 'tee')
# print(my_tuple.index('amin'))

# len(), max(), min(), sum()
# a = (1,2,3,4,5,6,7,8,9)
# print(len(a))
# print(max(a))
# print(min(a))
# print(sum(a))

# my_tuple = (1,True,['isa','esen'])
# my_tuple[2][0] = 'no'
# print(my_tuple)

# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}
# if robert.intersection(kail) and robert.intersection(merri):
#     print('kail merri')
# elif robert.intersection(merri):
#     print('merry')
# elif robert.intersection(kail):
#     print('kail')
# else:
#     print('no one')

# tilek = {'Dodo', 'ImperiaPizza', 'FreshBox'}
# timur = {'OchakKebap', 'FreshBox'}
# alexandr = {'FreshBox', 'KFC'}
# elina = set()
# print(tilek&timur&alexandr)

ingredients = {"cыр чеддар","грибы", "соус","шпинат"}
ingredients.add('помидор')
ingredients.discard('колбаса')
ingredients.remove('шпинат')
ingredients.add('базилик')
ingredients.discard('сыр чеддар')
ingredients.add('сыр моцарелла')
print(ingredients)