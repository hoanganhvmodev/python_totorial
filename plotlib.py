from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('Agg')

x = [2, 5, 8, 12, 45]
y = [7, 9, 23, 33, 46]
y1 = [12, 33, 34, 45, 95]

plt.plot(x, y, color='k', marker='.')
plt.plot(x, y1, color='b', label='python')

plt.xlabel('Attack')
plt.ylabel('HP')
plt.title('Pokemon')
plt.legend(['pikaChu', 'Chaos'])
plt.grid()

plt.show()

###  Matplotlib Bars ###

name = ['HoangAnh', 'Thuy', 'Hieu', 'Giang', 'Huy', 'Mai']
age = [21, 24, 34, 45, 79, 19]

plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age chart')
plt.legend(['Name', 'Age'])

plt.bar(name, age, color='hotpink')
plt.show()

### Matplotlib Pie Charts ###
y = [45, 15, 35, 5]
mylabels = ['Apples','Sam Sung', 'Nokia', 'Vertu']

plt.pie(y, labels=mylabels)
plt.legend()
plt.savefig("img.png")
