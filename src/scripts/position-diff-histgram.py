import pandas as pd
import matplotlib.pyplot as plt

path = "../data/position-diff.csv"

data = pd.read_csv(path)
clean_data = data.dropna()

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'  # Times New Romanに近いスタイルで数式を表示
plt.rcParams['font.size'] = 24

# $\Delta x_m$のヒストグラムを再度作成して保存
plt.figure(figsize=(8, 6))
plt.hist(clean_data['x_m_diff'], bins='auto', color='blue', alpha=0.7)
plt.title("Histogram of $\\Delta x_m$")
plt.xlabel('$\\Delta x_m$ / \u03bcm')
plt.ylabel('Frequency')
plt.savefig('../figures/delta-x-y-histogram/delta-x-histogram.png', format='png', dpi=300)

# $\Delta y_m$のヒストグラムを再度作成して保存
plt.figure(figsize=(8, 6))
plt.hist(clean_data['y_m_diff'], bins='auto', color='green', alpha=0.7)
plt.title('Histogram of $\\Delta y_m$')
plt.xlabel('$\\Delta y_m$ / \u03bcm')
plt.ylabel('Frequency')
plt.savefig('../figures/delta-x-y-histogram/delta-y-histogram.png', format='png', dpi=300)
