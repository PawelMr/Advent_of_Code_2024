import copy
import re
import collections
from heapq import heappush, heappop
import time


with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]

def disassemble_into(string):
    pattern = r'(\w+)'
    number_txt_list = re.findall(pattern, string)
    return number_txt_list

def get_graf(list_lpk):
    dict_s ={}
    for two_pk in list_lpk:
        for i in range(2):
            if dict_s.get(two_pk[i]):
                dict_s[two_pk[i]].append(two_pk[i-1])
            else:
                dict_s[two_pk[i]]= [two_pk[i - 1]]
    return dict_s

def get_group(dict_s:dict):
    ful_group = []
    for key, value in dict_s.items():
        if key.startswith('t'):
            for i in range(len(value)-1):
                for i2 in range(i+1, len(value)):
                    if value[i] in dict_s[value[i2]]:
                        if {key,value[i], value[i2]} not in ful_group:
                            ful_group.append({key,value[i], value[i2]})

    return ful_group

input_data = [disassemble_into(i) for i in list_txt]
graf = get_graf(input_data)

time_start = time.time()
group_t = get_group(graf)
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {len(group_t)} \n Время Решения:{execution_time}")


def get_max_group(dict_s:dict):
    ful_group = []
    for key, value in dict_s.items():
        if key == 'ta':
            print()
        if key.startswith('t'):
            group = {key} | set(value)
            for i in value:
                group = group & (set(dict_s[i]) | {i})
                for j in group:
                    group = group & (set(dict_s[j]) | {j})
                if group not in ful_group:
                    ful_group.append(group)
    return ful_group



time_start = time.time()

o_group = get_max_group(graf)
parol = ",".join(sorted(list(sorted(o_group, key =lambda x: len(x), reverse=True)[0])))
time_finish = time.time()
execution_time = time_finish - time_start

print(f"Решение задания 2: {parol} \n Время Решения:{execution_time}")








