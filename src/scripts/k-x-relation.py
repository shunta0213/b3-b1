import numpy as np
import matplotlib.pyplot as plt
import scienceplots


plt.style.use(['science','ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'  # Times New Romanに近いスタイルで数式を表示

# 定数
a = 1.50e-06  # メーター
eta = 8.90e-04  # パスカル・秒
T = 299.35  # ケルビン
t = 5.0  # 秒

x = np.linspace(1.0e-12, 4.0e-12, 400)

k = x * 3 * np.pi * a * eta / (T * t)

plt.figure()
plt.plot(x*1e12, k)
plt.xlabel(u"$\\left<(\\Delta x)^2\\right>$ / $10^{-12}$ m$^2$")
plt.ylabel("$k$ / JK$^{-1}$")

plt.savefig("../figures/k-x-relation/k-x-relation.png")
