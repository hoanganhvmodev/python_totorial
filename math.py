#Built-in Math Functions
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)    #output: 5
print(y)    #output: 25

#The abs() function returns the absolute (positive) value of the specified number
x = abs(-7.25)

print(x)    #output 7.25

#The pow(x, y) function returns the value of x to the power of y (xy).
x = pow(4, 3)

print(x)    #output: 64

#The Math Module
import math
x = math.sqrt(64)

print(x)    #output 8.0

#The math.ceil() method rounds a number upwards to its nearest integer,
# and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#The math.pi constant, returns the value of PI (3.14...):
import math
x = math.pi

print(x)    #output: 3.141592653589793