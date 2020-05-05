"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный).
Определите, есть ли в списке число, которое является индексом элемента "odd".
Напишите функцию, которая будет возвращать True или False, соответсвенно.
"""
# Мое решение.
def odd_ball(arr):
    index_number = arr.index("odd")
    if index_number in arr:
        return True
    else: return False

# Решение учителя
def odd_ball(arr):
    return arr.index('odd') in arr

print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"])) # True
print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"])) # False
print(odd_ball(["even",10,"odd",2,"even"])) # True



"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности 
включительно. 
Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. 
Попробуйте решить задачу двумя способами (один из способов в одну строчку кода).
"""
# Мое решение.
def find_sum(n):
    array = [i for i in range(1, n+1) if i % 3 == 0 or i % 5 == 0]
    print(sum(array))

find_sum(5) # return 8 (3 + 5)
find_sum(10) # return 33 (3 + 5 + 6 + 9 + 10)

# Решение учителя 1.
def find_sum(n):
    res = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res

print(find_sum(5)) # return 8 (3 + 5)
print(find_sum(10)) # return 33 (3 + 5 + 6 + 9 + 10)

# Решение учителя 2.
def find_sum2(n):
    return sum(i for i in range(1, n+1) if i % 3 == 0 or i % 5 == 0)

print(find_sum2(5)) # return 8 (3 + 5)
print(find_sum2(10)) # return 33 (3 + 5 + 6 + 9 + 10)

"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""

# Мое решение.
def get_names(names):
    list = []
    for n in names:
        if len(n) == 4:
            list.append(n)
    return list

names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
print(get_names(names), end=" ")

print("-------------")

# Решение учителя
def get_names2(names):
    return [i for i in names if len(i) == 4]

names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
print(get_names2(names), end=" ")