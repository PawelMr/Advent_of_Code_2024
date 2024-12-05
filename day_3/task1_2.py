import copy
import re
import collections


with open("input_2.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()

def parser_str(str_element):
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", str_element)
    return matches

def parser_str_2(str_element):
    matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", str_element)
    return matches

def disassemble_into_numbers(string):
    pattern = r'(\d+)'
    number_txt_list = re.findall(pattern, string)
    number_list = [int(i) for i in number_txt_list]
    return number_list

list_mul = []
for str_txt in list_txt:
    list_mul.extend(parser_str(str_txt))
list_two_num = []
for one_mul in list_mul:
    list_two_num.append(disassemble_into_numbers(one_mul))
sum_mul = 0
for i in list_two_num:
    sum_mul  += i[0]*i[1]
print(f"Решение задания 1: {sum_mul}")

import time
time_start = time.time()

list_mul = []
for str_txt in list_txt:
    list_mul.extend(parser_str_2(str_txt))
list_two_num = []
for one_mul in list_mul:
    list_two_num.append(one_mul if "do" in one_mul else disassemble_into_numbers(one_mul))
sum_mul = 0
enable_flag = True
for i in list_two_num:
    if enable_flag and i == "don't()":
        enable_flag = False
    if not enable_flag and i == "do()":
        enable_flag = True
    if enable_flag and isinstance(i, list):
        sum_mul  += i[0]*i[1]
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 2: {sum_mul} \n Время Решения:{execution_time}")



