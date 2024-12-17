import copy
import re
import collections
import time


with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]

def get_dict_coordinates(list_string):
    dict_coordinates = {}
    for y, string in enumerate(list_string):
        for x, letter in enumerate(string):
            if dict_coordinates.get(letter):
                dict_coordinates[letter].append((x,y))
            else:
                dict_coordinates.update({letter:[(x,y)]})
    return dict_coordinates

def get_nearby_coordinates(coordinates):
    directions = [(0, -1),
                  (1, 0),
                  (0, 1),
                  (-1, 0)]
    new_list = []
    for (xd, yd) in directions:
        new_x = coordinates[0]+ xd
        new_y = coordinates[1] + yd
        new_list.append((new_x, new_y))
    return new_list


def get_group_coordinates(start_list_coordinates, return_group = False):
    list_coordinates = copy.deepcopy(start_list_coordinates)
    list_groups = []
    new_groups = []
    set_analysis = set()
    while list_coordinates:
        if not set_analysis:
            element = list_coordinates.pop(0)
            if new_groups:
                if return_group:
                    list_groups.append(new_groups)
                else:
                    list_groups.append(get_sum_group(new_groups))
                new_groups = []
        else:
            element = set_analysis.pop()
            list_coordinates.remove(element)
        x, y = element
        list_nearby_xy = get_nearby_coordinates(element)
        p_point = 4
        for (nx,ny) in list_nearby_xy:
            if (nx,ny) in start_list_coordinates:
                p_point -= 1
            if (nx,ny) in list_coordinates:
                set_analysis.add((nx,ny))
        if return_group:
            new_groups.append((x, y))
        else:
            new_groups.append((x,y,p_point))
    if new_groups:
        if return_group:
            list_groups.append(new_groups)
        else:
            list_groups.append(get_sum_group(new_groups))
    return list_groups


def get_sum_group(group):
    p_group = sum([i[2] for i in group])
    s_group = len(group)
    return p_group * s_group


time_start = time.time()

dict_letter = get_dict_coordinates(list_txt)
sum_many = 0
for key, value in dict_letter.items():
    sum_many+= sum(get_group_coordinates(value))
# get_group_coordinates(dict_letter['R'])

time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum_many} \n Время Решения:{execution_time}")



def count_corners(list_point):
    directions = [(0, -1),
                  (1, 0),
                  (0, 1),
                  (-1, 0)]
    directions_diagonal = [(1, -1),
                           (1, 1),
                           (-1, 1),
                           (-1, -1)]
    set_directions = {(0, -1),
                      (1, 0),
                      (0, 1),
                      (-1, 0),
                      (1, -1),
                      (1, 1),
                      (-1, 1),
                      (-1, -1)}
    list_set_corners = [{(0, -1, 0), (1, 0, 0)},
                        {(1, 0, 0),  (0, 1, 0)},
                        {(0, 1, 0), (-1, 0, 0)},
                        {(0, -1, 0),  (-1, 0, 0)},
                        {(0, -1, 1), (1, -1, 0), (1, 0, 1)},
                        {(1, 0, 1), (1, 1, 0), (0, 1, 1)},
                        {(0, 1, 1), (-1, 1, 0), (-1, 0, 1)},
                        {(0, -1, 1), (-1, -1, 0), (-1, 0, 1)}
                        ]

    sum_corners = 0
    for x,y in list_point:
        list_d = []
        for dx, dy in directions:
            if (x + dx, y + dy) in list_point:
                list_d.append((dx, dy))
        list_dd = []
        for dx, dy in directions_diagonal:
            if (x + dx, y + dy) in list_point:
                list_dd.append((dx, dy))

        set_ful_gr = set((xg,yg, 1 if(xg,yg) in list_dd or (xg,yg) in list_d else 0) for xg,yg in set_directions)
        for comb in list_set_corners:
            if not comb - set_ful_gr:
                # print(f"{x,y}   - угол {comb}")
                sum_corners+=1
        # print()
    return sum_corners




time_start = time.time()

dict_letter = get_dict_coordinates(list_txt)
sum_many = 0
for key, value in dict_letter.items():
    group_f = get_group_coordinates(value, True)
    for f in group_f:

        n_corners = count_corners(f)
        sum_many += n_corners * len(f)
        print(f"группа {key}    площадь {len(f)}  количество сторон {n_corners} "
              f"сумма {n_corners * len(f)}")
# get_group_coordinates(dict_letter['R'], True)

time_finish = time.time()
execution_time = time_finish - time_start

print(f"Решение задания 1: {sum_many} \n Время Решения:{execution_time}")








