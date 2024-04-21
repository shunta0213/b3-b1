import numpy as np
from math import pi
from scipy.constants import Boltzmann
import matplotlib.pyplot as plt
import scienceplots


plt.style.use(['science','ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'  # Times New Romanに近いスタイルで数式を表示

rng = np.random.default_rng()

def init_x():
  return rng.random(2)

def init_v():
  return rng.normal(0, 1, 2)

def random_f(alpha, k, T, dt):
  var = 2 * alpha * k * T / dt
  return rng.normal(0, var, 2)

def v_one(alpha, dt, m, v_n, f_n):
  return (1 - alpha * dt / m) * v_n + dt * f_n / m


t = 1.0 #sec
dt = 1E-6 #sec

a = 1e-8 #m /radius
m = 1e-14 #kg
eta = 1e-3 #Ns/m^2 = kg m/s^2 s^3/m^3 / 粘性率
T = 300 #K
alpha = 6 * pi * a * eta
k = Boltzmann
print(k)

print(f"alpha: {alpha}")
print(f"gamma: {alpha/m}")
print(f"1/gamma: {m/alpha}")

x = [np.zeros(2)]
v = [np.zeros(2)]
for i in range(int(t/dt)):
    fi = random_f(alpha, k, T, dt)
    v_i = v_one(alpha, dt, m, v[i], fi)
    v.append(v_i)
    x.append(x[i] + v[i] * dt)

x = np.array(x) * 1E+11

x_x, x_y = zip(*x)

plt.plot(x_x, x_y)
plt.xlabel('$x$ /m')
plt.ylabel('$y$ /m')

plt.savefig("../figures/brownian-2d-sim/brownian-2d-sim.png")
