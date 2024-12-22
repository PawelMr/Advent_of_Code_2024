import copy
import re
import collections
from heapq import heappush, heappop
import time


with open("input.txt", mode="r", encoding="utf-8") as test_file:
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

def pars_2_kl_22222(ldc):
    stro = ""
    for dc in ldc:
        dx = dc[0]
        dy = dc[1]
        strx = "<" * -dx + ">" * dx
        stry = "^" * -dy + "v" * dy
        stro += strx + stry + "A" if dy < 0 and dx < 0 else stry + strx + "A"
    return stro

def pars_2_kl(source, target, kl = kl1):
    minx, maxx, miny, maxy = (0, 3, 0, 3) if kl == kl1 else (0, 3, -1, 0)
    tx,ty = target
    sx,sy = source
    dx = tx - sx
    dy = ty - sy
    vert = "v"*dx+"^"*-dx
    horiz = ">"*dy+"<"*-dy
    if dy > 0 and minx<=tx<=maxx and miny<=sy<=maxy:
        return vert+horiz+"A"
    if minx<=sx<=maxx and miny<=ty<=maxy:
        return horiz+vert+"A"
    if minx<=tx<=maxx and miny<=sy<=maxy:
        return vert+horiz+"A"

def delta_c(coordinates, kl= kl1):
    nkl = ""
    for i in range(1, len(coordinates)):
        if coordinates[i - 1] == coordinates[i]:
            nkl+="A"
        else:
            try:
                nkl += pars_2_kl(coordinates[i - 1],coordinates[i], kl)
            except:
                print()
                pars_2_kl(coordinates[i - 1], coordinates[i], kl)

    return nkl

def rough_score(txts)     :
    c = parse_string_in_c(txts)
    k = delta_c(c)

    c2 = parse_string_in_c(k,kl2)
    k2 = delta_c(c2,kl2)

    c3 = parse_string_in_c(k2,kl2)
    k3 = delta_c(c3,kl2)

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








