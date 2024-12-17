import copy
import re
import collections



with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()

def disassemble_into_numbers(string):
    pattern = r'(\d)'
    number_txt_list = re.findall(pattern, string)
    number_list = [int(i) for i in number_txt_list]
    return number_list

def dell_final_bloc(list_count_bloc):
    count_bloc_f_f = list_count_bloc.pop(-1)
    if list_count_bloc:
        empty_bloc_f = list_count_bloc.pop(-1)
    return count_bloc_f_f

def calculate_task_1(list_count_bloc):
    beg_id_f = 0
    fin_id_f = (len(start_cart) - 1) // 2
    blank_bloc = False
    id_bloc = 0
    sum_control = 0
    count_bloc_ff = dell_final_bloc(list_count_bloc)
    while list_count_bloc:
        if not blank_bloc:
            count_bloc = list_count_bloc.pop(0)
            for i in range(count_bloc):
                sum_control += beg_id_f * id_bloc
                id_bloc += 1
            beg_id_f += 1
            blank_bloc = not blank_bloc
        else:
            count_bloc = list_count_bloc.pop(0)
            for i in range(count_bloc):
                if count_bloc_ff == 0:
                    count_bloc_ff = dell_final_bloc(list_count_bloc)
                    fin_id_f -= 1
                sum_control += fin_id_f * id_bloc
                count_bloc_ff -= 1
                id_bloc += 1
            blank_bloc = not blank_bloc
    if count_bloc_ff:
        for  i in range(count_bloc_ff):
            count_bloc_ff-=1
            sum_control += fin_id_f * id_bloc
            id_bloc += 1
    return sum_control





import time
time_start = time.time()

start_cart = disassemble_into_numbers(list_txt[0])

remainder_for_parsing = copy.copy(start_cart)
sum_task1 = calculate_task_1(remainder_for_parsing)


time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum_task1} \n Время Решения:{execution_time}")

def get_new_list_file(list_file):
    new_list_file = copy.deepcopy(list_file)
    list_file.reverse()
    for block, idf in list_file:
        if not idf is None:
            list_place = [i for i in new_list_file if i[1] is None and i[0] >= block]
            if list_place:
                new_place = list_place[0]
                index = new_list_file.index(new_place)
                list_index_f = [i for i,v in enumerate(new_list_file) if v==[block, idf]]
                if index< list_index_f[-1]:
                    new_list_file[list_index_f[-1]] =[new_list_file[list_index_f[-1]][0], None]

                    if block == new_place[0]:
                        new_list_file[index] = [block, idf]
                    else:
                        new_list_file = (new_list_file[:index] +
                                         [[block, idf], [new_place[0]-block,None]] +
                                         new_list_file[index+1:])
    return new_list_file



import time
time_start = time.time()

list_block = [[value, index // 2 if not index % 2 else None] for index, value in enumerate(start_cart)]

new_list_block = get_new_list_file(list_block)

sum_task2 = 0
idb = 0
for blocks , id_f in new_list_block:
    for z in range(blocks):
        if not id_f is None:
            sum_task2 += idb*id_f
        idb +=1

time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 2: {sum_task2} \n Время Решения:{execution_time}")




