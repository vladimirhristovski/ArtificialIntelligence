from Midterm_1.searching_framework import *


class Toxic_Pacman(Problem):

    def __init__(self, pacman_1, pacman_2, hospital, walls, width, height):
        super().__init__((pacman_1, (), pacman_2, ()))
        self.width = width
        self.height = height
        self.hospital = hospital
        self.walls = walls

    def goal_test(self, state):
        return state[0] == state[2] == self.hospital

    def check_valid(self, state):
        pacman_1 = state[0]
        pacman_1_trail = state[1]
        pacman_2 = state[2]
        pacman_2_trail = state[3]
        if pacman_1 == pacman_2 == self.hospital:
            # Доколку пакман 1 е на иста позиција со пакман 2 и воедно двата се на позицијата на болницата врати True
            return True
        elif pacman_1 in self.walls or pacman_2 in self.walls or pacman_1 == pacman_2 or pacman_1[0] < 0 or pacman_1[
            0] >= self.width or pacman_1[1] < 0 or pacman_1[1] >= self.height or pacman_2[0] < 0 or pacman_2[
            0] >= self.width or pacman_2[1] < 0 or pacman_2[
            1] >= self.height or pacman_1 in pacman_1_trail or pacman_1 in pacman_2_trail or pacman_2 in pacman_2_trail or pacman_2 in pacman_1_trail:
            # Доколку пакман 1 или пакман 2 се најдат на иста позиција или надвор од дозволениот опсег или во ѕид
            # или во сопствената токсична трага или во токсичната трага на другиот пакман да врати False
            return False
        else:
            # Во спротивно врати True
            return True

    def move_pacman1(self, state, direction, action):
        pacman_1 = list(state[0])
        pacman_1_trail = list(state[1])

        pacman_1[0] += direction[0]
        pacman_1[1] += direction[1]

        if action == "Stop":
            # Доколку акцијата е да остани во место и должината на неговата токсична трага е поголема од 0, намали ја токсичната трага за 1
            if len(pacman_1_trail) > 0:
                pacman_1_trail = pacman_1_trail[1:]
        else:
            # Во спротивно
            if len(pacman_1_trail) < 3:
                # Доколку токсичната трага е со должина помала од 3, зголеми ја трагата за претходната состојба на пакман
                pacman_1_trail.append(state[0])
            elif len(pacman_1_trail) == 3:
                # Доколку токсичната трага е со должина 3, зголеми ја трагата за претходната состојба на пакман, па скрати намли ја токсичната трага за 1
                pacman_1_trail.append(state[0])
                pacman_1_trail = pacman_1_trail[1:]

        check_state = (tuple(pacman_1), tuple(pacman_1_trail), state[2], state[3])

        if self.check_valid(check_state):
            # Проверка дали позициите на пакман се валидни
            return check_state
        else:
            return None

    def move_pacman2(self, state, direction, action):
        pacman_2 = list(state[2])
        pacman_2_trail = list(state[3])

        pacman_2[0] += direction[0]
        pacman_2[1] += direction[1]

        if action == "Stop":
            # Доколку акцијата е да остани во место и должината на неговата токсична трага е поголема од 0, намали ја токсичната трага за 1
            if len(pacman_2_trail) > 0:
                pacman_2_trail = pacman_2_trail[1:]
        else:
            if len(pacman_2_trail) < 3:
                # Доколку токсичната трага е со должина помала од 3, зголеми ја трагата за претходната состојба на пакман
                pacman_2_trail.append(state[2])
            elif len(pacman_2_trail) == 3:
                # Доколку токсичната трага е со должина 3, зголеми ја трагата за претходната состојба на пакман, па скрати намли ја токсичната трага за 1
                pacman_2_trail.append(state[2])
                pacman_2_trail = pacman_2_trail[1:]

        check_state = (state[0], state[1], tuple(pacman_2), tuple(pacman_2_trail))

        if self.check_valid(check_state):
            # Проверка дали позициите на пакман се валидни
            return check_state
        else:
            return None

    def successor(self, state):
        neighbours = dict()

        actions = ("Gore", "Dolu", "Levo", "Desno", "Stop")
        # Дозволени акции за движење

        directions = ((0, +1), (0, -1), (-1, 0), (+1, 0), (0, 0))
        # Дозволени насоки за движење

        for action1, direction1 in zip(actions, directions):
            res1 = self.move_pacman1(state, direction1, action1)
            # Прво го придвижуваме пакман 1
            if res1 is not None:
                # Доколку неговата позиција е валидна продолжуваме тука
                for action2, direction2 in zip(actions, directions):
                    res2 = self.move_pacman2(res1, direction2, action2)
                    # Потоа го придвижуваме пакман 2
                    if res2 is not None:
                        # Конечно, доколку позициите на двата пакмени е валидна да се додаде во речникот со акции
                        neighbours["Pacman_1 : " + action1 + ", Pacman_2 : " + action2] = res2

        return neighbours

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state = node.state
        pacman_1 = state[0]
        pacman_2 = state[2]
        return abs(pacman_1[0] - self.hospital[0]) + abs(pacman_1[1] - self.hospital[1]) + abs(
            pacman_2[0] - self.hospital[0]) + abs(pacman_2[1] - self.hospital[1])


if __name__ == '__main__':
    width = 7
    height = 5
    pacman_1 = (0, 4)
    pacman_2 = (0, 1)
    hospital = (6, 4)
    walls = ((2, 2), (3, 2), (3, 3), (3, 4), (4, 2))

    problem = Toxic_Pacman(pacman_1, pacman_2, hospital, walls, width, height)
    node = astar_search(problem)

    if node is not None:
        print(node.solution())
    else:
        print("A solution was not found!")
