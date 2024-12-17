import copy
import re
import collections
import time


with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()

def disassemble_into_numbers(string):
    pattern = r'(\d)'
    number_txt_list = re.findall(pattern, string)
    number_list = [int(i) for i in number_txt_list]
    return number_list

def find_points_start(map_ful):
    list_points_start = []
    for ind_y, line_x in enumerate(map_ful):
        [list_points_start.append((ind_x, ind_y)) for ind_x, value in enumerate(line_x) if value==0]
    return list_points_start

def take_step(point_start, map_ful, direction, max_ix, max_iy):
    new_x = point_start[0] + direction[0]
    new_y = point_start[1] + direction[1]
    if 0<=new_x<=max_ix and 0<=new_y<=max_iy:
        if map_ful[point_start[1]][point_start[0]]+1 == map_ful[new_y][new_x]:
            return (new_x, new_y), map_ful[new_y][new_x]
    return None, None

def find_way(map_ful, point_start):
    directions = [(0, -1),
                  (1, 0),
                  (0, 1),
                  (-1, 0)]
    max_ix = len(map_ful[0])-1
    max_iy = len(map_ful)-1
    list_route = []
    list_ways = [[point_start]]
    while list_ways:
        ways = list_ways.pop(-1)
        point_step = ways[-1]
        for direction in directions:
            new_point, height=take_step(point_step, map_ful, direction, max_ix, max_iy)
            if height is None:
                continue
            if height == 9:
                list_route.append(ways+[new_point])
            else:
                list_ways.append(ways+[new_point])
    return list_route



time_start = time.time()

start_cart = [disassemble_into_numbers(i) for i in list_txt]
list_points_zero = find_points_start(start_cart)

sum_task1 = 0
for point_zero in list_points_zero:
    len_way = len(set([i[-1] for i in find_way(start_cart, point_zero)]))
    sum_task1+=len_way


time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum_task1} \n Время Решения:{execution_time}")


time_start = time.time()

start_cart = [disassemble_into_numbers(i) for i in list_txt]
list_points_zero = find_points_start(start_cart)

sum_task1 = 0
for point_zero in list_points_zero:
    len_way = len(([i[-1] for i in find_way(start_cart, point_zero)]))
    sum_task1+=len_way


time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum_task1} \n Время Решения:{execution_time}")




