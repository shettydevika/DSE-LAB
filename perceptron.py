#Implementation of Perceptron Algorithm for AND,OR,NOT & XOR Logic Gate 
import numpy as np 
  
# define Unit Step Function 
def unitStep(v): 
    if v >= 0: 
        return 1
    else: 
        return 0
    
# design Perceptron Model  
def perceptronModel(x, w, b): 
    v = np.dot(w, x) + b 
    y = unitStep(v) 
    return y 

#AND Logic Function
def AND_logicFunction(x):
    w = np.array([1, 1])
    b = -1.5
    return perceptronModel(x, w, b)

# OR Logic Function 
def OR_logicFunction(x): 
    w = np.array([1, 1]) 
    b = -0.5
    return perceptronModel(x, w, b) 

# NOT Logic Function
def NOT_logicFunction(x):
	return perceptronModel(x, w=-1, b=0.5)
print("Output of NOT Logical Function")
print("NOT(0) = {}".format(NOT_logicFunction(0)))
print("NOT(1) = {}".format(NOT_logicFunction(1)))


# XOR Logic Function
def XOR_logicFunction(x):
    gate_1 = AND_logicFunction(x)
    gate_2 = NOT_logicFunction(gate_1)
    gate_3 = OR_logicFunction(x)
    new_x = np.array([gate_2, gate_3])
    output = AND_logicFunction(new_x)
    return output

# testing the Perceptron Model 
test1 = np.array([0, 0]) 
test2 = np.array([0, 1]) 
test3 = np.array([1, 0]) 
test4 = np.array([1, 1]) 

print("\nOutput of AND Logical Function")
print("AND({}, {}) = {}".format(0, 0, AND_logicFunction(test1)))
print("AND({}, {}) = {}".format(0, 1, AND_logicFunction(test2)))
print("AND({}, {}) = {}".format(1, 0, AND_logicFunction(test3)))
print("AND({}, {}) = {}".format(1, 1, AND_logicFunction(test4)))

print("\nOutput of OR Logical Function")
print("OR({}, {}) = {}".format(0, 0, OR_logicFunction(test1))) 
print("OR({}, {}) = {}".format(0, 1, OR_logicFunction(test2))) 
print("OR({}, {}) = {}".format(1, 0, OR_logicFunction(test3))) 
print("OR({}, {}) = {}".format(1, 1, OR_logicFunction(test4))) 

print("\nOutput of XOR Logical Function")
print("XOR({}, {}) = {}".format(0, 0, XOR_logicFunction(test1)))
print("XOR({}, {}) = {}".format(0, 1, XOR_logicFunction(test2)))
print("XOR({}, {}) = {}".format(1, 0, XOR_logicFunction(test3)))
print("XOR({}, {}) = {}".format(1, 1, XOR_logicFunction(test4)))

'''
OUTPUT:
Output of NOT Logical Function
NOT(0) = 1
NOT(1) = 0

Output of AND Logical Function
AND(0, 0) = 0
AND(0, 1) = 0
AND(1, 0) = 0
AND(1, 1) = 1

Output of OR Logical Function
OR(0, 0) = 0
OR(0, 1) = 1
OR(1, 0) = 1
OR(1, 1) = 1

Output of XOR Logical Function
XOR(0, 0) = 0
XOR(0, 1) = 1
XOR(1, 0) = 1
XOR(1, 1) = 0'''
