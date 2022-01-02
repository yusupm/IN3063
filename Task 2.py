import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats

y = []
for i in range(9):
    y.append(random.randint(100000, 200000))
y.append(800000)
y = sorted(y)
x = [i for i in range(10)]
data = {'x': x, 'y': y}
dataset = pd.DataFrame(data=data)
# dataset = dataset.drop([9])
x = dataset['x']
y = dataset['y']
plt.scatter(x,y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color = 'red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dataset')
plt.show()

z = np.abs(stats.zscore(dataset))
print(z)