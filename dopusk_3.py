# Промоделировать работу Марковской цепи с одним поглощающим состоянием из трех.
# Путем моделирования оценить среднее время достижения поглощающего состояния и
# вычислить его теоретически.
# Пока не доделала


import random
import matplotlib.pyplot as plt
import numpy as np

ro = [[0.7, 0.2999, 0.0001],
      [0.6, 0.2999, 0.1001],
      [0, 0, 1]]

t22 = 0
t12 = (ro[2][0] * (1 + ro[0][0] + ro[0][1] + ro[0][2]) + ro[1][1] * (1 - ro[0][0]) + ro[1][2] * (1 - ro[0][0])) / (
        1 - ro[0][0] - ro[1][1] + ro[1][1] * ro[0][0])
t02 = (ro[0][0] + ro[0][1] * (1 + t12) + ro[0][2]) / (1 - ro[0][0])

print("Среднее время достижения поглощения (теория) (0): ", + t02)
print("Среднее время достижения поглощения (теория) (1): ", + t12)

cur_state = 0
T = 1000
time0 = 0
time1 = 0
for j in range(0, T):
    c = random.random()
    if cur_state == 0:
        if c < ro[0][0]:
            cur_state = 0
            time0 = time0 + 1
        elif ro[0][0] < c < (ro[0][0] + ro[0][1]):
            cur_state = 1
            time1 = time1 + 1
        else:
            cur_state = 2
            break
    elif cur_state == 1:
        if c < ro[1][0]:
            cur_state = 0
            time0 = time0 + 1
        elif ro[1][0] < c < (ro[1][0] + ro[1][1]):
            cur_state = 1
            time1 = time1 + 1
        else:
            cur_state = 2
            break
    else:
        break
print("Практика (0): ", + (time0 / T))
print("Практика (1): ", + (time1 / T))
