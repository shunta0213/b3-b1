import matplotlib.pyplot as plt
import scienceplots
import pandas as pd

plt.style.use(['science','ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'  # Times New Romanに近いスタイルで数式を表示
# plt.rcParams['font.size'] = 24

# Load the CSV file to check its contents
file_path = '../data/k-n-relation.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head()

# Create a plot with three axes
fig, ax1 = plt.subplots()

# Setting font to Times New Roman

# Plot n (viscosity) on the first y-axis
color = 'tab:red'
ax1.set_xlabel('Temperature / $T$ °C')
ax1.set_ylabel('Viscosity / $\\eta$ $10^{-3}$ Pa s', color=color)
ax1.plot(data['T'], data['n'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for k using the same x-axis
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel("Boltzmann Constant / $k_{x_m} 10^{-23}$J/K", color=color)
ax2.plot(data['T'], data['k_x']*1e23, color=color)  # Scale k for better readability
ax2.tick_params(axis='y', labelcolor=color)


# Show the plot
plt.show()
plt.savefig("../figures/k-n-relation/k-x-n-relation.png", format="png", dpi=300)

fig, ax1 = plt.subplots()

# Plot n (viscosity) on the first y-axis
color = 'tab:red'
ax1.set_xlabel('Temperature / $T$ °C')
ax1.set_ylabel('Viscosity / $\\eta$ $10^{-3}$ Pa s', color=color)
ax1.plot(data['T'], data['n'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for k using the same x-axis
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel("Boltzmann Constant / $k_{x_m} 10^{-23}$J/K", color=color)
ax2.plot(data['T'], data['k_y']*1e23, color=color)  # Scale k for better readability
ax2.tick_params(axis='y', labelcolor=color)

plt.savefig("../figures/k-n-relation/k-y-n-relation.png", format="png", dpi=300)
