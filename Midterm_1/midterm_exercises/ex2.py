from constraint import *


def check_valid(*vars):
    x = 1000 * vars[0] + 100 * vars[1] + 10 * vars[2] + vars[3]
    y = 1000 * vars[-4] + 100 * vars[-3] + 10 * vars[-2] + vars[1]
    res = 10000 * vars[-4] + 1000 * vars[-3] + 100 * vars[2] + 10 * vars[1] + vars[-1]
    return x + y == res


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(AllDifferentConstraint(),variables)
    problem.addConstraint(check_valid, variables)

    # ----------------------------------------------------

    print(problem.getSolution())
