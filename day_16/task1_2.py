import copy
import re
import collections
import time



with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]

direction_map = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1)
}
map_direction = {
    (1, 0):">",
    (-1, 0):"<",
    (0, -1):"^",
    (0, 1):"v"
}

def get_content_coordinates(step, ful_map):
    return ful_map[step[1]][step[0]]

def get_new_step(old_step,direction):
    return old_step[0]+direction[0], old_step[1]+direction[1]

def get_variants_movement_not_slope(last_step, penultimate_step, ful_map):
    now_variants = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if last_step[0] == 0:
        now_variants.remove((-1, 0))
    if last_step[0] == len(ful_map) - 1:
        now_variants.remove((1, 0))
    # new_list_next_step = [get_new_step(last_step, i)
    #                       for i in now_variants if get_new_step(last_step, i) != penultimate_step
    #                       and get_content_coordinates(get_new_step(last_step, i), ful_map) != "#"]
    new_list_next_step = []
    for i in now_variants:
        if( get_new_step(last_step, i) != penultimate_step and
        get_content_coordinates(get_new_step(last_step, i), ful_map) != "#"):
            new_list_next_step.append(get_new_step(last_step, i))
    return new_list_next_step

def run_straight_line(step_start,next_step,ful_map, vector_old):
    list_vec = ">v<^"
    new_list_next_step = [next_step]
    step = next_step
    old_step = step_start
    penultimate_step = step_start
    count_step = 0
    new_vec = vector = vector_old
    while len(new_list_next_step) == 1 and get_content_coordinates(penultimate_step, ful_map) != "E":
        count_step += 1
        new_vec = map_direction[(step[0] - old_step[0], step[1] - old_step[1])]
        if new_vec != vector:
            # if list_vec[list_vec.index(new_vec)+1] == vector  or list_vec[list_vec.index(new_vec)-1] == vector:
            #     count_step += 1000
            # else:
            #     count_step += 2000
            count_step += 1000
            vector = new_vec
        new_list_next_step = get_variants_movement_not_slope(step, penultimate_step, ful_map)
        penultimate_step = step

        if new_list_next_step:
            old_step = step
            step = new_list_next_step[0]


    return penultimate_step[0], penultimate_step[1], count_step, vector_old, new_vec

def get_fork(ful_map):
    dict_fork = {}
    for y in range(len(ful_map)):
        for x in range(len(ful_map[y])):
            if (x, y) == (1, 13):
                print()
            if ful_map[y][x] != "#":
                variants = get_variants_movement_not_slope((x,y), None, ful_map)
                if len(variants) == 2 and get_content_coordinates((x, y), ful_map) == ".":
                    continue
                else:
                    list_point_finish = []
                    for variant in variants:
                        direction = map_direction[(variant[0] - x,variant[1] -y)]
                        new_point = run_straight_line((x,y), variant, ful_map, direction)
                        if len(get_variants_movement_not_slope(new_point[:2], None, ful_map))>1:
                            list_point_finish.append(new_point)
                        # list_point_finish.append(new_point)
                    dict_fork.update({(x,y):list_point_finish})
    return dict_fork


# алгоритм поиска в ШИРИНУ
def get_min_length_paths(step_start, step_finish, dict_fork, vec_st, one_min_length=None):
    list_vec = ">v<^"
    turn_map = [(step_start[0], step_start[1], 0, vec_st)]
    visited_points = set()
    min_length =  1000*1000* len(dict_fork) if not one_min_length else  one_min_length
    while turn_map:
        x, y, sum_paths, vec = turn_map.pop()
        if sum_paths is None:
            visited_points.remove((x, y))
            continue
        if (x, y) == step_finish:
            min_length = min(sum_paths, min_length)
            continue
        if sum_paths>=min_length:
            continue
        if (x, y) in visited_points:
            continue
        visited_points.add((x, y))
        turn_map.append((x, y, None, vec))
        for new_x, new_y, new_sum,in_vec, new_vec in dict_fork[(x, y)]:
            if vec != in_vec:
                # if list_vec[list_vec.index(vec)+1] == vec  or list_vec[list_vec.index(vec)11] == vec:
                #     new_sum += 1000
                # else:
                #     new_sum += 2000
                new_sum += 1000
            if (1, 11) == (new_x, new_y):
                print()

            turn_map.append((new_x, new_y, sum_paths + new_sum, new_vec))
    return min_length

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
            for neighbour in graph[node]:
                if neighbour[:2] in seen:
                    continue
                if (node, neighbour[:2]) in list_exclude:
                    continue
                seen.add(neighbour[:2])
                prev[neighbour[:2]] = node
                new_nodes.append(neighbour[:2])
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

def count_cost_way(list_step, ful_map, st_vec):
    old_vec = st_vec
    sum_cost = 0
    for in_step in range(1,len(list_step)):
        list_options = ful_map[list_step[in_step - 1]]
        for i in list_options:
            if list_step[in_step] == i[:2]:
                sum_cost+=i[2]
                if old_vec != i[3]:
                    sum_cost +=1000
                old_vec = i[4]
                break
    return sum_cost



time_start = time.time()

point_start = [(st.index("S"), ind) for ind, st in enumerate(list_txt) if "S" in  st ][0]
point_finish = [(st.index("E"), ind) for ind, st in enumerate(list_txt) if "E" in  st ][0]
ful_fork = get_fork(list_txt)
one_way = get_path(point_start,point_finish,ful_fork)
sum_way_one = count_cost_way(one_way,ful_fork,">")
sum_way = get_min_length_paths(point_start,point_finish,ful_fork, ">",sum_way_one)
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum_way} \n Время Решения:{execution_time}")


time_start = time.time()

time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 2: {0} \n Время Решения:{execution_time}")








