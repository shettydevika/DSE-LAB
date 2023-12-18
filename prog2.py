import numpy as np

#create arrays
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])

#basic operations
print("Array a: ",a)
print("Array b: ",b)
print("Sum of arrays a&b : ",np.add(a,b))
print("Difference of arrays a&b : ",np.subtract(a,b))
print("Product of arrays a&b : ",np.multiply(a,b))
print("Division of arrays a&b : ",np.divide(a,b))
print("Square root of array a: ",np.sqrt(a))
print("Exponential of array a: ",np.exp(a))

#aggregation operations
print("Minimum value of array a: ",np.min(a))
print("Maximum value of array b: ",np.max(b))
print("Mean of array a: ",np.mean(a))
print("Sandard Deviation of array b: ",np.std(b))
print("Sum of all the elements in array a: ",np.sum(a))

#reshaping arrays
c=np.array([[1,2],[3,4],[5,6]])
print("Array c:")
print(c)
print("Reshaped array c(2 rows, 3 columns):")
print(np.reshape(c,(2,3)))

#transposing arrays
d=np.array([[1,2,3],[4,5,6]])
print("Array d:")
print(d)
print("Transposed array d:")
print(np.transpose(d))

'''
Array a:  [1 2 3 4 5]
Array b:  [ 6  7  8  9 10]
Sum of arrays a&b :  [ 7  9 11 13 15]
Difference of arrays a&b :  [-5 -5 -5 -5 -5]
Product of arrays a&b :  [ 6 14 24 36 50]
Division of arrays a&b :  [0.16666667 0.28571429 0.375      0.44444444 0.5       ]
Square root of array a:  [1.         1.41421356 1.73205081 2.         2.23606798]
Exponential of array a:  [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]
Minimum value of array a:  1
Maximum value of array b:  10
Mean of array a:  3.0
Sandard Deviation of array b:  1.4142135623730951
Sum of all the elements in array a:  15
Array c:
[[1 2]
 [3 4]
 [5 6]]
Reshaped array c(2 rows, 3 columns):
[[1 2 3]
 [4 5 6]]
Array d:
[[1 2 3]
 [4 5 6]]
Transposed array d:
[[1 4]
 [2 5]
 [3 6]]
 '''
