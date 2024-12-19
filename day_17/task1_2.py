import copy
import re
import collections
import time



with open("test.txt", mode="r", encoding="utf-8") as test_file:
    list_txt = test_file.readlines()
    list_txt = [i.rstrip() for i in list_txt]


class Computer:
    def __init__(self, a,b,c, list_program):
        self.reg_a = a
        self.reg_b = b
        self.reg_c = c
        self.ind_operation = 0
        self.list_operation = [(list_program[i], list_program[i + 1]) for i in range(0, len(list_program), 2)]
        self.output: list[int] = []

    def adv(self, opr):
        numerator = self.reg_a
        denominator = 2 ** opr
        val = numerator // denominator
        self.reg_a = val

    def bxl(self, opr):
        numb1 = self.reg_b
        numb2 = opr
        val = numb1 ^ numb2
        self.reg_b = val

    def bst(self, opr):
        val = opr % 8
        self.reg_b = val

    def jnz(self, opr):
        if self.reg_a != 0:
            self.ind_operation = opr-1

    def bxc(self, opr):
        val = self.reg_b ^ self.reg_c
        self.reg_b = val

    def out(self, opr):
        val = opr % 8
        self.output.extend([int(i) for i in str(val)])

    def bdv(self, opr):
        numerator = self.reg_a
        denominator = 2 ** opr
        val = numerator // denominator
        self.reg_b = val

    def cdv(self, opr):
        numerator = self.reg_a
        denominator = 2 ** opr
        val = numerator // denominator
        self.reg_c = val

    def get_opr(self, value):
        if 0 <= value <= 3:
            return value
        elif value == 4:
            return self.reg_a
        elif value == 5:
            return self.reg_b
        elif value == 6:
            return self.reg_c
        elif value == 7:
            return 7
        else:
            raise Exception(f"ошибка в операторе {value}")

    def perform_operation(self, instruction, int_opr):
        # print(f"{instruction}  ===  {self.output} , reg = {self.reg_a}, {self.reg_b}, {self.reg_c},")
        opr = self.get_opr(int_opr)
        if instruction == 0:
            self.adv(opr)
        elif instruction == 1:
            self.bxl(int_opr)
        elif instruction == 2:
            self.bst(opr)
        elif instruction == 3:
            self.jnz(opr)
        elif instruction == 4:
            self.bxc(opr)
        elif instruction == 5:
            self.out(opr)
        elif instruction == 6:
            self.bdv(opr)
        elif instruction == 7:
            self.cdv(opr)
        else:
            raise Exception(f"ошибка в операции {instruction}")

    def perform_program(self):
        while 0 <= self.ind_operation < len(self.list_operation):
            instruction, int_opr = self.list_operation[self.ind_operation]
            self.perform_operation(instruction, int_opr)
            self.ind_operation +=1


def prob(a, b, c, program):
    test_cl = Computer(a, b, c, program)
    test_cl.perform_program()
    print(test_cl.output)
    print(f"регистр А = {test_cl.reg_a}, регистр В = {test_cl.reg_b}, регистр С = {test_cl.reg_c}")



# print("\nтест1")
# prob(0, 0, 9,[2,6])
# print("\nтест2")
# prob(10, 0, 0, [5,0,5,1,5,4])
# print("\nтест3")
# prob(2024, 0, 0, [0,1,5,4,3,0])
# print("\nтест4")
# prob(0, 29, 0, [1,7])
# print("\nтест5")
# prob(0, 2024, 43690, [4,0])
# print("\nтест6")
# prob(729, 0, 0, [0,1,5,4,3,0])


time_start = time.time()
task1 = Computer(61156655, 0, 0, [2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0])
task1.perform_program()
res_task1 = task1.output
str_res = str(res_task1).replace(" ","")
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 1: {str_res} \n Время Решения:{execution_time}")

def reconstruction(list_pr):
    version_reg_a = [0]
    for i in range(1, len(list_pr)+1):
        new_ver = []
        for num in version_reg_a:
            for tail in range(8):
                ver = 8*num+ tail
                task = Computer(ver, 0, 0, list_pr)
                task.perform_program()
                res_task = task.output
                if res_task == list_pr[-i:]:
                    new_ver.append(ver)
        version_reg_a = new_ver
    return min(version_reg_a)



time_start = time.time()
reg_a = reconstruction([2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0])
time_finish = time.time()
execution_time = time_finish - time_start
print(f"Решение задания 2: {reg_a} \n Время Решения:{execution_time}")








