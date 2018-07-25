import numpy as np

a = np.array([1, 2, 3])
print(a) #return an array of rank1
print(type(a))#display class  of a -numpy.ndarray 
print(a.shape)
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.shape)  # returns (2,3)
print(b[0, 0], b[0, 1], b[1, 0]) # 1,2,,4