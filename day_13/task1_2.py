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
    number_list = [int(i) for i in number_txt_list]
    return number_list

initial_data = []
one_group = {}
for txt in list_txt:
    if txt:
        one_group.update({txt.split(":")[0]:disassemble_into_numbers(txt)})
    else:
        initial_data.append(one_group)
        one_group = {}
if one_group:
    initial_data.append(one_group)
    one_group = {}

def find_key_combination(dict_button, increase = 0):
    list_option = []
    ax = dict_button['Button A'][0]
    bx = dict_button['Button B'][0]
    px = dict_button['Prize'][0] + increase
    ay = dict_button['Button A'][1]
    by = dict_button['Button B'][1]
    py = dict_button['Prize'][1] + increase
    max_click_b = 100 if not increase and px//bx< 100 else px//bx
    for click_b in range(max_click_b+1):
        # click_a = int((px - click_b * bx) // ax)
        # if  ay*click_a +by*click_b == py and ax*click_a +bx*click_b == px:
        #     print((click_a, click_b))
        #     list_option.append((click_a, click_b))
        click_a = (px - click_b* bx) / ax
        if click_a % 1 == 0:
            click_a = int(click_a)
        else:
            continue
        if ay*click_a +by*click_b == py:
            list_option.append((click_a,click_b))
    return list_option

def find_key_combination2(dict_button):
    list_option = []
    ax = dict_button['Button A'][0]
    bx = dict_button['Button B'][0]
    px = dict_button['Prize'][0]
    ay = dict_button['Button A'][1]
    by = dict_button['Button B'][1]
    py = dict_button['Prize'][1]
    max_click_b = max_click_a= 100
    # max_click_b = px // ax
    for click_b in range(max_click_b+1):
        for click_a in range(max_click_a+1):
            if  ay*click_a +by*click_b == py and ax*click_a +bx*click_b == px:
                print((click_a, click_b))
                list_option.append((click_a, click_b))
        # click_a = (px - click_b* bx) / ax
        # if click_a % 1 == 0:
        #     click_a = int(click_a)
        # else:
        #     continue
        # if ay*click_a +by*click_b == py:
        #     list_option.append((click_a,click_b))
    return list_option



def calculate_tokens(list_options):
    list_tokens = []
    for option in list_options:
        one_po_token = 3*option[0]+option[1]
        list_tokens.append(one_po_token)
    return min(list_tokens) if list_tokens else 0

time_start = time.time()
sum_tokens = 0
for i in initial_data:
    comb = find_key_combination(i)
    tokens_play = calculate_tokens(comb)
    sum_tokens+=tokens_play
    # print(f"игра {i} комбинации {comb}  нужно токенов минимум {tokens_play}, сумма {sum_tokens}")

# sum_tokens = sum([calculate_tokens(find_key_combination(i)) for i in initial_data])
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {sum_tokens} \n Время Решения:{execution_time}")


def find_key_combination_mach(dict_button, increase=0):
    list_option = []
    ax = dict_button['Button A'][0]
    bx = dict_button['Button B'][0]
    px = dict_button['Prize'][0] + increase
    ay = dict_button['Button A'][1]
    by = dict_button['Button B'][1]
    py = dict_button['Prize'][1] + increase
    n = (py * ax - px * ay) / (by * ax - bx * ay)
    k = (px - n*bx ) / ax

    click_a = int(k)
    click_b = int(n)
    if ay * click_a + by * click_b == py and ax * click_a + bx * click_b == px:
        # print((click_a, click_b))
        list_option.append((click_a, click_b))
    return list_option



time_start = time.time()

sum_tokens = 0
for i in initial_data:
    comb = find_key_combination_mach(i, increase=10000000000000)
    tokens_play = calculate_tokens(comb)
    sum_tokens+=tokens_play
    # print(f"игра {i} комбинации {comb}  нужно токенов минимум {tokens_play}, сумма {sum_tokens}")

# find_key_combination_mach({'Button A': [94, 34], 'Button B': [22, 67], 'Prize': [8400, 5400]})
time_finish = time.time()
execution_time = time_finish - time_start

print(f"Решение задания 2: {sum_tokens} \n Время Решения:{execution_time}")








