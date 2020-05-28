# Machine Learning - Data Distribution by Chisoftmeida
import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0, 5.0, 250)

print(x)

# Histogram
x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

# Big Data Distributions
x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()