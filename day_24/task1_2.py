import copy
import re
import collections
from heapq import heappush, heappop
import time


with open("input3.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]

def disassemble_into(string):
    pattern = r'(\d+)'
    number_txt_list = re.findall(pattern, string)
    return int(number_txt_list[0])

def sel_op(txt):
    if txt == "AND":
        return get_and
    if txt == "OR":
        return get_or
    if txt == "XOR":
        return get_xor

def get_and(a,b): return a & b

def get_or(a,b): return a | b

def get_xor(a,b): return a ^ b

def parse_input(list_str):
    i_r = list_str.index("")
    inp_number = list_str[:i_r]
    inp_quit = list_str[i_r+1:]
    dict_inp_num = {i.split(":")[0]:disassemble_into(i.split(":")[1]) for i in inp_number}
    dict_quit_fun = {i.split(" -> ")[-1]:[i.split()[0],i.split()[2], sel_op(i.split()[1])] for i in inp_quit}
    return dict_inp_num, dict_quit_fun

def search_target_zn(dict_quit_fun, lit = "z"):
    set_target_value = [i for i in dict_quit_fun if i.startswith(lit)]
    return set_target_value
d_z, d_f = parse_input(list_txt)

def get_quit_value(dict_num_in: dict, dict_fun: dict):
    dn = copy.copy(dict_num_in)
    set_target = set(search_target_zn(dict_fun))
    new_set_target = set()
    while set_target or new_set_target:
        tr = set_target.pop()
        if not set_target:
            set_target = new_set_target
        if not dn.get(tr) is None:
            continue
        f_zn = dict_fun[tr]
        if (not dn.get(f_zn[0]) is None) and (not dn.get(f_zn[1]) is None):
            dn.update({tr:f_zn[2](dn[f_zn[0]], dn[f_zn[1]])})
            continue
        if not dn.get(f_zn[0]):
            set_target.add(f_zn[0])
        if not dn.get(f_zn[1]):
            set_target.add(f_zn[1])
        new_set_target.add(tr)

    return dn





time_start = time.time()

dr = get_quit_value(d_z, d_f )
otv = sorted([(key, value) for key, value in dr.items() if key.startswith("z")], key = lambda x:x[0], reverse=True)
otv = [str(i[1])for i in otv]
otv = "".join(otv)
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {int(otv, 2)} \n Время Решения:{execution_time}")





# def parse_input_funk(list_str):
#     i_r = list_str.index("")
#
#     inp_quit = list_str[i_r+1:]
#
#     dict_quit_fun = {i.split(" -> ")[-1]:i.split(" ")[0:3] for i in inp_quit}
#     return dict_quit_fun


time_start = time.time()

# df_os = parse_input_funk(list_txt)
# d_f_z = {key: value for key, value in df_os.items() if key.startswith("z")}
def get_variant(var,k, sn):
    if k.endswith(sn):
        if k[0] == "x":
            return var[0]
        else:
            return var[1]
    else:
        return 0

for number in range(45):
    str_number = str(number)
    str_number =  str_number.zfill(2)
    list_variant = [(0,1),(1,0),(1,1)]
    for variant in list_variant:
        d_z_n ={key: get_variant(variant,key,str_number) for key, value in d_z.items()}
        dr = get_quit_value(d_z_n, d_f )
        otv = sorted([(key, value) for key, value in dr.items() if key.startswith("z")], key = lambda x:x[0], reverse=True)
        otv = [str(i[1])for i in otv]
        otv = "".join(otv)
        print(f"знак {str_number} вариант {variant} результат {otv} ")


time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 2: {0} \n Время Решения:{execution_time}")








