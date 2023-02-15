import matplotlib.pyplot as plt

# create some sample data
x_values = [1, 2, 3, 4, 5]
y_values = [3, 1, 4, 1, 5]

# create the line plot
plt.plot(x_values, y_values)

# find the minimum y value and its index
min_y_value = min(y_values)
min_y_index = y_values.index(min_y_value)

# add the minimum y value as text on the plot
plt.text(x_values[min_y_index], min_y_value, str(min_y_value))

# display the plot
plt.show()
