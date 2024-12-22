import copy
import re
import collections
from heapq import heappush, heappop
import time


with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]


def op_1(sn):
    nsn = sn * 64
    nsn = nsn ^ sn
    return nsn % 16777216


def op_2(sn):
    nsn = int(sn / 32)
    nsn = nsn ^ sn
    return nsn % 16777216


def op_3(sn):
    nsn = sn * 2048
    nsn = nsn ^ sn
    return nsn % 16777216


def get_new_number(sn):
    return op_3(op_2(op_1(sn)))


def get_list_new_number_t2(sn, len_n):
    list_nn = [sn]
    list_nn.extend([sn := get_new_number(sn) for i in range(len_n-1)])
    list_nn = [i%10 for i in list_nn]
    dl = get_delta(list_nn)
    dict_r={}
    for i in range(3,len(dl)):
        if not dict_r.get((dl[i-3],dl[i-2],dl[i-1],dl[i])):
            dict_r.update({(dl[i-3],dl[i-2],dl[i-1],dl[i]):list_nn[i+1]})
    # dict_r = {(dl[i-3],dl[i-2],dl[i-1],dl[i]):list_nn[i+1] for i in range(3,len(dl)) }
    return dict_r


def get_delta(listn):
    ld = [listn[i] - listn[i-1] for i in range(1, len(listn))]
    return ld

def get_new_number_n_st(sn, count_n):
    for i in range(count_n):
        sn = get_new_number(sn)
    return sn

time_start = time.time()
n_l = [get_new_number_n_st(int(i), 2000) for i in list_txt]
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum(n_l)} \n Время Решения:{execution_time}")


def get_max(ldd):
    od = []
    set_key = set()
    [set_key := set_key | set(d.keys()) for d in ldd]
    for key in set_key:
        if key == (-2, 1, -1, 3):
            print()
        list_sum = [d.get(key, 0) for d in ldd]
        od.append(sum(list_sum))
    return max(od)


time_start = time.time()
ld_l = [get_list_new_number_t2(int(i), 2000) for i in list_txt]

max_s = get_max(ld_l)
time_finish = time.time()
execution_time = time_finish - time_start

print(f"Решение задания 2: {max_s} \n Время Решения:{execution_time}")








