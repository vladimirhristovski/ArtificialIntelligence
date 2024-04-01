from Midterm_1.searching_framework import *


class Football(Problem):

    def __init__(self, player, ball):
        super().__init__((player, ball))
        self.columns = 8
        self.rows = 6
        self.opponent1 = ((2, 2), (3, 2), (4, 2), (2, 3), (3, 3), (4, 3), (2, 4), (3, 4), (4, 4))
        self.opponent2 = ((4, 3), (5, 3), (6, 3), (4, 4), (5, 4), (6, 4), (4, 5), (5, 5), (6, 5))
        self.goal = ((7, 2), (7, 3))

    def goal_test(self, state):
        return state[1] in self.goal

    def check_valid(self, state):
        new_state = list(state)
        player = new_state[0]
        ball = new_state[1]
        if player == (3, 3) or player == (
                5, 4) or player == ball or ball in self.opponent1 or ball in self.opponent2 or not 0 <= player[
            0] < self.columns or not 0 <= player[1] < self.rows or not 0 <= ball[0] < self.columns or not 0 <= ball[
            1] < self.rows:
            return None
        return state

    def check_if_player_is_around_ball(self, state):
        new_state = list(state)
        player = new_state[0]
        ball = list(new_state[1])
        ball_space = ((ball[0] - 1, ball[1] - 1), (ball[0], ball[1] - 1),
                      (ball[0] - 1, ball[1]), (ball[0] - 1, ball[1] + 1), (ball[0], ball[1] + 1))
        return player in ball_space

    def move_player(self, state, direction):
        new_state = list(state)
        player = list(new_state[0])
        player[0] += direction[0]
        player[1] += direction[1]

        new_state = (tuple(player), state[1])

        return self.check_valid(new_state)

    def move_player_with_ball(self, state, direction):
        new_state = list(state)
        player = list(new_state[0])
        ball = list(new_state[1])

        if player == [ball[0] + direction[0] * -1, ball[1] + direction[1] * -1]:
            player[0] = ball[0]
            player[1] = ball[1]
            ball[0] += direction[0]
            ball[1] += direction[1]
            updated_state = (tuple(player), tuple(ball))
            return self.check_valid(updated_state)
        return None

    def successor(self, state):

        neighbours = dict()

        actions_player = (
            "Pomesti coveche gore", "Pomesti coveche dolu", "Pomesti coveche desno", "Pomesti coveche gore-desno",
            "Pomesti coveche dolu-desno")

        actions_ball = ("Turni topka gore", "Turni topka dolu", "Turni topka desno", "Turni topka gore-desno",
                        "Turni topka dolu-desno")

        directions = ((0, +1), (0, -1), (+1, 0), (+1, +1), (+1, -1))

        if self.check_if_player_is_around_ball(state):
            for action, direction in zip(actions_player, directions):
                res = self.move_player(state, direction)
                if res is not None:
                    neighbours[action] = res
            for action, direction in zip(actions_ball, directions):
                res = self.move_player_with_ball(state, direction)
                if res is not None:
                    neighbours[action] = res
        else:
            for action, direction in zip(actions_player, directions):
                res = self.move_player(state, direction)
                if res is not None:
                    neighbours[action] = res

        return neighbours

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    player = tuple(map(int, input().split(",")))
    ball = tuple(map(int, input().split(",")))

    problem = Football(player, ball)
    node = depth_first_graph_search(problem)

    if node is not None:
        print(node.solution())
    else:
        print("No solution found!")
