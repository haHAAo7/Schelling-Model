import random
import re


red_color = "\x1b[6;30;41m"
blue_color = "\x1b[2;31;44m"
size = 40  # размер сетки
iters = 400000  # кол-во итераций
a = []


def test_happy(a, x, y, size):
    c = a[x][y]
    t = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            x1 = x + j
            y1 = y + i
            if (y1 >= 0) & (y1 < size) & (x1 >= 0) & (x1 < size) & ((i != 0) or (j != 0)):
                if a[y1][x1] == c:
                    t += 1
    return t >= 4


def print_field(f, size):
    for i in range(size):
        for j in range(size):
            if a[i][j] == 1:
                print(red_color, end='')
            elif a[i][j] == 2:
                print(blue_color, end='')
            elif a[i][j] == 0:
                print("\x1b[0m", end='')
            print(re.sub('[0-2]', " ", str(a[i][j])), end=' ')
        print("\x1b[0m", end='')
        print('')


def get_random_empty(a, size):
    while True:
        i = random.randrange(0, size)
        j = random.randrange(0, size)
        if a[i][j] == 0:
            return i, j


def get_unhappy(a, size):
    while True:
        i = random.randrange(0, size)
        j = random.randrange(0, size)
        if not test_happy(a, i, j, size):
            return i, j


for i in range(size):
    b = []
    for j in range(size):
        q = random.randrange(0, 100)
        p = 0
        if q < 45:
            p = 1
        elif q < 90:
            p = 2
        b.append(p)
    a.append(b)
print_field(a, size)
for k in range(iters):
    y, x = get_unhappy(a, size)
    i2, j2 = get_random_empty(a, size)
    a[i2][j2] = a[y][x]
    a[y][x] = 0
print("\n")
print_field(a, size)

