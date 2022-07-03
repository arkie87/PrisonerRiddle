import random


def get_boxes(N):
    choices = [i for i in range(N)]
    order = []
    for i in range(N):
        choice = random.choice(choices)
        choices.pop(choices.index(choice))
        order += [choice]
    return order


def playone(i, boxes):
    b = i
    for j in range(len(boxes) // 2):
        b = boxes[b]
        if i == b:
            return True
    else:
        return False


def play(N):
    boxes = get_boxes(N)
    for i in range(N):
        result = playone(i, boxes)
        if not result:
            return False
    else:
        return True


s = 0
for i in range(100000):
    result = play(100)
    if result:
        s += 1
