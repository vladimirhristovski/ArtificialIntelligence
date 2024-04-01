from Midterm_1.searching_framework import Problem, astar_search


class Labyrinth(Problem):
    def __init__(self, n, walls, explorer, house):
        super().__init__(explorer, house)
        self.size = n
        self.walls = walls

    def move(self, state, direction, action):
        explorer = list(state)

        if "Desno" not in action:
            explorer[0] += direction[0]
            explorer[1] += direction[1]
        else:
            for i in range(direction[0]):
                tmp = list(state)
                tmp[0] += i
                if tuple(tmp) in self.walls or tmp[0] < 0 or tmp[0] >= self.size or tmp[1] < 0 or tmp[1] >= self.size:
                    return None

            explorer[0] += direction[0]
            explorer[1] += direction[1]

        if tuple(explorer) in self.walls or explorer[0] < 0 or explorer[0] >= self.size or explorer[1] < 0 or \
                explorer[1] >= self.size:
            return None

        return tuple(explorer)

    def successor(self, state):

        neighbours = dict()

        actions = ("Desno 2", "Desno 3", "Gore", "Dolu", "Levo")

        directions = ((+2, 0), (+3, 0), (0, +1), (0, -1), (-1, 0))

        for action, direction in zip(actions, directions):
            res = self.move(state, direction, action)
            if res is not None:
                neighbours[action] = res

        return neighbours

    def h(self, node):
        explorer = node.state
        return (abs(explorer[0] - self.goal[0]) + abs(explorer[1] - self.goal[1])) / 3

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    n = int(input())
    wall_num = int(input())
    walls = []
    for i in range(wall_num):
        walls.append(tuple(map(int, input().split(","))))
    explorer = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))

    problem = Labyrinth(n, tuple(walls), explorer, house)

    node = astar_search(problem)

    if node is not None:
        print(node.solution())
    else:
        print("A solution was not found!")
