import random


class Game:
    def __init__(self, N):
        self.N = N
        self.guesses = N // 2
        self.shuffle_boxes()

    def shuffle_boxes(self):
        boxes = list(range(self.N))
        random.shuffle(boxes)
        self.boxes = boxes

    def play_one(self, player):
        box = player
        for _ in range(self.guesses):
            box = self.boxes[box]
            if player == box:
                return True
        else:
            return False

    def play(self):
        for player in range(self.N):
            result = self.play_one(player)
            if not result:
                return False
        else:
            return True


def test():
    s = 0
    n = 100
    N = 100000
    for _ in range(N):
        game = Game(n)
        result = game.play()
        if result:
            s += 1

    print(f"Success Rate: {round(s/N*100, 2)}%")


test()
