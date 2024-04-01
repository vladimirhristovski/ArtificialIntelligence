from constraint import *


def check_valid(*items):
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0

    for item in items:
        if item == "T1":
            t1 += 1
        if item == "T2":
            t2 += 1
        if item == "T3":
            t3 += 1
        if item == "T4":
            t4 += 1
    if 0 <= t1 <= 4 and 0 <= t2 <= 4 and 0 <= t3 <= 4 and 0 <= t4 <= 4:
        return True
    else:
        return False


def print_info(solution):
    # print(solution)
    sorted_solution = sorted(solution)
    papers = []
    lectures = []
    time = []
    for s in sorted_solution:
        papers.append(s.split("_")[0])
        lectures.append(s.split("_")[1])
        time.append(solution[s])
    for i in range(1, len(sorted_solution)):
        print(f'{papers[i]} ({lectures[i]}): {time[i]}')
    print(f'{papers[0]} ({lectures[0]}): {time[0]}')


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = []

    AI_papers = []
    ML_papers = []
    NLP_papers = []

    for paper in papers:
        variables.append(f'{paper}_{papers[paper]}')
        if papers[paper] == "NLP":
            NLP_papers.append(f'{paper}_{papers[paper]}')
        if papers[paper] == "ML":
            ML_papers.append(f'{paper}_{papers[paper]}')
        if papers[paper] == "AI":
            AI_papers.append(f'{paper}_{papers[paper]}')

    # print(variables)
    # print(AI_papers, ML_papers, NLP_papers)

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata

    if 0 < len(AI_papers) <= 4:
        problem.addConstraint(AllEqualConstraint(), AI_papers)
    if 0 < len(ML_papers) <= 4:
        problem.addConstraint(AllEqualConstraint(), ML_papers)
    if 0 < len(NLP_papers) <= 4:
        problem.addConstraint(AllEqualConstraint(), NLP_papers)
    problem.addConstraint(check_valid, variables)

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    print_info(result)
