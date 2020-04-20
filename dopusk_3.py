# Промоделировать работу Марковской цепи с одним поглощающим состоянием из трех.
# Путем моделирования оценить среднее время достижения поглощающего состояния и
# вычислить его теоретически.
# Пока не доделала


import random
import matplotlib.pyplot as plt
import numpy as np

ro = [[0.7, 0.29, 0.01],
      [0.5, 0.3333, 0.1667],
      [0, 0, 1]]

ro = np.array(ro)
vectorB = np.array([1, 1, 1])
current_matrix = -ro
current_matrix[0][0] = 1 - ro[0][0]
current_matrix[1][1] = 1 - ro[1][1]
print(np.linalg.inv(current_matrix).dot(vectorB)[1])


# Практика

T = 1000000
n = 100000
time = 0
for i in range(0, n):
    cur_state = 1
    for j in range(0, T):
        c = random.random()
        if cur_state == 0:
            if c < ro[0][0]:
                cur_state = 0
                time = time + 1
            elif ro[0][0] < c < (ro[0][0] + ro[0][1]):
                cur_state = 1
                time = time + 1
            else:
                cur_state = 2
                break
        elif cur_state == 1:
            if c < ro[1][0]:
                cur_state = 0
                time = time + 1
            elif ro[1][0] < c < (ro[1][0] + ro[1][1]):
                cur_state = 1
                time = time + 1
            else:
                cur_state = 2
                break
        else:
            break
print("Практика (0): ", + (time / n))
