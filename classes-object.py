#Create a Class
class MyClass:
  x = 5

print(MyClass)  #output; <class '__main__.MyClass'>

#Create Object
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)     #output: 5

#The __init__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)

print(p1.name)  #output: john
print(p1.age)   #output: 36

#Object Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()     #output: Hello my name is John

#Delete Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age  #delete age

#Delete Objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1    #delete ojb person

#The pass Statement
class Person:
  pass  #class definitions cannot be empty, but if you for some reason have a class definition with no content,
        #put in the pass statement to avoid getting an error.

