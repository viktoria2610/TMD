# Смоделировать работу Марковской цепи с двумя состояниями за t шагов. Оценить
# вероятность того, что она окажется в i-ом состоянии на шаге t. Также произвести
# теоретический расчет данной вероятности.

import random
import matplotlib.pyplot as plt
import numpy as np


def theoretic(ro, state):
    p0 = np.array([1, 0])
    list_pr_practical = []
    if state == 0:
        list_pr_practical.append(1)
    else:
        list_pr_practical.append(0)

    for k in range(0, t):
        p0 = p0.dot(ro)
        list_pr_practical.append(p0[state])
    return list_pr_practical


def function(ro, n, t, state0):
    count0 = 0
    count1 = 0
    for i in range(0, n):
        cur_state = 0  # состояние 0
        for j in range(0, t):
            c = random.random()
            if cur_state == 0:
                if c < ro[0][0]:
                    cur_state = 0
                else:
                    cur_state = 1
            else:
                if c < ro[1][0]:
                    cur_state = 0
                else:
                    cur_state = 1
        if cur_state == state0:
            count0 = count0 + 1
        else:
            count1 = count1 + 1
    return count0/n, count1/n


n = int(input("Введите n: "))  # кол-во повторений
ro = [[0.8, 0.2],
      [0.6, 0.4]]
listT = []
listPr = []

for t in range(0, 10):
    listT.append(t)
    listPr.append(function(ro, n, t, 0))

list_pr_theoretic0 = theoretic(ro, 0)
list_pr_theoretic1 = theoretic(ro, 1)

plt.plot(listT, listPr, color='red', label='Практическая')
plt.plot(listT, list_pr_theoretic0, color='green', label='Теоретическая(0)')
plt.plot(listT, list_pr_theoretic1, color='blue', label='Теоретическая(1)')

plt.legend()
plt.xlabel('T')
plt.ylabel('Pr')
plt.savefig('res1.png')
plt.show()
