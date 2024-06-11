import matplotlib.pyplot as plt
import numpy as np

# Sample data with some variation
data = np.random.randint(10, 500, size=(200, 150))  # Creates a 5x5 array with values between 10 and 49

# Create the heat map
plt.imshow(data, cmap='viridis')  # 'viridis' is a colormap representing low to high values

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Heat Map Example')

# Display the heat map
#plt.show()  # Error:  FigureCanvasAgg is non-interactive, and thus cannot be shown

#save as 
plt.savefig('heat_map.png')  

# Close the figure to avoid memory leaks(optional)
plt.close()