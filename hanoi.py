def move(no, x, y):
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'Move disk [{no}] from {x} to {y}')

    if no > 1:
        move(no - 1, 6 - x - y, y)

move(5, 1, 3)
