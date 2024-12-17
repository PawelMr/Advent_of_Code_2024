import copy
import re
import collections
import time


with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]

def disassemble_into_numbers(string):
    pattern = r'(-?\d+)'
    number_txt_list = re.findall(pattern, string)
    number_list = [int(i) for i in number_txt_list]
    return number_list

initial_data = []
one_group = {}
for txt in list_txt:
    robot = {i[0]:disassemble_into_numbers(i) for i in txt.split()}
    initial_data.append(robot)


def find_position_after_n_seconds(rob,size_pol,n_sek = 100, res_cord = False ):
    x_pol = size_pol[0]
    y_pol = size_pol[1]
    x_new = (rob["p"][0] + rob['v'][0] * n_sek) % x_pol
    y_new = (rob["p"][1] + rob['v'][1] * n_sek) % y_pol
    if res_cord:
        return x_new, y_new
    # if (x_new,y_new) == (6, 0):
    #     print()
    sector = None
    if x_new < x_pol // 2 and y_new < y_pol // 2:
        sector = 1
    elif x_new > x_pol // 2  and y_new < y_pol // 2:
        sector = 2
    elif x_new < x_pol // 2 and y_new > y_pol // 2:
        sector = 3
    elif x_new > x_pol // 2  and y_new > y_pol // 2:
        sector = 4
    # print((x_new,y_new, sector))
    return sector


def moving_in_time(or_list_rob,size_pol,n_sek = 5):
    x_pol = size_pol[0]
    y_pol = size_pol[1]
    list_rob = copy.deepcopy(or_list_rob)


    for s in range(n_sek+1):
        print(f"============================= {s} sec =================================\n")
        list_pr = [tuple(i["p"]) for i in list_rob]
        col_p = collections.Counter(list_pr)
        for i in range(size_pol[1]):
            print("".join([str(col_p.get((j, i), ".")) for j in range(size_pol[0])]))
        for rob in list_rob:
            x, y = rob["p"]
            x += rob['v'][0]
            if x >= x_pol:
                x -= x_pol
            if x <0:
                x = x_pol+x
            y += rob['v'][1]
            if y >= y_pol:
                y -= y_pol
            if y <0:
                y = y_pol + y
            rob["p"] = (x,y)
        print("\n====================================================================\n")
    # list_pr = [i["p"] for i in list_rob]
    # col_p = collections.Counter(list_pr)
    # for i in range(size_pol[1]):
    #     print("".join([str(col_p.get((j, i), ".")) for j in range(size_pol[0])]))




time_start = time.time()
# pol = (11,7)
pol = (101,103)
# # find_position_after_n_seconds({'p': [2, 4], 'v': [2, -3]},pol, 5)
# list_sector = [find_position_after_n_seconds(i,pol,n_sek=100, res_cord=True) for i in initial_data]
#
# # list_sector = [find_position_after_n_seconds({'p': [2, 4], 'v': [2, -3]},pol, 5, res_cord=True)]
# col = collections.Counter(list_sector)
#
# for i in range(7):
#     print("".join([str(col.get((j,i), ".")) for j in range(11)]))

list_sector = [find_position_after_n_seconds(i,pol,n_sek=100) for i in initial_data]
col = collections.Counter(list_sector)
list_count = [value for key, value in col.items() if key]
pr_sect = 1
for i in list_count:
    pr_sect *= i


time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {pr_sect} \n Время Решения:{execution_time}")

st_pattern = ("0000000",
              "0001000",
              "0011100",
              "0111110")
st_point_patt = (3,1)

def check_set_in_pattern(set_points, pattern,point_patt):
    len_pattern_x = len(pattern[0])
    len_pattern_y = len(pattern[1])
    for ch_p in set_points:
        error = False
        for y_p, string in enumerate(pattern):
            for x_p, zn in enumerate(string):
                x = ch_p[0] + x_p - point_patt[0]
                y = ch_p[1] + y_p - point_patt[1]
                if ((x,y) in set_points) != int(zn):
                    error = True
                    break
            if error:
                break
        if not error:
            return True
    return False


time_start = time.time()


# list_rob = [find_position_after_n_seconds(i,pol,n_sek=6752, res_cord=True) for i in initial_data]
# col = collections.Counter(list_rob)
#
# for i in range(pol[1]):
#     print("".join([str(col.get((j,i), ".")) for j in range(pol[0])]))
# check_set_in_pattern(set(list_rob),st_pattern,st_point_patt)
# check_set_in_pattern(set([find_position_after_n_seconds(i,pol,n_sek=6752, res_cord=True) for i in initial_data]),st_pattern,st_point_patt)

sec = 1
while sec<10000:
    list_rob = [find_position_after_n_seconds(i, pol, n_sek=sec, res_cord=True) for i in initial_data]
    el = check_set_in_pattern(set(list_rob), st_pattern,st_point_patt)
    if el:
        break
    sec+=1

# for sec in range(7000):
#     el = check_set_in_pattern(set([find_position_after_n_seconds(i,pol,n_sek=sec, res_cord=True) for i in initial_data]),st_pattern,st_point_patt)
#     print(f"{sec}   ----  {el}")



time_finish = time.time()
execution_time = time_finish - time_start

print(f"Решение задания 2: {sec} \n Время Решения:{execution_time}")








