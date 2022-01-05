# Description
# Create a function which computes the Euclidean norm of each line for a
# 2D array. Use numpy operations and vectorization, avoid for cycles.

import numpy

def power_function(item):
    return item * item

def sqrt_function(item):
    return numpy.sqrt(item)

def main():
    list = numpy.arange(5)[:, None]*numpy.ones((5,3))

    vectorized_function = numpy.vectorize(power_function)
    data = vectorized_function(list).sum(axis=1)
    vectorized_function = numpy.vectorize(sqrt_function)
    print(vectorized_function(data))

if __name__ == '__main__':
    main()
