import numpy
numpy.set_printoptions(legacy='1.13')
A = list(map(float, input().split()))
AA = numpy.array(A)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
