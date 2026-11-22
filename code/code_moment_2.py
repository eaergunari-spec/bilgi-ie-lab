import numpy as np
import matplotlib.pyplot as plt

forecast = np.array([32, 28, 24, 16])
rate = np.array([4, 3, 5, 2])
allocation = np.array([6, 5, 5, 4])

# 1,000 possible evenings around the forecast
future_demand = np.random.poisson(forecast, size=(1000, 4))
capacity = allocation * rate
served = np.minimum(future_demand, capacity)
total_served = served.sum(axis=1)

print('Average orders served:', round(total_served.mean(), 1))
print('10th percentile:', round(np.percentile(total_served, 10), 1))
print('Worst simulated evening:', int(total_served.min()))

plt.hist(total_served, bins=15, edgecolor='white')
plt.xlabel('Orders served in one evening')
plt.ylabel('Number of simulated evenings')
plt.title('Same plan, 1,000 possible futures')
plt.show()
