import copy
import re
import collections



with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()

def disassemble_into_numbers(string):
    pattern = r'(\w)'
    number_txt_list = re.findall(pattern, string)
    number_list = [i for i in number_txt_list]
    return number_list

def get_symbol_coordinates(list_str):
    dict_symbol = {}
    for  y,str_value in enumerate(list_str):
        for x, symbol in enumerate(str_value):
            if symbol.isalnum():
                if dict_symbol.get(symbol):
                    dict_symbol[symbol].append((x,y),)
                else:
                    dict_symbol.update({symbol:[(x,y),]})
    return dict_symbol

def get_antinode(xy1, xy2, k = 1):
    xr = xy2[0] - xy1[0]
    yr = xy2[1] - xy1[1]
    xy3 = (xy1[0] - xr*k, xy1[1] - yr*k)
    xy4 = (xy2[0] + xr*k, xy2[1] + yr*k)
    return [xy3, xy4]

def get_ful_antinode_one_antenna(list_coordinate, m_x,m_y, one = True):
    list_antinode = []
    for index, xy1 in enumerate(list_coordinate):
        for xy2 in list_coordinate[index+1:]:
            if one:
                new_antinode = get_antinode(xy1, xy2)
                new_antinode = [i for i in new_antinode if 0<=i[0]<=m_x and 0<=i[1]<=m_y]
            else:
                n_k = 0
                new_antinode = []
                while True:
                    new_one_antinode = get_antinode(xy1, xy2, k = n_k)
                    if (3, 1) in new_one_antinode:
                        print()
                    new_one_antinode = [i for i in new_one_antinode if 0<=i[0]<=m_x and 0<=i[1]<=m_y]

                    if new_one_antinode:
                        n_k += 1
                        new_antinode.extend(new_one_antinode)
                    else:
                        break
            list_antinode.extend(new_antinode)
    return list_antinode


list_txt = [i.rstrip() for i in list_txt]

import time
time_start = time.time()

antenna_coordinates = get_symbol_coordinates(list_txt)
set_antinodes = set()
max_x = len(list_txt[0])-1
max_y = len(list_txt)-1
[set_antinodes.update(get_ful_antinode_one_antenna(value,max_x, max_y)) for index, value in antenna_coordinates.items()]

time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {len(set_antinodes)} \n Время Решения:{execution_time}")


import time
time_start = time.time()

antenna_coordinates = get_symbol_coordinates(list_txt)
set_antinodes = set()
max_x = len(list_txt[0])-1
max_y = len(list_txt)-1
[set_antinodes.update(get_ful_antinode_one_antenna(value,max_x, max_y, one=False)) for index, value in
 antenna_coordinates.items()]
set_antennas = set()
[set_antennas.update(value) for index, value in antenna_coordinates.items()]

time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 2: {len(set_antinodes)} \n Время Решения:{execution_time}")




