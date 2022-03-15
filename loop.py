#The while Loop
i = 1
while i < 6:
  print(i)
  i += 1

#The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#The continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#The else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String
for x in "hoanganh":
  print(x)

#The break Statement(For)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "hoanganh":
    break

#Break(For)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "hoanganh":
    break
  print(x)

#continue(For)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "hoanganh":
    continue
  print(x)

#The range() Function
for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Seven")
##################
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Seven")    #If the loop breaks, the else block is not executed.

#Nested Loops
arr1 = ["a", "b", "c"]
arr2 = ["d", "e", "f"]

for x in arr1:
  for y in arr2:
    print(x, y)