import copy
import re
import collections
from heapq import heappush, heappop
import time



with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]

    ind_division = list_txt.index("")
    set_options = set(", ".join(list_txt[:ind_division]).split(", "))
    list_mix = list_txt[ind_division+1:]

def create_variant(line_color,set_color):
    paths = []
    heappush(paths, (set(), line_color))
    list_quit = []

    while paths:
        head = heappop(paths)
        set_parts, remaining_line = head
        if remaining_line == "":
            # list_quit.append(set_parts)
            print("Да")
            return True
        for i in range(1,len(remaining_line)+1):
            if remaining_line[:i] in set_color:
                heappush(paths, (set_parts|{remaining_line[:i]}, remaining_line[i:]))
    # return list_quit
    print("Нет")
    return False


def create_variant2(line_color,set_color):
    paths = []
    list_quit = []
    set_good_remains = {line_color}
    while set_good_remains:
        remaining_line = set_good_remains.pop()
        if remaining_line in set_color:
            # list_quit.append(set_parts)
            print("Да")
            return True
        for i in range(1,len(remaining_line)+1):
            if remaining_line[i:] not in set_good_remains and remaining_line[:i] in set_color:
                set_good_remains.add(remaining_line[i:])
    # return list_quit
    print("Нет")
    return False


time_start = time.time()
variants = [create_variant2(i, set_options) for i in list_mix]
variants = [i for i in variants if i]
sum_v = len(variants)
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum_v} \n Время Решения:{execution_time}")

def calculate_variant(line_color,set_color, max_len_color):
    count_v = {line_color:set()}
    set_good_remains = {line_color}
    while set_good_remains:
        remaining_line = set_good_remains.pop()
        max_ind = max_len_color+1 if len(remaining_line)+1> max_len_color+1 else len(remaining_line)+1
        for i in range(1,max_ind):
            if remaining_line[:i] in set_color:
                set_good_remains.add(remaining_line[i:])
                if remaining_line not in count_v:
                    count_v[remaining_line] = {remaining_line[i:]}
                else:
                    count_v[remaining_line].add(remaining_line[i:])
    # return list_quit
    print(line_color)
    return calculate_value(count_v,line_color,)


def calculate_value(graph, element, memo={}):
    """
    Вычисляет значение элемента в графе, используя рекурсию.

    :param graph: словарь, где ключи - элементы графа, а значения - множества элементов, на которые есть ребра из ключа
    :param element: элемент графа, для которого нужно вычислить значение
    :param memo: элемент графа, для которого нужно вычислить значение
    :return: значение элемента
    """

    # Если значение элемента уже вычислено, возвращаем его
    if element in memo:
        return memo[element]

    # Если элемент является начальным (пустой строкой), то его значение равно 1
    if element == '':
        value = 1
    # Иначе вычисляем значение как сумму значений элементов, на которые есть ребра из данного элемента
    else:
        value = sum(calculate_value(graph, adjacent_element, memo) for adjacent_element in graph.get(element, {}))

    # Запоминаем вычисленное значение и возвращаем его
    memo[element] = value
    return value


# # алгоритм поиска в ШИРИНУ
# def count_way(dict_fork, step_start, step_finish, ):
#     turn_map = [(step_start, 0)]
#     visited_points = set()
#     count_length = 0
#     while turn_map:
#         step, sum_paths = turn_map.pop()
#         if sum_paths is None:
#             visited_points.remove(step)
#             continue
#         if step == step_finish:
#             count_length += 1
#             continue
#         if step in visited_points:
#             continue
#         visited_points.add(step)
#         turn_map.append((step, None))
#         for new_step in dict_fork.get(step, []):
#             turn_map.append((new_step, sum_paths + 1))
#     return count_length

# def count_way(dict_way,purpose):
#     way = 0
#     if not dict_way.get(purpose):
#         return 0
#
#     for value in dict_way[purpose]:
#         if value =="":
#             way+=1
#         else:
#             way+=count_way(dict_way, value)
#     return way


# def calculate_variant(line_color,set_color):
#     count_v = {'' :[]}
#     set_good_remains = {''}
#     while set_good_remains:
#         remaining_line = set_good_remains.pop()
#         if remaining_line == line_color:
#             continue
#         for v in set_color:
#             if line_color.startswith(remaining_line + v):
#                 # print( f"начало {remaining_line} нашли элемент {v} вся строка {remaining_line+v}")
#                 set_good_remains.add(remaining_line + v)
#
#                 if remaining_line + v not in count_v:
#                     count_v[remaining_line + v] = [remaining_line]
#                 else:
#                     count_v[remaining_line + v].append(remaining_line)
#     print(line_color)
#     return count_v.get(line_color, 0)



time_start = time.time()
len_col = max([len(i) for i in set_options])

calculate_variant(list_mix[3], set_options,len_col)
variants = [calculate_variant(c, set_options, len_col) for c in list_mix]
print(variants)
time_finish = time.time()
execution_time = time_finish - time_start

print(f"Решение задания 2: {sum(variants)} \n Время Решения:{execution_time}")








