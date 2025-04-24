from load_data import load_data
import numpy as np
from sort import bubble_sort
import matplotlib.pyplot as plt
from datetime import datetime

data = load_data('activity.csv')
power_W = data['PowerOriginal']

N_steps = len(power_W)
zeit = np.arange(N_steps)

sorted_power_W = bubble_sort(power_W)

plt.plot(zeit/60,sorted_power_W)
plt.xlabel('Time (min.)')
plt.ylabel('Power (W)')

plt.savefig('power_curve.png')

plt.show()