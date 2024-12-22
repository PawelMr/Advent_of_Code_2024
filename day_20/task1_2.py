import copy
import re
import collections
from heapq import heappush, heappop
import time


with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]


def get_new_step(old_step,direction):
    return old_step[0]+direction[0], old_step[1]+direction[1]


def get_content_coordinates(step, ful_map):
    return ful_map[step[1]][step[0]]


def get_variants_movement_not_slope(last_step, penultimate_step, ful_map):
    now_variants = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if last_step[1] == 0:
        now_variants.remove((0, -1))
    if last_step[1] == len(ful_map) - 1:
        now_variants.remove((0, 1))
    new_list_next_step = [get_new_step(last_step, i)
                          for i in now_variants if get_new_step(last_step, i) != penultimate_step
                          and get_content_coordinates(get_new_step(last_step, i), ful_map) != "#"]
    return new_list_next_step


def run_straight_line(step_start,next_step,ful_map):
    new_list_next_step = [1]
    step = next_step
    penultimate_step = step_start
    set_step = []
    while len(new_list_next_step) == 1:
        set_step.append(step)
        new_list_next_step = get_variants_movement_not_slope(step, penultimate_step, ful_map)
        penultimate_step = step
        if new_list_next_step:
            step = new_list_next_step[0]
    return penultimate_step[0], penultimate_step[1], set_step


def get_fork(ful_map):
    dict_fork = {}
    for i in range(len(ful_map)):
        for j in range(len(ful_map[i])):
            if ful_map[i][j] != "#":
                variants = get_variants_movement_not_slope((j, i), None, ful_map)
                if len(variants) == 2:
                    continue
                else:
                    list_point_finish = []
                    for variant in variants:
                        list_point_finish.append(run_straight_line((j, i), variant, ful_map))
                    dict_fork.update({(j, i):list_point_finish})
    return dict_fork


def get_path(start, end, graph, list_exclude=()):
    """
    returns the shortest path between start and end
    The solution doesn't NEED the shortest path (in fact it might be better random) but each cycle is quicker if we do
    """
    prev = {start: start}
    nodes = [start]
    seen = {start}
    while nodes:
        new_nodes = []
        for node in nodes:
            for x,y, set_step in graph[node]:
                if (x,y) in seen:
                    continue
                if (node, (x,y)) in list_exclude:
                    continue
                seen.add((x,y))
                prev[(x,y)] = node
                new_nodes.append((x,y))
        nodes = new_nodes

    if prev.get(end) is None:
        return None

    path = []
    node = end
    while node != start:
        path.append(node)
        node = prev[node]
    path.append(start)
    return path[::-1]


def get_bag_wall(step, ful_map):
    list_jump =[]
    now_variants = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for xd,yd in now_variants:
        xn = step[0]+xd
        yn = step[1] + yd
        xn2 = step[0]+xd*2
        yn2 = step[1] + yd*2
        if 0<=xn2<len(ful_map[0]) and 0<=yn2<len(ful_map):
            if get_content_coordinates((xn,yn), ful_map) =="#" and get_content_coordinates((xn2, yn2), ful_map) != "#":
                list_jump.append((xn2, yn2))

    return list_jump

def get_bag_wall_new(step, ful_map, len_jump):
    list_vz = [(1, 1), (-1, 1), (1, -1), (-1, -1), ]
    list_jump =[]
    for lj in range(2, len_jump+1):
        for xd in range(0, lj+1):
            yd = lj - xd
            for zx,zy in list_vz:
                xd = zx*xd
                yd = zy*yd
                xn = step[0] + xd
                yn = step[1] + yd
                if 0 <= xn < len(ful_map[0]) and 0 <= yn < len(ful_map) and \
                        (xn, yn) not in list_jump and \
                        get_content_coordinates((xn,yn), ful_map) != "#":
                    list_jump.append((xn,yn))
    return list_jump


def get_point_bag(list_way, ful_map):
    dict_bag = {}
    for step in list_way:
        jumps = get_bag_wall(step, ful_map)
        new_bag_step = [i for i in jumps if not dict_bag.get(i)]
        if new_bag_step:
            dict_bag.update({step: new_bag_step})
    return dict_bag


def get_point_bag_new(list_way, ful_map, len_jump=2):
    dict_bag = {}
    for ind_s, step in enumerate(list_way):

        jumps = get_bag_wall_new(step, ful_map, len_jump=len_jump)
        new_bag_step = [i for i in jumps if not dict_bag.get(i) and get_savings(step, i, list_way)>0]
        if new_bag_step:
            dict_bag.update({step: new_bag_step})
    return dict_bag


def get_savings(step1, step2, list_way):
    ind1 = list_way.index(step1)
    ind2 = list_way.index(step2)
    return abs(ind1-ind2) - abs(step1[0]-step2[0])- abs(step1[1]-step2[1])


def get_sum_count_savings(dict_bag, list_way):
    list_savings = 0
    for step1, list_jump in dict_bag.items():
        for step2 in list_jump:
            if get_savings(step1, step2, list_way) >= 100:
                list_savings+=1
    return list_savings


point_start = [(st.index("S"), ind) for ind, st in enumerate(list_txt) if "S" in  st ][0]
point_finish = [(st.index("E"), ind) for ind, st in enumerate(list_txt) if "E" in  st ][0]
map_graf = get_fork(list_txt)
get_path(point_start,point_finish, map_graf)
list_ful_step = [point_start] + map_graf[point_start][0][2]


time_start = time.time()
dict_hit = get_point_bag(list_ful_step, list_txt)
sum_count = get_sum_count_savings(dict_hit, list_ful_step)

time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum_count} \n Время Решения:{execution_time}")



time_start = time.time()
print(f"Длинна пути {len(list_ful_step)}")
dict_hit2 = get_point_bag_new(list_ful_step, list_txt, len_jump=20)
sum_count = get_sum_count_savings(dict_hit2, list_ful_step)


time_finish = time.time()
execution_time = time_finish - time_start

print(f"Решение задания 2: {sum_count} \n Время Решения:{execution_time}")








