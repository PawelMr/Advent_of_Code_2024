import copy
import re
import collections
import time


with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]

index_split = list_txt.index("")
initial_map = list_txt[:index_split]
list_traffic = "".join(list_txt[index_split + 1:])

len_map_x = len(initial_map[0])
len_map_y = len(initial_map)

def get_map_dict(list_str):
    dict_map = {}
    dict_object = {}
    for in_y, string in enumerate(list_str):
        for in_x, symbol in enumerate(string):
            if symbol == ".":
                continue
            dict_map.update({(in_x,in_y):symbol})
            if dict_object.get(symbol):
                dict_object[symbol].add((in_x,in_y))
            else:
                dict_object.update({symbol:{(in_x,in_y)}})
    return dict_map, dict_object



direction_map = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1)
}

def make_step(direction,dict_object):
    x_s,y_s = dict_object["@"].pop()
    xd,yd = direction_map[direction]
    nx = x_s+xd
    ny = y_s+yd
    set_box = set()
    new_set_box = set()
    while True:
        if (nx, ny) in dict_object["#"]:
            dict_object["@"].add((x_s, y_s),)
            return dict_object
        if (nx, ny) in dict_object["O"]:
            set_box.add((nx, ny))
            new_set_box.add((nx+xd, ny+yd))
        if (nx, ny) not in dict_object["O"] and (nx, ny) not in dict_object["#"]:
            new_set_obj_bod = (dict_object["O"] - set_box).union(new_set_box)
            dict_object["O"] = new_set_obj_bod
            dict_object["@"].add((x_s+xd,y_s+yd),)
            return dict_object
        nx += xd
        ny += yd

def draw_map(dict_object , new_ver = False):
    lmy = len_map_y
    lmx = len_map_x * 2 if new_ver else len_map_x
    for y in range(lmy):
        list_x = []
        fl_continue = False
        for x in range(lmx):
            if fl_continue:
                fl_continue = False
                continue
            if (x,y) in dict_object["O"]:
                if new_ver:
                    list_x.append("[")
                    list_x.append("]")
                    fl_continue = True
                else:
                    list_x.append("O")
            elif (x,y) in dict_object["#"]:
                list_x.append("#")
            elif (x,y) in dict_object["@"]:
                list_x.append("@")
            else:
                list_x.append(".")
        str_x = "".join(list_x)
        print(str_x)

def count_coordinate_one_obj(x,y):
    return x+100*y


map_start, position_obj_f = get_map_dict(initial_map)
# draw_map(position_obj)


time_start = time.time()
position_obj = copy.deepcopy(position_obj_f)
for step in list_traffic:
    position_obj = make_step(step, position_obj)
    # print(f"\n"
    #       f"========================\n"
    #       f"====step - {step} ============")
    # draw_map(position_obj)
sum_coordinates = 0

for obj in position_obj["O"]:
    sum_coordinates += count_coordinate_one_obj(*obj)
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum_coordinates} \n Время Решения:{execution_time}")

def get_new_coordinates(dict_obj):
    new_set = set()
    for x,y in dict_obj["#"]:
        new_set.add((2 * x, y))
        new_set.add((2 * x + 1, y))
    dict_obj["#"] = new_set
    x,y = dict_obj["@"].pop()
    dict_obj["@"].add((2 * x, y))
    new_set = set()
    for x, y in dict_obj["O"]:
        new_set.add((2 * x, y))
    dict_obj["O"] = new_set
    return dict_obj


def make_step_new(direction,dict_object):
    x_s,y_s = dict_object["@"].pop()
    xd,yd = direction_map[direction]
    nx = x_s+xd
    ny = y_s+yd
    list_xy = [(nx, ny)]
    set_box = set()
    new_set_box = set()
    while True:
        list_new_xy = []
        void = True
        for nx, ny in list_xy:
            if (nx, ny) in dict_object["#"]:
                dict_object["@"].add((x_s, y_s), )
                return dict_object
            if yd != 0:
                if (nx, ny) in dict_object["O"]:
                    set_box.add((nx, ny))
                    new_set_box.add((nx+xd, ny+yd))
                    list_new_xy.extend([(nx+xd, ny+yd),(nx+xd+1, ny+yd)])
                    void = False
                if (nx-1, ny) in dict_object["O"]:
                    set_box.add((nx-1, ny))
                    new_set_box.add((nx+xd-1, ny+yd))
                    list_new_xy.extend([(nx+xd -1 , ny+yd),(nx+xd, ny+yd)])
                    void = False
            elif xd ==1:
                if (nx, ny) in dict_object["O"]:
                    set_box.add((nx, ny))
                    new_set_box.add((nx+xd, ny+yd))
                    list_new_xy.extend([(nx+xd+1, ny+yd)])
                    void = False
            elif xd == -1:
                if (nx-1, ny) in dict_object["O"]:
                    set_box.add((nx-1, ny))
                    new_set_box.add((nx-1+xd, ny+yd))
                    list_new_xy.extend([(nx+xd-1, ny+yd)])
                    void = False
        list_xy = list_new_xy
        if void:
            new_set_obj_bod = (dict_object["O"] - set_box).union(new_set_box)
            dict_object["O"] = new_set_obj_bod
            dict_object["@"].add((x_s + xd, y_s + yd), )
            return dict_object

time_start = time.time()
position_obj = copy.deepcopy(position_obj_f)
position_obj = get_new_coordinates(position_obj)
# draw_map(position_obj, new_ver=True)

for step in list_traffic:
    position_obj = make_step_new(step, position_obj)
    # print(f"\n"
    #       f"========================\n"
    #       f"====step - {step} ============")
    # draw_map(position_obj, new_ver=True)

sum_coordinates = 0
for obj in position_obj["O"]:
    sum_coordinates += count_coordinate_one_obj(*obj)

time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 2: {sum_coordinates} \n Время Решения:{execution_time}")








