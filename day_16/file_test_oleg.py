from heapq import heappush, heappop

from collections import defaultdict

paths = []
# элемент очереди:
# 1. стоимость
# 2. набор позиций, который мы посетили
# 3. Направление движения
# 4. Текущее положение
with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]

fld_ful = {}
for y, string in enumerate(list_txt):
    for x, value in enumerate(string):
        fld_ful.update({(x,y):value})
        if value == "S":
            st_point = (x,y)
        if value == "E":
            end_point = (x, y)

def get_way_sum(start_pos, end_pos, east,fld):
    heappush(paths, (0,  east, start_pos))
    seen = set()  # <-- вынесли их отдельно
    while paths:
        head = heappop(paths)
        score,  dp, p = head
        if p == end_pos:
            print(score)
            break
        # сразу считаем шаг + поворот. none - "без поворота"
        variances = ((0, 1), (1, 1001), (-1, 1001))
        for v in variances:
            rotation, penalty = v
            ndp = apply(dp, rotation) # применяем поворот
            np = advance(p, ndp) # делаем шаг
            ns = score + penalty # новая стоимость
            if np not in seen and fld.get(np, '#') != '#':  #  если мы там не были и там не стена
                seen.add(np)
                heappush(paths, (ns, ndp, np)) # добавляем в кучу

def apply(old_v, rot):
    list_v = "^>v<"
    return list_v[(list_v.index(old_v) +rot)%len(list_v)]

def advance(p, vs):
    direction_map = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }
    v = direction_map[vs]
    return p[0]+v[0], p[1]+v[1]



get_way_sum(st_point,end_point,">", fld_ful)


def get_min_way(start_pos, end_pos, east,fld):
    # тут стоимость для пары (pos, dp)
    # score_at_pos = defaultdict(lambda: +inf)
    score_at_pos = {}
    # тут словарь всех точек для каждой стоимости
    total_len = defaultdict(lambda: set())
    paths2 = []
    heappush(paths2, (0, {start_pos}, east, start_pos))
    while paths2:
        head = heappop(paths2)
        score, seen, dp, p = head
        if p == end_pos:  # <-- нашли конец?
            total_len[score] |= seen  # <-- добавим все посещенные точки в словарь
            continue
        variances = ((0, 1), (1, 1001), (-1, 1001))
        for v in variances:
            rotation, penalty = v
            ndp = apply(dp, rotation)
            np = advance(p, ndp)
            ns = score + penalty
            if np not in seen and fld[np] != '#':
                if np == (130,1):
                    print()
                flt_key = (np, ndp)
                # эвристика для исключения дохлых вариантов
                # if score_at_pos[flt_key] >= ns:
                #     heappush(paths, (ns, seen | {np}, ndp, np))
                # # обновим стоимость, если меньше
                # score_at_pos[flt_key] = min(score_at_pos[flt_key], ns)

                # эвристика для исключения дохлых вариантов
                if score_at_pos.get(flt_key, 100000000000)  >= ns:
                    heappush(paths2, (ns, seen | {np}, ndp, np))
                    # обновим стоимость, если меньше
                    score_at_pos[flt_key] = min(score_at_pos.get(flt_key, 100000000000), ns)
                else:
                    score_at_pos[flt_key] = ns

                # А вот и ответ на обе части
    min_p = min(total_len.keys())
    print(f'Part A: {min_p}')
    print(f'Part B: {len(total_len[min_p])}')

get_min_way(st_point,end_point,">", fld_ful)