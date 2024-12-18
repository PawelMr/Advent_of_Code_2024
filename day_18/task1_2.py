import copy
import re
import collections
import time



with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]


def disassemble_into_numbers(string):
    pattern = r'(\d+)'
    number_txt_list = re.findall(pattern, string)
    number_list = tuple(int(i) for i in number_txt_list)
    return number_list

list_bit = [disassemble_into_numbers(i) for i in list_txt]

def get_path(start, end, graph, list_exclude=()):
    """

    """
    prev = {start: start}
    nodes = [start]
    seen = {start}
    while nodes:
        new_nodes = []
        for node in nodes:
            for neighbour in graph[node]:
                if neighbour in seen:
                    continue
                if (node, neighbour) in list_exclude:
                    continue
                seen.add(neighbour)
                prev[neighbour] = node
                new_nodes.append(neighbour)
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

def get_graph(size_x, size_y, list_exceptions):
    direction= [(1, 0),(-1, 0),(0, -1),(0, 1)]
    graph = {}
    for y in range(size_y+1):
        for x in range(size_x + 1):
            if (x,y) in list_exceptions:
                continue
            for dx, dy  in direction:
                nx = x+dx
                ny = y+ dy
                if 0<=nx<=size_x and 0<=ny<=size_y and (nx,ny) not in list_exceptions:
                    if graph.get((x,y)):
                        graph[(x,y)].append((nx,ny),)
                    else:
                        graph.update({(x,y):[(nx,ny)]})
    return graph


time_start = time.time()
# map_graph = get_graph(6,6,list_bit[:12])
# way = get_path((0,0),(6,6), map_graph)

map_graph = get_graph(70,70,list_bit[:1024])
way=get_path((0,0),(70,70), map_graph)

time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {len(way)-1} \n Время Решения:{execution_time}")

def fatal_bait(size_x, size_y, list_exclude):
    good_bait = 1
    bed_bait = len(list_exclude) - 1
    while (bed_bait - good_bait) >1:
        n_bait = (good_bait + bed_bait) //2
        n_map_graph = get_graph(size_x, size_y, list_exclude[:n_bait])
        n_way = get_path((0, 0), (size_x, size_y), n_map_graph)
        if 2897<n_bait<2902:
            print()
        if n_way:
            good_bait = n_bait # 2898
        else:
            bed_bait = n_bait # 2899
    return bed_bait-1

time_start = time.time()
# ind_fb = fatal_bait(6,6,list_bit)
ind_fb = fatal_bait(70,70,list_bit)
time_finish = time.time()
execution_time = time_finish - time_start
print(f"надо 2898 пришло {ind_fb}")
print(f"Решение задания 2: {list_bit[ind_fb]} \n Время Решения:{execution_time}")








