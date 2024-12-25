import copy
import re
import collections
from heapq import heappush, heappop
import time


with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]

kl1 = "789456123X0A"
kl2 = "X^A<v>"

# ckl = {
#     ">": (0, 1),
#     "<": (0, -1),
#     "^": (-1, 0),
#     "v": (1, 0)
# }
#
# klc = {
#     (0, 1): ">",
#     (0, -1): "<",
#     (-1, 0): "^",
#     (1, 0): "v"
# }


def disassemble_into_numbers(string):
    pattern = r'(\d+)'
    number_txt_list = re.findall(pattern, string)
    number_list = [int(i) for i in number_txt_list]
    return number_list


def parse_string_in_c(cod: str, kl = kl1):
    # list_baton = cod.split()
    kls = (2, 3) if kl==kl1 else (2,0)
    list_c = [kls]
    for symbol in cod:
        ind = kl.index(symbol)
        y = ind // 3
        x = ind % 3

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
    null = (0,3) if kl==kl1 else (0,0)
    tx,ty = target
    sx,sy = source
    dx = tx - sx
    dy = ty - sy
    horiz = ">"*dx+"<"*-dx
    vert = "v"*dy+"^"*-dy
    if dx<0 and (tx,sy) != null:
        return horiz+vert+ "A"
    elif dy > 0 and (sx,ty)!=null:
        return vert + horiz + "A"
    elif (sx,ty)!=null:
        return vert + horiz + "A"
    elif dx>0 and (tx,sy) != null:
        return horiz+vert+ "A"

    else:
        raise Exception("ХРЕНЬ")



def delta_c(coordinates, kl= kl2):
    nkl = ""
    for i in range(1, len(coordinates)):
        if coordinates[i - 1] == coordinates[i]:
            nkl+="A"
        else:
            # try:
                nkl += pars_2_kl(coordinates[i - 1],coordinates[i], kl)
            # except:
            #     print()
            #     pars_2_kl(coordinates[i - 1], coordinates[i], kl)

    return nkl

def rough_score(txts, lenp = 2)     :
    c = parse_string_in_c(txts)
    k = delta_c(c, kl1)

    for i in range(lenp):
        c = parse_string_in_c(k, kl2)
        k = delta_c(c, kl2)
    # c2 = parse_string_in_c(k,kl2)
    # k2 = delta_c(c2,kl2)
    #
    # c3 = parse_string_in_c(k2,kl2)
    # k3 = delta_c(c3,kl2)

    return len(k)* disassemble_into_numbers(txts)[0]

time_start = time.time()
s = sum([rough_score(i) for i in list_txt])
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {s} \n Время Решения:{execution_time}")



def pars_kl(lkl):
    list_kl = [i+"A" for i in lkl.split("A")[:-1]]
    return list_kl


cache_transition = {}
def rough_score_2(txts, lenp = 2)     :
    c = parse_string_in_c(txts)
    k = delta_c(c, kl1)

    ck = collections.Counter([k])
    for i in range(lenp+1):
        new_ck = collections.Counter()
        for kn, count in ck.items():
            cn = parse_string_in_c(kn, kl2)
            k_str = delta_c(cn, kl2)
            list_n_k = pars_kl(k_str)
            step_count = collections.Counter(list_n_k)
            # cache_transition.update({kn:list_n_k})


            for k in step_count:
                step_count[k] *= count
            new_ck.update(step_count)
        ck = new_ck
    return sum(ck.values())* disassemble_into_numbers(txts)[0]


    # c2 = parse_string_in_c(k,kl2)
    # k2 = delta_c(c2,kl2)

    return 0


time_start = time.time()
# rough_score_2(list_txt[0])
s = sum([rough_score_2(z, 25) for z in list_txt])
time_finish = time.time()
execution_time = time_finish - time_start

print(f"Решение задания 2: {s} \n Время Решения:{execution_time}")








