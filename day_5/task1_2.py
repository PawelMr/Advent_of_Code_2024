import copy
import re
import collections

with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()

def get_two_parts(original_list):
    """ отделяем правила от очередей в исходном файле"""
    index = original_list.index("\n")
    return original_list[:index], original_list[index+1:]

def disassemble_into_numbers(string):
    pattern = r'(\d+)'
    number_txt_list = re.findall(pattern, string)
    number_list = [int(i) for i in number_txt_list]
    return number_list

def disassemble_rule(list_rule):
    """Собираем правила пачати в прямом последовательности, ключ страница, значение список страниц которые идут после"""
    dict_rule = {}
    for i in list_rule:
        key, value = disassemble_into_numbers(i)
        if dict_rule.get(key):
            dict_rule[key].append(value)
        else:
            dict_rule.update({key:[value]})
    return dict_rule

def disassemble_rule_reverse(list_rule):
    """Собираем правила пачати в прямом последовательности, ключ страница, значение список страниц которые идут после"""
    dict_rule = {}
    for i in list_rule:
        value, key = disassemble_into_numbers(i)
        if dict_rule.get(key):
            dict_rule[key].append(value)
        else:
            dict_rule.update({key:[value]})
    return dict_rule


def del_bet_queue(ful_list_queue, dict_rule, bet = True):
    """проверка соответствует ли правилам, берем прямые правила
    ключ страница, значение список страниц которые идут после"""
    new_list_queue = []
    if bet:
        check_bat = lambda x: not x
    else:
        check_bat = lambda x: x
    for queue in ful_list_queue:
        skip = False
        for index, page in enumerate(queue):
            for i in dict_rule.get(page,[]):
                if i in queue[:index]:
                    skip = True
                if skip:
                    break
        if check_bat(skip):
            new_list_queue.append(queue)
    return new_list_queue

def sum_center(array):
    summ = 0
    for i in array:
        summ += i[len(i)//2]
    return summ

import time
time_start = time.time()
rule_print, list_queue = get_two_parts(list_txt)
rule_print = disassemble_rule(rule_print)
list_queue = [disassemble_into_numbers(i) for i in list_queue]

good_queue = del_bet_queue(list_queue,rule_print)
answer = sum_center(good_queue)
time_finish = time.time()
execution_time = time_finish - time_start

print(f"Решение задания 1: {answer} \n Время Решения:{execution_time}")



def fn_sort_1(a,b):
    """функция сотрировки"""
    if a>b:
        return -1
    elif a<b:
        return 1
    else:
        return 0

def fn_sort_rule(rule,reverse_rule):
    """обертка для передачи правил сортировки"""
    def fn_sort(a, b):
        """функция сотрировки"""
        if b in rule.get(a,[]):
            return -1
        elif b in reverse_rule.get(a,[]):
            return 1
        else:
            return 0
    return fn_sort
import time
from functools import cmp_to_key
time_start = time.time()

rule_print_txt, list_queue = get_two_parts(list_txt)
list_queue = [disassemble_into_numbers(i) for i in list_queue]
rule_print = disassemble_rule(rule_print_txt)
revers_rule_print = disassemble_rule_reverse(rule_print_txt)
bet_queue = del_bet_queue(list_queue,rule_print, bet=False)

new_bet_queue = [sorted(i,key=cmp_to_key(fn_sort_rule(rule_print,revers_rule_print))) for i in bet_queue]
answer = sum_center(new_bet_queue)
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 2: {answer}  \n Время Решения:{execution_time}")




#
#
# # |||||||||||||||||||||||||||||||||||||||||ПЛОХО||||||||||||||||||||||||||||||||||||||||||||||||
#
# def shuffle_queue(queue, dict_rule):
#     "Пытаемся очередь выстроить в правильном порядке, перенося в начало списка каждый элемент на котором прошел сбой"
#     skip = True
#     while skip:
#         skip = False
#         for index, page in enumerate(queue):
#             for i in dict_rule.get(page,[]):
#                 if i in queue[:index]:
#                     skip = True
#                     replacement = index
#                 if skip:
#                     break
#             if skip:
#                 break
#         if skip:
#             new_queue = [queue[replacement]]
#             new_queue.extend(queue[:replacement])
#             new_queue.extend(queue[replacement+1:])
#             queue = new_queue
#     return queue
#
#
# # первое решение с перебором долго и плохо
# import time
# time_start = time.time()
# bet_queue = del_bet_queue(list_queue,rule_print, bet=False)
# new_bet_queue = [shuffle_queue(i,rule_print) for i in bet_queue]
# # new_bet_queue = [sorted(i,key=cmp_to_key(fn_sort_1)) for i in bet_queue]
# answer = sum_center(new_bet_queue)
# time_finish = time.time()
# execution_time = time_finish - time_start
# print(f"Решение задания 2: {answer}  \n Время Решения:{execution_time}\n "
#       f"первое решение с перебором долго и плохо")
