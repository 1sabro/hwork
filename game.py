#задача 1 ->1 point
# a=0
# b=2
# c=5
# a,b,c = a+b, c-b, a+b+c
# print(a,b,c)

# 2 -----> 1 point
# a = int(input(': '))
# def func(a):
#     per = a*4
#     plo = a ** 2
#     di = a*(a**0.5)
#     return per,plo,di
# print(func(5))

# 3 ----> 1 point
# a = int(input())
# b = str(a)
# c = [i for (i) in b]
# d = 'no'

# if c[0]<c[1]:
#     if c[1]<c[2]:
#         if c[2]<c[3]:
#             d = 'yes'
# print(d)

# 5 -> 0
# a = '1234'
# b = a[-1]+'23'+a[0]
# print(b)

#4 --> 0,5

# for i in range(10000, 100000):
#     r = str(i)
#     s = [int(i) for i in r]
#     w = sum(s)
    
#     if i %2 ==0:
#         if s[2] != 0:
#             if w % 4 ==0:
#                 print(i)
    
# 8 -> 0,5
# for i in range (1,51):
#     if i %3 ==0:
#         print(i,'Fizz')
#     elif i % 5 ==0:
#         print(i,'Buzz')
#     if i % 3 ==0 and i % 5 ==0:
#         print(i,'FizzBuzz')
# 7 -> 1
# a = int(input("сколько кг"))
# cost = 20
# print('кг',a*cost)
# b = int(input('сколько руб'))
# c = 20
# print('руб',b/c)

# 6 -> 0 points
# geo_logo = [{'visit2:'['Delfi', 'india']}, {'visit3':['vl','ross']},{'visit9':['kur','ross']}]
# new = []
# for i in geo_logo:
#     for k,v in i.items():
#         print(v)
