# 1.Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4
num = [2, 3, 5, 6, 9, 5, 10]
sum = 0
for i in range (len(num)):
    if i % 2 == 0:
        sum += num[i]
print (sum)


# 2.Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
numbers = [1, 8, 9, -4, 5]
result = []
res_list = len(numbers)//2 if len(numbers)%2 == 0 else len(numbers)//2+1
for i in range(res_list):
    result.append(numbers[i]*numbers[len(numbers)-i-1])
print (result)


# 3.В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
from decimal import Decimal

num_list = [1.2, 1.3, 6.5, 5.6, 5.3]
result_n = 0
decimal_num_list = list(map(Decimal, num_list))
def min_dec_num_list (num_list):  
    min_num = decimal_num_list[0] - math.floor(decimal_num_list[0])
    for i in range(len(num_list)):
        min_dec = decimal_num_list[i] - math.floor(decimal_num_list[i])
        if min_dec < min_num:
            min_num = min_dec   
    return min_num
def max_dec_num_list (num_list):
    max_num = decimal_num_list[0] - math.floor(decimal_num_list[0])
    for i in range(len(num_list)):
        max_dec = decimal_num_list[i] - math.floor(decimal_num_list[i])
        if max_dec > max_num:
            max_num = max_dec   
    return max_num
result_n = max_dec_num_list(num_list) - min_dec_num_list(num_list)
print ((round(result_n, 1)))


# 4.Написать программу преобразования десятичного числа в двоичное
numb = 96
binary = ''
while numb != 0:
    binary = str(numb % 2) + binary
    numb = numb // 2
print (binary)
