import matplotlib.pyplot as plt
import random

x_in, x_out, y_in, y_out = [], [], [], []
in_count, out_count = 0, 0

# Generating random points through random generation of x and y values
for i in range(10000000):
    x = random.random()
    y = random.random()

    # use of pythagoras formula to check if point is within the semi circle
    if ((x ** 2 + y ** 2) ** 0.5) <= 1:
        x_in.append(x)
        y_in.append(y)
        in_count += 1
    else:
        x_out.append(x)
        y_out.append(y)
        out_count += 1

# usage of ratio of area of quarant in a square to estimate the value of pi 
pi = in_count / (in_count + out_count) * 4
print('In ={}, Out ={}, Pi ={}'.format(in_count, out_count, pi))

# plot all generated value and the quardrant for visualization
plt.scatter(x_in, y_in, c='#1f77b4', s=1)
plt.scatter(x_out, y_out, c='#ff7f0e', s=1)

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('In ={}, Out={}, Pi ={}'.format(in_count, out_count, pi))

plt.show()
