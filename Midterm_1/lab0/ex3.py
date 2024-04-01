import os
import random

os.environ["OPENBLAS_NUM_THREADS"] = "1"
random.seed(0)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, position):
        if position == 0:  # move left
            self.y -= 1
        if position == 1:  # move up
            self.x -= 1
        if position == 2:  # move right
            self.y += 1
        if position == 3:  # move down
            self.x += 1

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x_y(self, x, y):
        self.x = x
        self.y = y


class Game:
    def __init__(self, m, n, matrix, points):
        self.m = m
        self.n = n
        self.matrix = matrix
        self.points = points

    def get_points(self):
        return self.points

    def set_points(self):
        self.points -= 1

    def get_m(self):
        return self.m

    def get_n(self):
        return self.n

    def get_matrix(self):
        return self.matrix


class Pacman:
    def __init__(self, m, n, matrix, points):
        self.player = Player(0, 0)
        self.game = Game(m, n, matrix, points)

    def play_game(self):
        player_x = self.player.get_x()
        player_y = self.player.get_y()
        game_m = self.game.get_m()
        game_n = self.game.get_n()
        game_matrix = self.game.get_matrix()
        current_game_points = self.game.get_points()
        if current_game_points == 0:
            print("Nothing to do here")
            return

        while current_game_points > 0:
            if player_y - 1 >= 0 and game_matrix[player_x][player_y - 1] == ".":  # left
                self.player.move(0)
                player_x = self.player.get_x()
                player_y = self.player.get_y()
                self.game.set_points()
                game_matrix[player_x][player_y] = "#"
                current_game_points = self.game.get_points()
                print("[" + str(self.player.get_x()) + ", " + str(self.player.get_y()) + "]")
                # print(self.game.get_points())
            elif player_y + 1 < game_n and game_matrix[player_x][player_y + 1] == ".":  # right
                self.player.move(2)
                player_x = self.player.get_x()
                player_y = self.player.get_y()
                self.game.set_points()
                game_matrix[player_x][player_y] = "#"
                current_game_points = self.game.get_points()
                print("[" + str(self.player.get_x()) + ", " + str(self.player.get_y()) + "]")
                # print(self.game.get_points())
            elif player_x + 1 < game_m and game_matrix[player_x + 1][player_y] == ".":  # down
                self.player.move(3)
                player_x = self.player.get_x()
                player_y = self.player.get_y()
                self.game.set_points()
                game_matrix[player_x][player_y] = "#"
                current_game_points = self.game.get_points()
                print("[" + str(self.player.get_x()) + ", " + str(self.player.get_y()) + "]")
                # print(self.game.get_points())
            elif player_x - 1 >= 0 and game_matrix[player_x - 1][player_y] == ".":  # up
                self.player.move(1)
                player_x = self.player.get_x()
                player_y = self.player.get_y()
                self.game.set_points()
                game_matrix[player_x][player_y] = "#"
                current_game_points = self.game.get_points()
                print("[" + str(self.player.get_x()) + ", " + str(self.player.get_y()) + "]")
                # print(self.game.get_points())
            else:  # random
                self.find_next_move()
                player_x = self.player.get_x()
                player_y = self.player.get_y()
                print("[" + str(self.player.get_x()) + ", " + str(self.player.get_y()) + "]")
                # print(self.game.get_points())

    def find_next_move(self):
        self.player.move(random.randint(0, 3))
        if self.player.get_x() < 0:
            self.player.set_x_y(self.player.get_x() + 1, self.player.get_y())
            return Pacman.find_next_move(self)
        if self.player.get_y() < 0:
            self.player.set_x_y(self.player.get_x(), self.player.get_y() + 1)
            return Pacman.find_next_move(self)
        if self.player.get_x() == self.game.get_m():
            self.player.set_x_y(self.player.get_x() - 1, self.player.get_y())
            return Pacman.find_next_move(self)
        if self.player.get_y() == self.game.get_n():
            self.player.set_x_y(self.player.get_x(), self.player.get_y() - 1)
            return Pacman.find_next_move(self)


if __name__ == "__main__":
    input_m = int(input())
    input_n = int(input())
    input_matrix = []
    game_points = 0
    for i in range(int(input_m)):
        input_matrix.append(list(input()))
        for j in range(len(input_matrix[i])):
            if input_matrix[i][j] == ".":
                game_points += 1

    pacman = Pacman(input_m, input_n, input_matrix, game_points)
    pacman.play_game()
