import matplotlib.pyplot as plt
import numpy as np

from methods.functions import get_c_x, get_gamma

# Параметры мячика и установки
r = 0.02  # радиус мячика в метрах
alpha = 0  # угол наклона установки

a = 30

t = np.linspace(0, 15, 10000)
y = get_gamma() * (((np.exp(t * (981 / (140 * r)) * (2 * a) ** 2 - get_cx()) - 1) / (
(np.exp(t * (981 / (140 * r)) * (2 * a) ** 2 - get_cx()) + 1))) ** 2 - 1)

fig, ax = plt.subplots(figsize=(15, 10))
plt.title('График функции $\cos(\\theta)$ от времени.')
plt.xlabel('t, c', fontsize=13)
plt.ylabel('$\cos(\\theta)$, c', fontsize=13)

ax.plot(t, y, color='black')

# ax.errorbar(x, y1, yerr=0.01, xerr=0.1, fmt='.k', capsize=2)

# ax.plot(x, y2, marker='o', color='dimgray')
# ax.errorbar(x, y2, yerr=0.01, xerr=0.1, fmt='.k', capsize=2)


plt.yticks(np.arange(-1, 1, 0.1))
plt.xticks(np.arange(0, 10, 1))
ax.grid()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

fig.savefig('/home/yaroslav/PROJECTS_ITMO/cylinder/plots/plot_1/cos_theta_ot_t.png')

plt.show()
