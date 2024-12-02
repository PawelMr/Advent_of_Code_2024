import copy
import re
import collections

with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()

print()

def disassemble_into_numbers(string):
    pattern = r'(\d+)'
    number_txt_list = re.findall(pattern, string)
    number_list = [int(i) for i in number_txt_list]
    return number_list
list_1 = []
list_2 = []

for string_txt in list_txt:
    list_int_str = disassemble_into_numbers(string_txt)
    list_1.append(list_int_str[0])
    list_2.append(list_int_str[1])
# list_txt = [disassemble_into_numbers(txt) for txt in list_txt]

list_1_dooble = copy.copy(list_1)
list_2_dooble = copy.copy(list_2)
sum_difference = 0
for i in range(len(list_1)):
    value_list_1 = min(list_1_dooble)
    value_list_2 = min(list_2_dooble)
    list_1_dooble.remove(value_list_1)
    list_2_dooble.remove(value_list_2)
    sum_difference +=abs(value_list_1-value_list_2)


print(f"Решение задания 1: {sum_difference}")

collections_list_2 = collections.Counter(list_2)

sum_composition_collections = 0
for value in list_1:
    sum_composition_collections += value*collections_list_2[value]
print(f"Решение задания 2: {sum_composition_collections}")
