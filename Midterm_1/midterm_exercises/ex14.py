from constraint import *


def check_valid(p1, p2, p3, t):
    simona_time = [13, 14, 16, 19]
    marija_time = [14, 15, 18]
    petar_time = [12, 13, 16, 17, 18, 19]

    if 2 >= int(p2) + int(p3) >= 1 == int(p1):
        if t not in simona_time:
            return False
        if int(p2) == 1 and t not in marija_time:
            return False
        if int(p3) == 1 and t not in petar_time:
            return False
    else:
        return False

    return True


def print_solution(solution):
    info = dict()
    info["Simona_prisustvo"] = solution['Simona_prisustvo']
    info["Marija_prisustvo"] = solution['Marija_prisustvo']
    info["Petar_prisustvo"] = solution['Petar_prisustvo']
    info["vreme_sostanok"] = solution['vreme_sostanok']

    print(info)


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----

    variables = []

    # Simona
    problem.addVariable("Simona_prisustvo", [0, 1])
    variables.append("Simona_prisustvo")

    # Marija
    problem.addVariable("Marija_prisustvo", [0, 1])
    variables.append("Marija_prisustvo")

    # Petar
    problem.addVariable("Petar_prisustvo", [0, 1])
    variables.append("Petar_prisustvo")

    # Vreme
    problem.addVariable("vreme_sostanok", list(range(12, 21)))
    variables.append("vreme_sostanok")
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(check_valid, [variables[0], variables[1], variables[2], variables[3]])

    # ----------------------------------------------------

    [print_solution(solution) for solution in problem.getSolutions()]
