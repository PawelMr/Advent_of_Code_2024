import copy
import re
import collections


with open("input.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()

def disassemble_matrix(list_str):
    return [list(i.strip()) for i in list_str]

def find_x(matrix, x,y, symbol="X"):
    """
    ищем следующий элемент x в направлении строки слева на право
    если надо то переходя вниз
    x -индекс столбца с которого начнем
    y -номер строки с которой начат поиск
    """
    while y < len(matrix):
        if symbol in matrix[y][x:]:
            return matrix[y][x:].index(symbol)+x, y
        else:
            x=0
            y+=1
    return False

def find_word(matrix, x,y):
    """
    ищем слово XMAS от полученных координат во все стороны
    """
    directions =[
        (1,0),
        (1,1),
        (0,1),
        (-1,1),
        (-1,0),
        (-1,-1),
        (0,-1),
        (1, -1)
    ]
    len_matrix_x = len(matrix[0])
    len_matrix_y = len(matrix)
    if matrix[y][x] != "X":
        raise Exception("Неверные входные координаты для поиска слова")
    sum_word = 0
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        if (0<=x + direction[0]*3<len_matrix_x and
                0<=y + direction[1]*3<len_matrix_y and
                matrix[new_y][new_x] == "M"):
            if read_word_end(matrix, new_x, new_y, direction):
                sum_word+=1
    return sum_word


def read_word_end(matrix, x, y, direction):
    if matrix[y + direction[1]][x + direction[0]] == "A" and matrix[y + direction[1] * 2][x + direction[0] * 2] == "S":
        return True



import time
time_start = time.time()
list_letters = disassemble_matrix(list_txt)

sum_xmas = 0
xl = 0
yl = 0
while True:
    coordinates = find_x(list_letters,xl,yl)
    if coordinates:
        # if find_word(list_letters,*coordinates):
        #     print(coordinates)
        sum_xmas +=find_word(list_letters,*coordinates)
        xl, yl = coordinates
        xl+=1
        if xl > len(list_letters[0])-1:
            yl += 1
            xl = 0
            if yl == len(list_letters):
                break
    else:
        break
time_finish = time.time()
execution_time = time_finish - time_start

print(f"Решение задания 1: {sum_xmas} \n Время Решения:{execution_time}")


def find_x_word(matrix, x,y):
    """
    ищем слово MAS от полученных координат во все стороны
    """

    directions_two = (1, 1)
    directions = (-1, 1)
    len_matrix_x = len(matrix[0])
    len_matrix_y = len(matrix)
    if matrix[y][x] != "A":
        raise Exception("Неверные входные координаты для поиска слова")
    if 0 < x < len_matrix_x - 1 and 0 < y < len_matrix_y - 1:
        if read_word_mas(matrix,x, y, directions)and read_word_mas(matrix,x, y, directions_two):
            return 1
    return 0

def read_word_mas(matrix, x, y, direction):
    word = (f"{matrix[y + direction[1]][x + direction[0]]}"
            f"{matrix[y][x]}"
            f"{matrix[y + direction[1] * -1][x + direction[0] * -1]}")

    return True if "M" in word and "S" in word else False

import time
time_start = time.time()
list_letters = disassemble_matrix(list_txt)
sum_x_mas = 0
xl = 0
yl = 0
while True:
    coordinates = find_x(list_letters,xl,yl,symbol="A")
    if coordinates:
        sum_x_mas += find_x_word(list_letters,*coordinates)
        # if find_x_word(list_letters,*coordinates):
        #     print(coordinates,find_x_word(list_letters,*coordinates))

        xl, yl = coordinates
        xl+=1
        if xl > len(list_letters[0])-1:
            yl += 1
            xl = 0
            if yl == len(list_letters):
                break
    else:
        break
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 2: {sum_x_mas}  \n Время Решения:{execution_time}")


# for index_y, value_list in enumerate(list_letters):
#     if index_y == 0 or index_y == len(list_letters) - 1:
#         continue
#     else:
#         for index_x, value in value_list:
#             if value == "A" and index_x != 0 and index_x != len(list_letters[0]) - 1:
#                 a = value_list[index_x - 1] + value + value_list[index_x - 1]
#                 b =
