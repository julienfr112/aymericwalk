import numpy as np
import turtle
import random

M = np.zeros(shape=(1000, 1000))
M[499][499] = 1

turtle.speed(0)
turtle.pensize(2)

abcd = list(range(4))


def donne_chemin(n, i, j):
    print(n, i, j)
    # turtle.speed(0)
    # turtle.pensize(2)
    # while n != 0:
    random.shuffle(abcd)
    for a in abcd:
        if a == 0 and M[i][j + 1] != 1:
            turtle.setheading(0)
            turtle.forward(3)
            M[i][j + 1] = 1
            M[i - 1][j] = 1
            M[i + 1][j] = 1
            return donne_chemin(n - 1, i, j + 1)

        if a == 1 and M[i - 1][j] != 1:
            turtle.setheading(90)
            turtle.forward(3)
            M[i - 1][j] = 1
            return donne_chemin(n - 1, i - 1, j)

        if a == 2 and M[i][j - 1] != 1:
            turtle.setheading(180)
            turtle.forward(3)
            M[i][j - 1] = 1
            return donne_chemin(n - 1, i, j - 1)

        if a == 3 and M[i + 1][j] != 1:
            turtle.setheading(270)
            turtle.forward(3)
            M[i + 1][j] = 1
            return donne_chemin(n - 1, i + 1, j)


donne_chemin(500, 499, 499)
import time
time.sleep(1)
