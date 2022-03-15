#Creating a Function + Calling a Function
def my_function():  #In Python a function is defined using the def keyword:
  print("Hello from a function")

my_function()

#Arguments
def my_function(param):
  print(param + 1)

my_function(2)
my_function(3)
my_function(4)

#Number of Arguments
def my_function(pram1, param2):
  print(pram1 + " " + param2)

my_function("hoang", "anh")

#Arbitrary Arguments, *args
def my_function(*param):
  print("it is " + param[2])

my_function("name", "age", "adress")

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))