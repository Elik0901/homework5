import random


def bet(slot, amount):
    slots = list(range(1, 31))
    win_slot = random.choice(slots)
    if slot == win_slot:
        print('YOU WIN')
        return amount * 2
    else:
        print('YOU LOSE')
        return -amount
