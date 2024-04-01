from constraint import *


def grouped_by_four(*variables):
    num_termini = {"T1": 0, "T2": 0, "T3": 0, "T4": 0}

    for variable in variables:
        num_termini[variable] = num_termini[variable] + 1

    return num_termini["T1"] <= 4 and num_termini["T2"] <= 4 and num_termini["T3"] <= 4 \
        and num_termini["T4"] <= 4


def printSolution(solution):
    papers = sorted(solution)

    terms = []

    for value in papers:
        terms.append(solution[value])

    print(f"{papers[0][0]} ({papers[0][1]}): {terms[0]}")
    for i in range(2, len(papers)):
        print(f"{papers[i][0]} ({papers[i][1]}): {terms[i]}")
    print(f"{papers[1][0]} ({papers[1][1]}): {terms[1]}")


if __name__ == '__main__':
    num = int(input())

    papers = dict()
    variables = []

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()
        variables.append((title, topic))

    # Tuka definirajte gi promenlivite
    ...

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())
    AI_papers = []
    ML_papers = []
    NLP_papers = []

    for variable in variables:
        if variable[1] == "AI":
            AI_papers.append(variable)
        elif variable[1] == "ML":
            ML_papers.append(variable)
        else:
            NLP_papers.append(variable)

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    if len(AI_papers) > 0 and len(AI_papers) <= 4:
        problem.addConstraint(AllEqualConstraint(), AI_papers)
    if len(ML_papers) > 0 and len(ML_papers) <= 4:
        problem.addConstraint(AllEqualConstraint(), ML_papers)
    if len(NLP_papers) > 0 and len(NLP_papers) <= 4:
        problem.addConstraint(AllEqualConstraint(), NLP_papers)

    problem.addConstraint(grouped_by_four, variables)

    result = problem.getSolution()

    printSolution(result)
