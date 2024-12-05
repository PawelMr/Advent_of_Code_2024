import copy
import re
import collections


with open("input_2.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()

print()


def disassemble_into_numbers(string):
    pattern = r'(\d+)'
    number_txt_list = re.findall(pattern, string)
    number_list = [int(i) for i in number_txt_list]
    return number_list


def check_growth_decreasing_list(array, growth=True):
    fn_growth = lambda x, y: x < y
    fn_decreasing = lambda x, y: x > y
    fn = fn_growth if growth else fn_decreasing
    return all([fn(x, y) for x, y in zip(array[:-1], array[1:])])


def get_min_max_difference(array):
    list_difference = [abs(x - y) for x, y in zip(array[:-1], array[1:])]
    return min(list_difference), max(list_difference)


list_string_int = [disassemble_into_numbers(txt) for txt in list_txt]
list_growing_str_int = [i for i in list_string_int if check_growth_decreasing_list(i) or
                        check_growth_decreasing_list(i, False)]
list_result = [i for i in list_growing_str_int if
               get_min_max_difference(i)[0] >= 1 and get_min_max_difference(i)[1] <= 3]

print(f"Решение задания 1: {len(list_result)}")

import time
time_start = time.time()
def check_report_in_difference(array):
    list_difference = [x - y for x, y in zip(array[:-1], array[1:])]
    list_bool_growth = [ 1 <= i <= 3 for i in list_difference]
    list_bool_decreasing = [-3 <= i <= -1 for i in list_difference]
    return all(list_bool_growth) or all(list_bool_decreasing)

list_result = []
for str_int in list_string_int:
    if check_report_in_difference(str_int):
        list_result.append(str_int)
    else:
        for index, value in enumerate(str_int):
            copy_str_int = copy.copy(str_int)
            copy_str_int.pop(index)
            if check_report_in_difference(copy_str_int):
                list_result.append(str_int)
                break

time_finish = time.time()
execution_time = time_finish - time_start
# check_report_in_dampener([1, 2, 7, 8, 9])
# list_result = [i for i in list_string_int if check_report_in_dampener(i)]
print(f"Решение задания 2: {len(list_result)} \n Время Решения:{execution_time}")

import time
time_start = time.time()
def check_dampener(list_difference,list_bool,fn):
    if list_bool.count(False) == 1 and (list_bool.index(False) == 0 or list_bool.index(False) == len(list_bool)-1):
        return True
    if list_bool.count(False) == 1:
        index_false = list_bool.index(False)
        return (fn(list_difference[index_false] + list_difference[index_false+1]) or
                fn(list_difference[index_false-1]  + list_difference[index_false]))
    if list_bool.count(False) == 2:
        index_false = [i for i, z in enumerate(list_bool) if not z]
        if index_false[1]-index_false[0] == 1:
            return fn(list_difference[index_false[0]]+list_difference[index_false[1]])
    else:
        return False

def check_report_in_difference_dampener(array):
    list_difference = [y - x for x, y in zip(array[:-1], array[1:])]
    fn_growth = lambda x: 1 <= x <= 3
    fn_decreasing = lambda x: -3 <= x <= -1
    list_bool_growth = [ fn_growth(i) for i in list_difference]
    list_bool_decreasing = [fn_decreasing(i) for i in list_difference]
    if all(list_bool_growth) or all(list_bool_decreasing):
        return True
    if list_bool_growth.count(False) < list_bool_decreasing.count(False):
        list_bool = list_bool_growth
        fn = fn_growth
    else:
        list_bool = list_bool_decreasing
        fn = fn_decreasing
    return check_dampener(list_difference,list_bool,fn)

list_result1 = []
for str_int in list_string_int:
    if check_report_in_difference_dampener(str_int):
        list_result1.append(str_int)

time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 2: {len(list_result1)} \n Время Решения:{execution_time}")
