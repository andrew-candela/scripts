from matplotlib import pyplot as plt
#line plot

y=[math.cos((math.pi * x)/500) for x in range(1000)]
x=[x for x in range(1000)]
plt.plot(x,y,color='green', marker='o', linestyle='solid')
plt.title("cosine(x)")
plt.ylabel("y=cos(x)")
plt.show()



variance = [1, 2, 4, 8, 16, 32, 64, 128, 256] 
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)] 
xs = [i for i, _ in enumerate(variance)]

# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance, 'g-', label='variance') # green solid line 
plt.plot(xs, bias_squared, 'r-.', label='bias^2') # red dot-dashed line 
plt.plot(xs, total_error, 'b:', label='total error') # blue dotted line


# because we've assigned labels to each series # we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()
