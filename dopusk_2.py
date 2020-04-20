# Смоделировать работу Марковской цепи с тремя состояниями. Оценить при помощи
# моделирования стационарное распределение и сравнить с теоретическим расчетом.
import random
import matplotlib.pyplot as plt
import numpy as np


ro = [[0.8, 0.2, 0],
      [0.3, 0.35, 0.35],
      [0, 0.7, 0.3]]
count0 = 0
count1 = 0
count2 = 0
cur_state = 0  # состояние 0
T = 100000

#Теория
vectorB = np.array([0, 0, 1])
ro_transpose = np.transpose(ro)
ro_transpose[0, 0] -= 1
ro_transpose[1, 1] -= 1
ro_transpose[2] = np.array([1, 1, 1])
ro_I = np.linalg.inv(ro_transpose)
print(ro_I.dot(vectorB))


#Практика
for j in range(0, T):
    c = random.random()
    if cur_state == 0:
        if c < ro[0][0]:
             cur_state = 0
        elif ro[0][0] < c < (ro[0][0] + ro[0][1]):
            cur_state = 1
        else:
            cur_state = 2
    elif cur_state == 1:
        if c < ro[1][0]:
            cur_state = 0
        elif ro[1][0] < c < (ro[1][0] + ro[1][1]):
            cur_state = 1
        else:
            cur_state = 2
    else:
        if c < ro[2][0]:
           cur_state = 0
        elif ro[2][0] < c < (ro[2][0] + ro[2][1]):
            cur_state = 1
        else:
            cur_state = 2
    if cur_state == 0:
        count0 = count0 + 1
    elif cur_state == 1:
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print("Практика (0): ", + (count0 / T))
print("Практика (1): ", + (count1 / T))
print("Практика (2): ", + (count2 / T))