from constraint import *


def check_col(*items):
    col_constraints = [3, 4, 10, 3]

    sum = 0
    num = 1
    con = 0
    for i in range(len(items)):
        if items[i] == 1:
            sum += num
        num += 1
        if num == 5:
            if sum != col_constraints[con]:
                return False
            sum = 0
            num = 1
            con += 1

    # sum1 = 0
    # num1 = 1
    # for i in range(4):
    #     if items[i] == 1:
    #         sum1 += num1
    #     num1 += 1
    # if sum1 != 3:
    #     return False
    #
    # sum2 = 0
    # num2 = 1
    # for i in range(4, 8):
    #     if items[i] == 1:
    #         sum2 += num2
    #     num2 += 1
    # if sum2 != 4:
    #     return False
    # #
    # sum3 = 0
    # num3 = 1
    # for i in range(8, 12):
    #     if items[i] == 1:
    #         sum3 += num3
    #     num3 += 1
    # if sum3 != 10:
    #     return False
    #
    # sum4 = 0
    # num4 = 1
    # for i in range(12, 16):
    #     if items[i] == 1:
    #         sum4 += num4
    #     num4 += 1
    # if sum4 != 3:
    #     return False
    #
    return True


def check_row(*items):
    row_constraints = [7, 7, 4, 5]

    sum = 0
    num = 1
    con = 0
    for i in range(len(items)):
        if items[i] == 1:
            sum += num
        num += 1
        if num == 5:
            if sum != row_constraints[con]:
                return False
            sum = 0
            num = 1
            con += 1

    # sum1 = 0
    # num1 = 1
    # for i in range(4):
    #     if items[i] == 1:
    #         sum1 += num1
    #     num1 += 1
    # if sum1 != 7:
    #     return False
    #
    # sum2 = 0
    # num2 = 1
    # for i in range(4, 8):
    #     if items[i] == 1:
    #         sum2 += num2
    #     num2 += 1
    # if sum2 != 7:
    #     return False
    # #
    # sum3 = 0
    # num3 = 1
    # for i in range(8, 12):
    #     if items[i] == 1:
    #         sum3 += num3
    #     num3 += 1
    # if sum3 != 4:
    #     return False
    #
    # sum4 = 0
    # num4 = 1
    # for i in range(12, 16):
    #     if items[i] == 1:
    #         sum4 += num4
    #     num4 += 1
    # if sum4 != 5:
    #     return False

    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = []

    for i in range(1, 5):
        for j in range(1, 5):
            variables.append((i, j))
            problem.addVariable((i, j), [0, 1])

    row_check = []
    for row in range(1, 5):
        for col in range(1, 5):
            row_check.append((row, col))
    problem.addConstraint(check_row, row_check)

    col_check = []
    for col in range(1, 5):
        for row in range(1, 5):
            col_check.append((row, col))
    problem.addConstraint(check_col, col_check)

    solution = problem.getSolution()

    for row in range(1, 5):
        for col in range(1, 5):
            print(solution[(row, col)], end="\t")
        print()
