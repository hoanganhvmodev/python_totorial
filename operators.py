#Python Operators
a = 1 + 2   #Addition
b = 2 -1    #Subtraction
c = 1*2     #Multiplication
d = 1/2     #Division
e = 2%1     #Modulus
f = 1**2    #Exponentiation
g = 4//2    #Floor division

#Python Comparison Operators
x = 1
y = 2
x == y  #Equal
x != y  #Not equal
x > y   #Greater than
x < y   #Less than
x >= y  #Greater than or equal to
x <= y  #Less than or equal to

#Python Logical Operators
a = 1
b = 2
c = 3
a < b and a < c     #Operator: and
a < b or a > c      #Operator: or
not(a < b and a <c) #Operator: not, Reverse the result, returns False if the result is true

#Python Identity Operators
#is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   # returns True because z is the same object as x

print(x is y)   # returns False because x is not the same object as y, even if they have the same content

print(x == y)   # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)   # returns False because z is the same object as x

print(x is not y)   # returns True because x is not the same object as y, even if they have the same content

print(x != y)   # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#Python Membership Operators
#in
x = ["apple", "banana"]

print("banana" in x)    # returns True because a sequence with the value "banana" is in the list

#not in
x = ["apple", "banana"]

print("pineapple" not in x) # returns True because a sequence with the value "pineapple" is not in the list

#Python Bitwise Operators
#Operator	Name
#   & 	    AND
#   |	    OR
#   ^	    XOR
#   ~       NOT

