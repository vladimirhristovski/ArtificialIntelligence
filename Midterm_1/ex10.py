class Agent:
    def __init__(self, x, y):
        self.pos_x = int(x)
        self.pos_y = int(y)

    def move_left(self):
        self.pos_x -= 1
        self.get_coordinates()

    def move_right(self):
        self.pos_x += 1
        self.get_coordinates()

    def move_upward(self):
        self.pos_y += 1
        self.get_coordinates()

    def move_downward(self):
        self.pos_y -= 1
        self.get_coordinates()

    def get_coordinates(self):
        print("X: "+str(self.pos_x)+" Y: "+str(self.pos_y))

if __name__ == '__main__':
    player=Agent(1,1)
    player.move_right()
    player.move_upward()
    player.move_right()
    player.move_downward()
    player.move_downward()

