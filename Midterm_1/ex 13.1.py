from searching_framework import *


class Beakers(Problem):
    def __init__(self, capacity, goal, initial):
        super().__init__(initial, goal)
        self.capacity = capacity

    def successor(self, state):
        neighbours = dict()

        res1 = self.empty(state, 0)
        if res1 is not None:
            neighbours["Empty_from_1"] = res1

        res2 = self.empty(state, 1)
        if res2 is not None:
            neighbours["Empty_from_2"] = res2

        res3 = self.transfer(state, 0, 1)
        if res3 is not None:
            neighbours["Transfer_from_1_to_2"] = res3

        res4 = self.transfer(state, 1, 0)
        if res4 is not None:
            neighbours["Transfer_from_2_to_1"] = res4

        return neighbours

    def empty(self, state, idx):
        if state[idx] == 0:
            return None

        updated_state = list(state)
        updated_state[idx] -= 1

        return tuple(updated_state)

    def transfer(self, state, idx_from, idx_to):
        if state[idx_from] == 0 or state[idx_to] == self.capacity[idx_to]:
            return None

        updated_state = list(state)
        updated_state[idx_from] -= 1
        updated_state[idx_to] += 1

        return tuple(updated_state)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


""" example:
12 8 - capacity first beaker and second beaker
6 4 - goal how much should they be filled
8 3 -  initial how much are they filled now
"""

if __name__ == '__main__':

    capacity = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    initial = tuple(map(int, input().split()))

    problem = Beakers(capacity, goal, initial)

    node = breadth_first_graph_search(problem)

    if node is not None:
        print(node)
        print(node.solution())
        print(node.path())
        print(node.solve())
    else:
        print("No solution found!")
