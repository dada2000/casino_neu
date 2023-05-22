import matplotlib.pyplot as plt
import numpy as np
import random

# Define the function
def f(x):
    return x**3 - 2

def g(x):
    return np.power((x+2),(1/3)) #(x+2)**(1/3)

# Generate x values from -10 to 10
x = np.linspace(-10, 10, 100)
print(f"np.linspace(-10, 10, 10) --> Type(x):{type(x)}")
print(x)
print("****************")
# Calculate corresponding y values ### np.linspace array can be directly entered in function without iteration
# ### --> returns np.array with func values --> entered into plt.plot()
y = f(x)
#print(f"y = f(x) --> Type(y){type(y)}")

z = g(x)

# Create the plot
#plt.plot(x, y, color = "blue")
plt.plot(x, z, color = "orange")

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = 3/x')

# Display the plot
plt.show()

#Update for 2nd PUSH test