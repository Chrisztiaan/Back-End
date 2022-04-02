import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 43, 1000)  # Create a list of evenly-spaced numbers over the range
y = np.linspace(1, 42, 1000)
z = np.linspace(1, 41, 1000)
plt.plot(x, np.cos(x))  # Plot the sine of each x point
plt.plot(x, np.sin(x))
plt.plot(x, np.sin(y))
plt.plot(x, np.cos(y))
plt.plot(z, np.sin(z))
plt.plot(z, np.cos(z))
plt.show()  # Display the plot
