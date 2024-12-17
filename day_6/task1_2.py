import copy
import re
import collections


with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()

def get_description_card(list_txt_string):
    """
    анализ списка строк, вернем:
    размер поля по x
    размер поля по y
    положение старта по координатам и направление числом ^ - 0, > - 1, v - 2, < - 3
    список координат всех препятствий
    """
    list_txt_string = [i.rstrip() for i in list_txt_string if i.rstrip()]
    max_x = len(list_txt_string[0])-1
    max_y = len(list_txt_string)-1
    security = []
    barrier = []
    for index_y, value_str in enumerate(list_txt_string):
        security.extend([[value_str.index(symbol), index_y, direction] for direction, symbol in enumerate("^>v<")
                       if symbol in value_str])

        barrier.extend([(index_,index_y) for index_, element in enumerate(value_str) if element == '#'])
    if len(security)==1:
        return max_x, max_y, security[0], barrier
    else:
        raise Exception("Неверные входные данные")

def hit_the_road(max_x, max_y, security, barriers):
    directions = {0: (0, -1),
                  1: (1, 0),
                  2: (0, 1),
                  3: (-1, 0)}
    dict_barriers_x = get_dict_barriers(barriers)
    dict_barriers_y = get_dict_barriers(barriers, axis = 1)
    comparison = lambda z1, z2, zn: z1 < z2 if zn == 1 else z1 > z2
    # set_coordinates = {(security[0],security[1]),}
    list_coordinates = [tuple(security)]
    new_trend = security[2]
    while (0<= security[0] + directions[security[2]][0] <= max_x
           and 0<= security[1] + directions[security[2]][1]<= max_y):
        x, y, trend = security
        trend = new_trend
        if directions[trend][0]:
            step = directions[trend][0]
            list_new_x = [i for i in dict_barriers_y.get(y,[]) if comparison(x, i, step)]
            if step == 1:
                list_new_x.sort()
            else:
                list_new_x.sort(reverse=True)
            new_x = list_new_x[0] - step if list_new_x else max_x if step == 1 else 0
            new_y = y
            # [set_coordinates.update(((i, new_y),)) for i in range(x, new_x + step, step)]
            new_list = [(i, new_y,trend) for i in range(x, new_x + step, step)]
        if directions[trend][1]:
            step = directions[trend][1]
            list_new_y = [i for i in dict_barriers_x.get(x,[]) if comparison(y, i, step)]
            if step == 1:
                list_new_y.sort()
            else:
                list_new_y.sort(reverse=True)
            new_y = list_new_y[0]- step if list_new_y else max_y if step == 1 else 0
            new_x = x
            # [set_coordinates.update(((new_x, i),)) for i in range(y, new_y + step, step)]
            new_list = [(new_x, i,trend) for i in range(y, new_y + step, step)]
        if new_list[1:] and new_list[-1] in list_coordinates:
            # print("ПЕТЛЯ!!!!!!!!  ")
            # print(list_coordinates)
            return "Петля"
        list_coordinates.extend(new_list[1:])

        new_trend = trend+1 if trend+1 <4 else 0
        security = (new_x, new_y,trend)
    return list_coordinates



def get_dict_barriers(barriers, axis = 0):
    """получить из списка координат словарь типа:
     координата оси: список координат второй оси которые ей соответствуют
     barriers - список координат
     axis - ось 0- x 1- y"""
    dict_barriers = dict()
    two_axis = 0 if axis else 1
    for i in barriers:
        if dict_barriers.get(i[axis]):
            dict_barriers[i[axis]].append(i[two_axis])
        else:
            dict_barriers.update({i[axis]:[i[two_axis]]})
    return dict_barriers

import time
time_start = time.time()

size_x, size_y, start_security, list_barrier = get_description_card(list_txt)
coordinates_presence = hit_the_road(size_x, size_y, start_security, list_barrier)
set_coordinates_presence = set([(x,y) for x,y,z in coordinates_presence])
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {len(set_coordinates_presence)} \n Время Решения:{execution_time}")



sum_new_barrier = 0
list_block =[]
for step_c in set_coordinates_presence:
    if tuple(start_security[:2]) != step_c and hit_the_road(size_x, size_y, start_security, list_barrier+[step_c]) == "Петля":
        # print(step_c)
        sum_new_barrier += 1
        list_block.append(step_c)

print(f"Решение задания 2: {sum_new_barrier} \n Время Решения: {'нет замера'}")



# |||||||||||||||ПЛОХО!!!|||||||||||||||||||||||||||||||||


def hit_the_road2(max_x, max_y, security, barriers):
    directions = {0: (0, -1),
                  1: (1, 0),
                  2: (0, 1),
                  3: (-1, 0)}
    x, y, trend = security
    list_way = []
    while 0<= x <= max_x and 0<= y<= max_y:
        list_way.append((x, y), )
        new_x = x + directions[trend][0]
        new_y = y + directions[trend][1]
        if (new_x,new_y) not in barriers:
            x, y = new_x, new_y
            continue
        else:
            deadlock = True
            for i in range(4):
                trend = trend + 1 if trend + 1 < 4 else 0
                new_x = x + directions[trend][0]
                new_y = y + directions[trend][1]
                if (new_x, new_y) not in barriers:
                    x, y = new_x, new_y
                    deadlock = False
                    break
            if deadlock:
                raise Exception("нашли тупик")
    return list_way



import time
time_start = time.time()

size_x, size_y, start_security, list_barrier = get_description_card(list_txt)
list_way_security = hit_the_road2(size_x, size_y, start_security, list_barrier)

time_finish = time.time()
execution_time = time_finish - time_start

print(f"Решение задания 1: {len(set(list_way_security))} \n Время Решения:{execution_time}")
# print(list_way_security)

