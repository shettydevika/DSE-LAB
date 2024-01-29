from functools import partial
def square(x):
    return x*x
def derivative(x):
    return 2*x
def difference_quotient(f,x,h):
    return(f(x+h)-f(x))/h
derivative_estimate=partial(difference_quotient,square,h=0.00001)
x_values=list(range(-10,10))
actual_derivatives=list(map(derivative,x_values))
estimated_derivatives=list(map(derivative_estimate,x_values))
import matplotlib.pyplot as plt
plt.title("Actual derivatives vs estimates")
plt.plot(x_values,actual_derivatives,'rx',label='Actual')
plt.plot(x_values,estimated_derivatives,'b+',label='Estimate')
plt.legend(loc=9)
plt.show()