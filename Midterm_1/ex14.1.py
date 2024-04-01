from searching_framework import *


class Explorer(Problem):
    def __init__(self, initial, goal):
        super().__init__((initial, (2, 5, -1), (5, 0, +1)))
        self.house = goal
        self.rows = 6
        self.columns = 8

    def goal_test(self, state):
        return state[0] == self.house

    def check_state(self, state):
        explorer, block1, block2 = state
        x, y = explorer
        return 0 <= x < self.columns and 0 <= y < self.rows and explorer != block1[:2] and explorer != block2[:2]

    def move_explorer(self, explorer, direction):
        explorer = list(explorer)
        explorer[0] += direction[0]
        explorer[1] += direction[1]

        return tuple(explorer)

    def move_block(self, block):
        x, y, d = block
        y += d
        if y >= self.rows or y < 0:
            d *= -1
            y += 2 * d

        return x, y, d

    def move(self, state, direction):
        explorer = self.move_explorer(state[0], direction)
        block1 = self.move_block(state[1])
        block2 = self.move_block(state[2])

        updated_state = (explorer, block1, block2)

        if self.check_state(updated_state):
            return updated_state
        else:
            return None

    def successor(self, state):
        neighbours = dict()

        sides = ("Move_right", "Move_left", "Move_up", "Move_down")
        coordinates = ((+1, 0), (-1, 0), (0, +1), (0, -1))

        for side, coordinate in zip(sides, coordinates):
            res = self.move(state, coordinate)
            if res is not None:
                neighbours[side] = res

        return neighbours

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


""" example:
0 2 - initial position of explorer
7 4 - goal position of house
"""

if __name__ == '__main__':
    initial = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))

    problem = Explorer(initial, goal)
    node = breadth_first_graph_search(problem)

    if node is not None:
        print(node)
        print(node.solve())
        print(node.solution())
        print(node.path())
    else:
        print("Solution not found!")
