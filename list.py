
'''====================================================================
append(item): добавляет элемент item в конец списка

insert(index, item): добавляет элемент item в список по индексу index

remove(item): удаляет элемент item. 
Удаляется только первое вхождение элемента. 
Если элемент не найден, генерирует исключение ValueError

clear(): удаление всех элементов из списка

index(item): возвращает индекс элемента item. 
Если элемент не найден, генерирует исключение ValueError * pop([index]): 
удаляет и возвращает элемент по индексу index. Если индекс не передан, 
то просто удаляет последний элемент.

count(item): возвращает количество вхождений элемента item в список

sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. 
но  помощью параметра key мы можем передать функцию сортировки.

reverse(): расставляет все элементы в списке в обратном порядке

====Кроме того, Python предоставляет ряд встроенных функций для работы в списках:====

len(list): возвращает длину списка

sorted(list, [key]): возвращает отсортированный список

min(list): возвращает наименьший элемент списка

max(list): возвращает наибольший элемент списка
======================================================================='''

# lists = [[1, 2, 3], [5, 75, 543, 23, 634], [-253, -523, 76, 5, 8, 0]]
# b = 0
# for i in lists:
#     if len(lists[b]) > len(lists[b+1]):
#         print(lists[b])
#     else:
#         b += 1
        
# lists = [[1, 2, 3,2,3,4,5,5], [5, 75, 543, 23, 634], [-253, -523, 76, 5, 8, 0]]
# for i in lists:
#     if len(lists[0]) > len(lists[1]):
#         print(lists[i])


list_ = [1, 2, 3]
print(list_.get(1))