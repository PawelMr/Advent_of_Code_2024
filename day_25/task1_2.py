import copy
import re
import collections
from heapq import heappush, heappop
import time


with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]


def count_pins(list_string):
    list_height = [-1 for _ in range(len(list_string[0]))]
    for str_y in list_string:
        for x,v in enumerate(str_y):
            if v == "#":
                list_height[x]+=1
    return list_height

def parse_data(list_string):
    s_i = 0
    f_i = 0
    list_key = []
    list_lock = []
    while not f_i is None:
        if list_string[s_i:].count(""):
            f_i = list_string[s_i:].index("")+s_i
        else:
            f_i = None
        height_pins = count_pins(list_string[s_i:f_i])
        if list_string[s_i][0] == "#":
            list_lock.append(height_pins)
        else:
            list_key.append(height_pins)
        s_i = f_i+1 if f_i else None
    return list_key, list_lock


def check_lock(l,k):
    v = 5
    check_k = True
    for i in range(len(l)):
        if l[i]+k[i] > v:
            check_k = False
    return check_k




lk, ll = parse_data(list_txt)

time_start = time.time()
sum_v = 0
for ill in ll:
    for ilk in lk:
        if check_lock(ill,ilk):
            sum_v+=1

time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum_v} \n Время Решения:{execution_time}")







time_start = time.time()


time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 2: {0} \n Время Решения:{execution_time}")








