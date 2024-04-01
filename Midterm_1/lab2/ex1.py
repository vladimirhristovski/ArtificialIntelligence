from Midterm_1.searching_framework import Problem, astar_search


class Climber(Problem):

    def __init__(self, climber, house, dir, boulders, width, height):
        super().__init__((climber, house, dir))
        self.boulders = boulders
        self.width = width
        self.height = height

    def goal_test(self, state):
        return state[0] == state[1]

    def move(self, state, direction):
        climber = list(state[0])
        house = list(state[1])
        house_dir = state[2]

        climber[0] += direction[0]
        climber[1] += direction[1]

        if house_dir == "desno":
            house[0] += 1
            if house[0] == self.width:
                house[0] -= 2
                house_dir = "levo"
        elif house_dir == "levo":
            house[0] -= 1
            if house[0] == -1:
                house[0] += 2
                house_dir = "desno"

        if tuple(climber) != tuple(house):
            if tuple(climber) not in self.boulders or climber[0] < 0 or climber[0] >= self.width or climber[1] < 0 or \
                    climber[1] >= self.height:
                return None

        new_state = (tuple(climber), tuple(house), house_dir)

        return new_state

    def successor(self, state):
        neighbours = dict()

        actions = ("Stoj", "Gore 1", "Gore 2", "Gore-desno 1", "Gore-desno 2", "Gore-levo 1", "Gore-levo 2")

        directions = ((0, 0), (0, +1), (0, +2), (+1, +1), (+2, +2), (-1, +1), (-2, +2))

        for action, direction in zip(actions, directions):
            res = self.move(state, direction)
            if res is not None:
                neighbours[action] = res

        return neighbours

    def h(self, node):
        climber = node.state[0]
        house = node.state[1]

        return abs(house[1] - climber[1]) / 2

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    climber = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))
    house_dir = input()

    problem = Climber(climber, house, house_dir, tuple(allowed), 5, 9)

    node = astar_search(problem)

    # print(node.solution())

    if node is not None:
        print(node.solution())
    else:
        print("A solution was not found!")
