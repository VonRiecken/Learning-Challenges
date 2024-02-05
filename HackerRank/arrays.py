import numpy


def arrays(arr):
    # complete this function
    # use numpy.array

    new = numpy.flip(numpy.array(arr, dtype=float), axis=0)

    return new
