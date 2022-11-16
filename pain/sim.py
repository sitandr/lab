import math
import matplotlib.pyplot as plt
import numpy as np

p_a = 10.1e5
V0 = 1.14e-3 # 1 л
S = math.pi * 5.95e-3**2
m = 4.8e-3

g = 9.8
R = 8.31
T_0 = 300

Φ = 0.01 # моль/с #?
α = 0.02 #?
β_c = 0 #?
β_v = 0 #?
dt = 0.00001

γ = 7/5

k = V0**(γ-1)*R*T_0

ν = p_a*V0/R/T_0
V = V0
x = 0
v = 0

xs = []
for i in range(4_00_000):
    V = V0 + S*x
    if V < 0:
        break
    p = k*ν/V**γ
    x += v*dt + (-g + (p-p_a)*S/m)*dt**2/2
    v += (-g + (p-p_a)*S/m)*dt
    v -= β_c * dt * np.sign(v) + β_v * v * dt


    ν += Φ*dt
    if x >= 0: 
        ν -= α*(p - p_a)*dt

    xs.append(x)



def count_cross(arr, c):
    arr_n = arr - c
    return ((arr_n[:-1] * arr_n[1:]) < 0).sum()

print('ν:', count_cross(np.array(xs), 0)/(len(xs)*dt)/2)
print('A:', (max(xs) - min(xs))/2*100) 

plt.plot(np.arange(len(xs))*dt, np.array(xs)*100)
plt.xlabel("Время, с")
plt.ylabel("Координата, см")
plt.show()
