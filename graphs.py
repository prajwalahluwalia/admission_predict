import numpy as np
import matplotlib.pyplot as plt


#mergesort
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

plt.subplot(221)
plt.plot(x, y)
plt.yscale('log')
plt.ylabel("Worst Case")
plt.title('Time Complexity of Merge Sort')
plt.grid(True)
plt.subplot(222)
plt.plot(x, y, color = 'red')
plt.ylabel('Average Case')
plt.yscale('log')
plt.grid(True)
plt.subplot(223)
plt.plot(x, y, color = 'orange')
plt.ylabel('Best Case')
plt.yscale('log')
plt.grid(True)


plt.show()

#Bubblesort

x = np.linspace(0, 6, 100)
y_1 = np.power(x, 2)
y_2 = np.power(x, 2)
y_3 = np.power(x, 1)
plt.plot(x, y_1, label = "Average CAse")
plt.plot(x, y_2+0.5, label = "Worst Case")
plt.plot(x, y_3, label = "Best Case")
plt.title('Compexity of Bubble Sort')
plt.xlabel('Time')
plt.show()

#Quicksort
x = np.linspace(0, 6, 100)
y_1 = np.power(x,2)

plt.subplot(211)
plt.plot(x, y_1)
plt.title('Compexity of Quick Sort')
plt.ylabel('Worst Case')
plt.xlabel('Time')

fig, ax = plt.subplots()
dt = 0.01
x = np.arange(dt, 20.0, dt)
ax.semilogx(x, np.exp(-x / 5.0))
plt.ylabel('Average Case')
plt.xlabel('Time')
plt.title('Compexity of Quick Sort')

fig, ax = plt.subplots()
dt = 0.01
x = np.arange(dt, 20.0, dt)
ax.semilogx(x, np.exp(-x / 5.0))
plt.ylabel('Best Case')
plt.xlabel('Time')
plt.title('Compexity of Quick Sort')
plt.show()

#selectionsort

x = np.linspace(0, 6, 100)
y_1 = np.power(x, 2)
y_2 = np.power(x, 2)
y_3 = np.power(x, 2)
plt.plot(x, y_1, label = "Average Case")
plt.plot(x, y_2+0.5, label = "Worst Case")
plt.plot(x, y_3+1, label = "Best Case")
plt.title('Compexity of Selection Sort')
plt.xlabel('Time')
plt.show()