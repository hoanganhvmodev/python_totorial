#Trong Python, hàm vô danh là hàm được định nghĩa mà không có tên. 
#Nếu các hàm bình thường được định nghĩa bằng cách sử dụng từ khóa def,
#thì hàm vô danh được định nghĩa bằng cách sử dụng từ khóa lambda

#systax =>  lambda tham_so: bieu_thuc

x = lambda a : a + 10
print(x(5))     #output 15

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))   #output 13

#
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)

print(mydoubler(11))    #output 22

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))    #output 22
print(mytripler(11))    #output 33