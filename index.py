# list = [10,20,30,40,50]
# print(list[::-1])

# newList = []
# list = [10,20,30,40,50]
# for i in range(len(list) -1, -1, -1):
#    newList.append(list[i])
# print(newList)

# newList = []
# list = [10,20,30,40,50]
# for num in list[::-1]:
#    newList.append(num)
# print(newList)

# nums = [10,20,30,40,50,60,70,80,90]
# def myFilter(list):
#     Filtered_nums = []
#     for num in list:
#         if num <= 50:
#             Filtered_nums.append(num)
#     print(myFilter([10,20,30,40,50,60,70,80,90], 50))

# def calculator(func, a, b):
#     return func(a, b)

# def add(a, b):
#     return(a + b)

# def devide(a, b):
#     return(a / b)

# def subtrct(a, b):
#     return(a - b)

# def multiply(a, b):
#     return(a * b)

# print(calculator(add, 2, 3))
# print(calculator(devide, 10, 2))
# print(calculator(subtrct, 10, 2))
# print(calculator(multiply, 10, 2))

# def sum_numbs(text: str):
#     acc = 0
#     list = text.split(' ')
#     for word in list:
#         if word.isdigit():
#             acc += int(word)
#     return acc
# print(sum_numbs('hello 11 '))

def chekio(abc):
    sum = 0
    for i in range(0, len(abc), 2):
        sum += abc[i]
    return sum * abc[-1] if abc else 0
print(chekio([0,1,2,3,4,5]))
print(chekio([1,3,5]))
print(chekio([6]))
print(chekio([]))