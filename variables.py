#Creating Variables
x = 10
msg = 'Hoang Anh'
print(x,msg)

#type
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Get type variables
x = 5
y = "John"
print(type(x))
print(type(y))

#distinguish between uppercase and lowercase letters
a = 4
A = "Sally" #A will not overwrite a
print(a,A)

#Camel Case
myVariableName = "HoangAnh"
#Pascal Case
MyVariableName = "HoangAnh"
#Snake Case
my_variable_name = "HoangAnh"

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)

#Global Variables-local variable
x = "Hoang Anh" #Global Variable

def myfunc():
  print("hello " + x)

myfunc()
###################
x = "HoangAnh" #Global Variable

def myfunc():
  x = "Word"    #local variable
  print("hello " + x)

myfunc()

print("hi " + x)

#If you use the "global" keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "HoangAnh"

myfunc()

print("hi " + x)

#python Data types
x = "Hello World"	                #str(string)
x = 20	                            #int
x = 20.5	                        #float
x = 1j                              #complex
x = ["apple", "banana", "cherry"]	#list
x = ("apple", "banana", "cherry")	#tuple
x = range(6)	                    #range
x = {"name" : "John", "age" : 36}	#dict
x = {"apple", "banana", "cherry"}	#set
x = True	                        #bool

#Looping Through a String
name = 'hoanganh'
for x in name:
    print(x)

#String Length
a = "Hello World!"
print('length',len(a))

#Check String
txt = "hi, i'm hoang anh"
print("hoang" in txt) #output true

#use if
txt = "The best things in life are free!"
if "life" in txt:
     print("true")
else:
    print("fasle")

#Slicing Strings
a = "Hoang Anh"
print(a[6:9])
print(a[:5])    #Slice From the Start
print(a[6:])    #Slice To the End
print(a[-9:-3]) #Negative Indexing

#Upper Case
a = "hello!"
print(a.upper())

#Lower Case
a = "HELLO!"
print(a.lower())

#Remove Whitespace
a = "     Hello, World!   "  #The strip() method removes any whitespace from the beginning or the end:
print(a.strip()) # returns "Hello, World!"

#Replace String
a = "Hello, World!"
print(a.replace("W", "P")) #return "Hello, Porld!

#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
a = "Hello"
b = "World"
c = a +" "+ b
print(c) #return 'Hello World'

#String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

