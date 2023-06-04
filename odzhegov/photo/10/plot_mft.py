import matplotlib.pyplot as plt
import numpy as np


data_x_1 = np.array([7, 10, 30, 70, 130, 160, 190])
data_min_1 = np.array([1.98, 3.3, 5.7, 11.5, 15.8, 26.9, 34.0])
data_max_1 = np.array([192, 189, 183.9, 151.3, 91.2, 64.4, 44.0])

I_1 = (data_max_1 - data_min_1)/(data_max_1 + data_min_1)

plt.scatter(data_x_1, I_1, label="Первая серия")

data_x_2 = np.array([10, 40, 70, 100, 130, 160, 190])
data_min_2 = np.array([3.7, 5.4, 7.9, 5.8, 5.7, 17.0, 19.1])
data_max_2 = np.array([87.8, 110.6, 71.7, 50.9, 52.9, 24.9, 19.1])

I_2 = (data_max_2 - data_min_2)/(data_max_2 + data_min_2)

plt.scatter(data_x_1, I_2, label="Вторая серия")

plt.legend()

plt.xlabel("Частота линий, lp/mm")
plt.ylabel("Контраст")

plt.show()

