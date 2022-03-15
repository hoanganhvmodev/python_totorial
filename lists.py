#Create a List
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list = ["abc", 34, True, 40, "male"]

print(list1)
print(list2)
print(list3)
print(list)

#type()
mylist = ["apple", "banana", "cherry"]

print(type(mylist))

#The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)     #output ['apple', 'banana', 'cherry']

#Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  #output banana

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])     #output cherry

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])    #output ['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])     #output ['apple', 'banana', 'cherry', 'orange']

#Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  #output ['orange', 'kiwi', 'melon']

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("true")     #output true

#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)     #output ['apple', 'blackcurrant', 'cherry']

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)     #output ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)     #output ['apple', 'banana', 'watermelon', 'cherry']

#Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")

print(thislist)     #output ['apple', 'banana', 'cherry', 'orange']

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)     #output ['apple', 'orange', 'banana', 'cherry']

#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

print(thislist)     #output ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)     #output     ['apple', 'banana', 'cherry', 'kiwi', 'orange']

#Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)     #output ['apple', 'cherry']

#Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)     #output ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()      #Remove the last item
print(thislist)     #['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]     #Remove the first item
print(thislist)     #output ['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist    #Delete the entire list:

#Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()        #Clear the list content
print(thislist)         #output []

#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)  #output: apple bannane cherry

#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])    #output: apple banana cherry
  i = i + 1 

#Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]    #output: apple banana cherry

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)  #output ['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)   #output ['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)  #output ['banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in range(10)]
print(newlist)      #output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x for x in range(10) if x < 5]
print(newlist)      #output [0, 1, 2, 3, 4]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)      #output ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

#Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)     #output ['banana', 'kiwi', 'mango', 'orange', 'pineapple']  => a b c d ...

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)     #output [23, 50, 65, 82, 100]

#Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)   #descending
print(thislist)     #output ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)     #output [100, 82, 65, 50, 23]

#Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()     #By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
print(thislist)     #output ['Kiwi', 'Orange', 'banana', 'cherry']

#Perform a case-insensitive sort of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)     #output ['banana', 'cherry', 'Kiwi', 'Orange']

#Reverse Order
thislist = ["b", "c", "K"]
thislist.reverse()
print(thislist)     #output ["k", "c", "b"]

#Copy a List
thislist = ["apple", "banana", "cherry"]
newlist = thislist.copy()
print(newlist)  #output ['apple', 'banana', 'cherry']

#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)    #output ['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)    #output ['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)     #output ['a', 'b', 'c', 1, 2, 3]

