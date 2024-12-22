import copy
import re
import collections
from heapq import heappush, heappop
import time


with open("test.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]

kl1 = "A0X321654987"
kl2 = "A^X>v<"

ckl = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}

klc = {
    (0, 1): ">",
    (0, -1): "<",
    (-1, 0): "^",
    (1, 0): "v"
}


def disassemble_into_numbers(string):
    pattern = r'(\d+)'
    number_txt_list = re.findall(pattern, string)
    number_list = [int(i) for i in number_txt_list]
    return number_list


def parse_string_in_c(cod: str, kl = kl1):
    # list_baton = cod.split()
    list_c = [(0,0)]
    for symbol in cod:
        ind = kl.index(symbol)
        y = ind // 3
        x = ind % 3
        if kl==kl2:
            y*=-1
        list_c.append((x, y))
    return list_c

def pars_2_kl(ldc):
    stro = ""
    for dc in ldc:
        dx = dc[0]
        dy = dc[1]
        if dx>0:
            strx = ">"*dx
        else:
            strx = "<" * (-1*dx)
        if dy>0:
            stry = "v"*dy
        else:
            stry = "^" * (-1*dy)
        stro +=strx+stry+ "A"
    return stro

def delta_c(coordinates):
    list_d = []
    for i in range(1, len(coordinates)):
        dx = coordinates[i - 1][0] - coordinates[i][0]
        dy = coordinates[i - 1][1] - coordinates[i][1]
        list_d.append((dx, dy))
    return(list_d)

def rough_score(txts)     :
    c = parse_string_in_c(txts)
    sd = delta_c(c)
    k = pars_2_kl(sd)
    c2 = parse_string_in_c(k,kl2)
    sd2 = delta_c(c2)
    k2 = pars_2_kl(sd2)
    c3 = parse_string_in_c(k2,kl2)
    sd3 = delta_c(c3)
    k3 = pars_2_kl(sd3)
    return len(k3)* disassemble_into_numbers(txts)[0]

time_start = time.time()
s = sum([rough_score(i) for i in list_txt])
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {s} \n Время Решения:{execution_time}")



time_start = time.time()


time_finish = time.time()
execution_time = time_finish - time_start

print(f"Решение задания 2: {0} \n Время Решения:{execution_time}")








