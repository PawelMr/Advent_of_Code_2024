from collections import Counter


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


point_start = [(st.index("S"), ind) for ind, st in enumerate(list_txt) if "S" in  st ][0]
point_finish = [(st.index("E"), ind) for ind, st in enumerate(list_txt) if "E" in  st ][0]
map_graf = get_fork(list_txt)
get_path(point_start,point_finish, map_graf)
list_ful_step = [point_start] + map_graf[point_start][0][2]




# from_pos - начальная точка пути
# path - set со всеми точками пути
# cost_dict - словарь, ключ - точка пути, значение - кол-во шагов от начала
# max_len - макс. длина пути жульничества
def find_cheats(from_pos, path, cost_dict, max_len):
    count_by_saved_dist = Counter()
    x, y = from_pos
    candidates = set()
    # "чертим" круг вокруг данной точки
    for dx in range(-max_len - 1, max_len + 1):
        for dy in range(-max_len - 1, max_len + 1):
            if dx == 0 and dy == 0:
                continue
            if not (0 <= x + dx < len(list_txt[0]) and 0 <= y + dy < len(list_txt)):
                continue
            try:
                get_content_coordinates((x + dx, y + dy), list_txt)
            except:
                print()
            if abs(dx) + abs(dy) <= max_len and get_content_coordinates((x + dx, y + dy), list_txt) != "#":
                candidates.add((x + dx, y + dy))
    # пересекаем с точками пути
    intersections = candidates.intersection(path)
    for p in intersections:
        # исходная длина по короткому пути
        original_distance = cost_dict[p] - cost_dict[from_pos]
        # если нашли точку, которая оказалась раньше текущей
        if original_distance < 0:
            continue
        px, py = p
        current_distance = abs(px - x) + abs(py - y) # путь через жульничество
        assert current_distance <= max_len
        if current_distance < original_distance:
            # успешно сжульничали
            # saved - сколько шагов сократили
            saved = original_distance - current_distance
            count_by_saved_dist[saved] += 1

    return count_by_saved_dist



answer = 0
for i in list_ful_step:

    col = find_cheats(i, set(list_ful_step), {j:i for i,j in enumerate(list_ful_step)}, 2)
    count_col = sum([value for key, value in col.items() if key>=100])
    answer+=count_col
print(answer)


answer = 0
for i in list_ful_step:

    col = find_cheats(i, set(list_ful_step), {j:i for i,j in enumerate(list_ful_step)}, 20)
    count_col = sum([value for key, value in col.items() if key>=100])
    answer += count_col
print(answer)
