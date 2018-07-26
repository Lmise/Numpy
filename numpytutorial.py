import numpy as np

a = np.array([1, 2, 3])
print(a) #return an array of rank1
print(type(a))#display class  of a -numpy.ndarray 
print(a.shape)
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.shape)  # returns (2,3)
#slicing
print(b[0, 0], b[0, 1], b[1, 0])  # 1,2,,4
e = np.random.random((2, 2))
print(e)


#Array Math
x = np.array([[1,2], [3,4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
print(x)
print(y)

#addition
print(x + y)
print(np.add(x, y))

#subtraction
print(x - y)
print(np.subtract(x, y))

#multiplication
print(x * y)
print(np.multiply(x, y))

#Division
print(x / y)
print(np.divide(x, y))

print(np.sqrt(x))

s = np.arange(6)  # works the same as range() in list
m =np.arange(0,10).reshape(5,2)
print(m)
