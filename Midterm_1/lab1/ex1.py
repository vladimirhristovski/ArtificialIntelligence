from Midterm_1.searching_framework import *


class Snake(Problem):

    def __init__(self, red_apples, green_apples):
        super().__init__((((0, 9), (0, 8), (0, 7)), "d", green_apples))
        self.size = 10
        self.red_apples = red_apples

    def goal_test(self, state):
        return len(state[2]) == 0

    def apple_check(self, state):
        updated_state = list(state)
        snake = list(updated_state[0])
        green_apples = list(updated_state[2])
        snake_length = len(snake) - 1

        if snake[snake_length] in green_apples:
            for apple in green_apples:
                if snake[snake_length] == apple:
                    green_apples.remove(apple)
                    new_state = (tuple(snake), state[1], tuple(green_apples))
                    return new_state
        new_state = (tuple(snake[1:]), state[1], state[2])
        return new_state

    def move_snake(self, state, direction, action):

        # new_state = list(state)
        updated_snake = list(state[0])
        updated_snake_head = list(updated_snake[-1])
        updated_snake_head[0] += direction[0]
        updated_snake_head[1] += direction[1]

        # if not 0 <= updated_snake_head[0] < self.size or not 0 <= updated_snake_head[1] < self.size or tuple(
        #         updated_snake_head) in updated_snake or tuple(updated_snake_head) in self.red_apples:
        #     return None

        if not 0 <= updated_snake_head[0] < self.size or not 0 <= updated_snake_head[1] < self.size:
            return None

        if tuple(updated_snake_head) in self.red_apples:
            return None

        if tuple(updated_snake_head) in updated_snake[1:]:
            return None

        current_direction = state[1]

        if action != "ProdolzhiPravo":
            if action == "SvrtiDesno":
                if current_direction == "l":
                    current_direction = "u"
                elif current_direction == "r":
                    current_direction = "d"
                elif current_direction == "u":
                    current_direction = "r"
                elif current_direction == "d":
                    current_direction = "l"
            elif action == "SvrtiLevo":
                if current_direction == "l":
                    current_direction = "d"
                elif current_direction == "r":
                    current_direction = "u"
                elif current_direction == "u":
                    current_direction = "l"
                elif current_direction == "d":
                    current_direction = "r"

        updated_snake.append(tuple(updated_snake_head))

        updated_state = (tuple(updated_snake), current_direction, state[2])

        return self.apple_check(updated_state)

    def successor(self, state):
        neighbours = dict()

        actions = ("ProdolzhiPravo", "SvrtiDesno", "SvrtiLevo")

        current_direction = state[1]

        if current_direction == "l":
            directions = ((-1, 0), (0, +1), (0, -1))
            for action, direction in zip(actions, directions):
                res = self.move_snake(state, direction, action)
                if res is not None:
                    neighbours[action] = res
        if current_direction == "r":
            directions = ((+1, 0), (0, -1), (0, +1))
            for action, direction in zip(actions, directions):
                res = self.move_snake(state, direction, action)
                if res is not None:
                    neighbours[action] = res
        if current_direction == "u":
            directions = ((0, +1), (+1, 0), (-1, 0))
            for action, direction in zip(actions, directions):
                res = self.move_snake(state, direction, action)
                if res is not None:
                    neighbours[action] = res
        if current_direction == "d":
            directions = ((0, -1), (-1, 0), (+1, 0))
            for action, direction in zip(actions, directions):
                res = self.move_snake(state, direction, action)
                if res is not None:
                    neighbours[action] = res

        return neighbours

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    number_of_green_apples = int(input())
    green_apples = []
    for i in range(number_of_green_apples):
        green_apples.append(tuple(map(int, input().split(","))))

    number_of_red_apples = int(input())
    red_apples = []
    for i in range(number_of_red_apples):
        red_apples.append(tuple(map(int, input().split(","))))

    problem = Snake(tuple(red_apples), tuple(green_apples))
    node = breadth_first_graph_search(problem)
    # print(node.solution())

    if node is not None:
        print(node.solution())
    # print(node)
    else:
        print("A solution was not found!")
