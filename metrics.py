# Fuente: https://pythonprogramming.net/legends-titles-labels-matplotlib-tutorial/
import matplotlib.pyplot as plt
import numpy as np
import time

y = []
for _ in range(50):
    #sent, received = time.time(), 0
    #time.sleep(np.random.randint(0, 900) / 1000)
    #received = time.time()
    #delta = received - sent
    delta = np.random.randint(0,5000) / 1000
    y.append(delta)

# Calculate percentiles
percentiles = np.percentile(y, [50,65,80,95,100])


# plot
plt.plot([50,65,80,95,100], percentiles, label='Experimento 1' , marker='x', color='b')
plt.ylim(0, 7)

# Add percentiles to the plot


plt.xlabel('Percentil')
plt.ylabel('Latencia en m/s')
plt.title('Metrica de Datos')
plt.legend()
plt.show()

plt.show()