import copy
import re
import collections
import time


with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()

def disassemble_into_numbers(string):
    pattern = r'(\d+)'
    number_txt_list = re.findall(pattern, string)
    number_list = [int(i) for i in number_txt_list]
    return number_list


def check_the_rules(a):
    if a==0:
        return [1]
    if len(str(a))%2 ==0:
        return [int(str(a)[:len(str(a))//2]), int(str(a)[len(str(a))//2:])]
    else:
        return [a*2024]

def conversion_one_step(list_element):
    new_list_element = []
    for element in list_element:
        new_list_element.extend(check_the_rules(element))
    return new_list_element

def make_conversion(start_list_element, n_step):
    list_element = copy.copy(start_list_element)
    # print(f"{0}  ---  {len(list_element)}")
    for i in range(n_step):
        # old_len_list = len(list_element)
        list_element = conversion_one_step(list_element)
        # print(f"{i + 1}  ---  {len(list_element)} ----   {len(list_element)  - old_len_list}")
    return list_element

time_start = time.time()

start_cart = disassemble_into_numbers(list_txt[0])
new_cart = make_conversion(start_cart,25)

# for i in start_cart:
#     if set(make_conversion([0],25)) != set(make_conversion([i],25)):
#         print(i)


time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {len(new_cart)} \n Время Решения:{execution_time}")

def list_in_list_count(list_element):
    set_element = set(list_element)
    return [(i, list_element.count(i)) for i in set_element]

def get_cart_five_step(element_start, list_result):
    return dict({element_start:list_in_list_count(list_result)})

def update_count_in_list(list_element):
    set_element = set(i[0] for i in list_element)
    return [(i, sum([j[1] for j in list_element if j[0] == i])) for i in set_element]

def go_by_five_step(list_element, dict_cart):
    new_list_element = []
    for element in list_element:
        if not dict_cart.get(element[0]):
            dict_cart.update(get_cart_five_step(element[0],make_conversion([element[0]],5)))
        new_list_element.extend([(i[0], i[1]*element[1]) for i in dict_cart[element[0]]])
    new_list_element = update_count_in_list(new_list_element)
    return new_list_element

time_start = time.time()
start_cart = disassemble_into_numbers(list_txt[0])
list_stone_count = list_in_list_count(start_cart)
dict_cart_step = {}
new_list_stone = copy.deepcopy(list_stone_count)

for b in range(15):
    new_list_stone = go_by_five_step(new_list_stone, dict_cart_step)

sum_stone = sum([i[1] for i in new_list_stone])
time_finish = time.time()
execution_time = time_finish - time_start
# Сохранял не весь набор элементов а только значение и количество с таким значением.
# под это надо было использовать словарь или коллекции
#  прирост скорости раз в 100 был бы
# https://online.sbis.ru/news/2e503d83-4a40-498c-8423-24a3beed4564
print(f"Решение задания 1: {sum_stone} \n Время Решения:{execution_time}")




