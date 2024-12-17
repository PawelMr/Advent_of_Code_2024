import copy
import re
import collections



with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()

def disassemble_into_numbers(string):
    pattern = r'(\d+)'
    number_txt_list = re.findall(pattern, string)
    number_list = [int(i) for i in number_txt_list]
    return number_list

def back_from_addition(a,b):
    return a-b if a-b>0 else False

def back_from_multiplication(a,b):
    z = a//b
    return z if b * z == a else False

def back_from_concordance(a,b):
    if str(a).endswith(str(b)):
        z = str(a).rsplit(str(b),1)[0]
        return int(z) if z else 0
    else:
        return False

def choosing_operator(a,b, concordance= False):
    list_result = []
    z = back_from_addition(a,b)
    x = back_from_multiplication(a,b)
    if z:
        list_result.append((z,"+"))
    if x:
        list_result.append((x, "*"))
    if concordance:
        y = back_from_concordance(a,b)
        if y:
            list_result.append((y, "||"))
    return list_result

def brute_force_of_operators(tuple_values,concordance= False):
    list_result = [tuple_values[0]]
    list_numbers = tuple_values[:0:-1]
    for b in list_numbers:
        new_list_result = []
        while list_result:
            one_branch = choosing_operator(list_result.pop(-1),b,concordance=concordance)
            new_list_result.extend([i[0] for i in one_branch])
        list_result = new_list_result
        if not list_result:
            break
    right_result = [i for i in list_result if i == 1 or i == 0]
    return bool(right_result)

import time
time_start = time.time()

initial_data = tuple(tuple(disassemble_into_numbers(i)) for i in list_txt)
list_right_data = [q for q in initial_data if brute_force_of_operators(q)]
sum_test = sum([i[0] for i in list_right_data])

time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum_test} \n Время Решения:{execution_time}")


import time
time_start = time.time()

initial_data = tuple(tuple(disassemble_into_numbers(i)) for i in list_txt)
list_right_data = [q for q in initial_data if brute_force_of_operators(q, concordance=True)]
sum_test = sum([i[0] for i in list_right_data])

time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum_test} \n Время Решения:{execution_time}")