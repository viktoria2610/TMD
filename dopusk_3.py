# Промоделировать работу Марковской цепи с одним поглощающим состоянием из трех.
# Путем моделирования оценить среднее время достижения поглощающего состояния и
# вычислить его теоретически.


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
time_theoretical = np.linalg.inv(current_matrix).dot(vectorB)
time_theoretical = np.delete(time_theoretical, [2, 2])
print(time_theoretical)


# Практика

def function(ro, n, T, state):
    time = 0
    for i in range(0, n):
        cur_state = state
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
                    break
            elif cur_state == 1:
                if c < ro[1][0]:
                    cur_state = 0
                    time = time + 1
                elif ro[1][0] < c < (ro[1][0] + ro[1][1]):
                    cur_state = 1
                    time = time + 1
                else:
                    break
            else:
                break
    return time / n


T = 1000000
n = 100000
print("Практическое значение времени при state = 0: ", + function(ro, n, T, 0))
print("Практическое значение времени при state = 1: ", + function(ro, n, T, 1))