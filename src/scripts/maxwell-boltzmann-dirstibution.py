import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science','ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'  # Times New Romanに近いスタイルで数式を表示

T = 299.15       # K
m = 18E-3 # kg/mol

v = np.linspace(0, 4000, 1000)

k1 = 3.10E-23
n1 = 2.68E+23

k2 = 2.03E-23
n2 = 4.09E+23

def maxwell_boltzmann(v, k, n):
    return np.sqrt(2/np.pi) * (m/n / k / T)**(3/2) * v**2 * np.exp(-m/n * v**2 / 2 / k / T)

# 2つの分布を計算
f_v1 = maxwell_boltzmann(v, k1, n1)
f_v2 = maxwell_boltzmann(v, k2, n2)

# グラフを描画
plt.figure()
plt.plot(v, f_v1, label=f'$k_x$')
plt.plot(v, f_v2, label=f'$k_y$', linestyle='--')
plt.xlabel('Velocity $v$ m/s')
plt.ylabel('Probability density $f(v)$')
plt.legend()
plt.show()

plt.savefig("../figures/maxwell-boltzmann-distribution/maxwell-boltzmann-distribution.png")
