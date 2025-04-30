from mod import mymodule
# __str__=2
# _a=3
# __b=4

# abc = "1","000","000"
# print(type(abc))
# __init__=2
# it=3
# on=3
# abc="5"
# print(int(abc))
# def main():
#     return (3)
# func = main()
# print(func)
# print(round(7463.123,4))

# name = "Kanwal 224uhsdkfkjjnfkd34567$"
# name2="Kanwal 224uhsdkfkjjnfkd34567$"
# # print(id(name))
# # print(id(name2))
# # print(name is not name2)
# # print(type(id(name)))
# mango=[2353:7632,435234353]
# apple = mango

# def example(a):
#     a = a + '2'
#     a = a*2
#     return a
# example("hello")

# print("He said, ‘Yes!'")

# print('”Once upon a time…”, she said.')
# print('3\b3')
# print("’That’s okay")

# print('tom\ndick\nharry')
# print('''tom
# \ndick
# \nharry''')
# x = "welcome"

# #if condition returns False, AssertionError is raised:
# assert x != "welcome", "x should not be 'welcome'"

# print(0.1+0.2)
# print(type(complex(2, 3)))
# print(float('inf'))

# print(~~~~~~~5)
# print(~5)

# print(float('56'+'78'))
# # print(float('12+34'))
# print( float('NaN'))
# print(bin(3))
# print(bin(4))
# print(int("10.0"))
# for i in x:
#     print(i)
#     string = i.upper()
#     print(string)
# print(x)


# x = ['ab', 'cd']
# for i in x:
#     string=i.upper()
#     x.append(string)
# print(x)

# myDict:dict[str, int]={"name":"ali",2:2}
# print(myDict)
# def test():
#         return ("Hello")
# print(type(test()))


# print(100.bit_length()) 
# class Hobby():
#         name="Naimal"
#         def myFunc(self):
#                 print(self.name)
# myObj=Hobby()   #1st __new__ (for alocate memory) 2nd __init__ (for initialize values)
# myObj.myFunc()

# myDict:dict[str | int, int | str]={"age":3,3:"3"}


# ba=bytearray(b"hello")
# print(type(ba))

# ba[0] = 65
# mv=memoryview(ba)
# print(mv)
# print(mv[1:3])
# print(bytes(mv[0:3]))

# bA=bytearray([65,66,98,99])
# print(bA)
# string=" "

# print(string[0],"me to khali hun")

# print(float("3.14"))

# print(type(range(5))) 
# print(range(10)[7]) 
# x = 300  
# y = 300  
# print(x is y)
# print("5" * 5)
# str:list[str,int,bool] = [1, "a",True]
# print(list)
# list="ad"
# print(list)
# isinstance(5, int)

# range(1, 10, 2)[3]
# 1,3,5,7,9
# A=None
# B=None
# print(id(A) , id(B))
# print(None is None)

# print(chr(65))
# data=[2,3,4,5,5,6,7,6,7,8,4]
# def f(x):
#     return x - 5
# a=print("Naimal")
# print(a)
# filtered = [print(y) for i in data if (y := f(i)) > 0]
# # print(y)
# print(filtered)
# if (n := len(data)) >10:
#  print(f"Data has {n} elements (too large!)")
# else:
#     print("else condition")
# b=bytes(b"Hello");
# c=b"Hello"
# print( type(c))
# ba=bytearray([65, 66, 67, 69])
# print(ba)
# ba[0]=101
# print(type(ba))

# mv=memoryview(b"Hello")[0:3]
# print(bytes(mv))

# fs=frozenset((2,3,5))
# print(fs)

# range(1, 10, 2)[3]
# [1,3,5,7,9]

# rng=range(5)
# print(rng)

# print(ord("a"))
# print(not True)
# x=7
# y=-x
# print(y)
# print(3 + "ab")
# x = 10  
# y = 5  
# print(x //= 3) 
# print(bin(5))
# x = 5  
# print(f"{x:b}")

# print(type(3.14))
# print(3 * "ab")
# print("ab" * 3)

# a = 5  
# b = a
# b=4
# print(a)
# print(b)

# x = 10  
# y = 5  
# x //= 3
# print(x) 

# -5, 256
# a = 1000; b = 1000; print(id(a) , id(b)) #True
# a = 5; b = 5; print(a is b)  #True
# a = "hello"; b = "hello"; print(a is b) #True
# a = [2]; b = [2]; print(id(a) , id(b))  #False


# x = 5  
# b=bin(5)
# myVar= f"{x:b}"
# print(myVar)
# print(b)
# print(f"{x:b}") 

# a = [1, 2]  
# b = [1, 2]  
# print(a is b)
# def f(x):  
#         return 2 * 2 
     
# # print([f(x) for x in range(3) if f(x) > 2]) 

# print([f(x) for x in range(3) if f(x) > 2])


# print("Hello, World!")
# x = 5, y = 10
# if 5 in [1,2,3]: print("No")
# x = (1, 2, 3)

# print(__name__)
# x = 10  
# def func(): 
     
#     global y
#     y=6
# func()  
# print(y)

# class Car():
#     __total_num=2
#     def __init__(self,name, age):
#         self.name=name
#         self.age=age
       
#     @staticmethod
#     def get_total():
#         print(Car.__total_num) 
    
# myObj=Car("Naimal", 23)
# print(Car.get_total())


# print("Python".find("th",3))
# try: x = 5/0;
# except ZeroDivisionError:
# try: x = 5/0 
# except: print("Error")

# x = [1, 2]  
# y = x  
# y = y+[3]  
# print(x)
# print("Hello".upper())
# def bahir():
#     x=5
#     def under():
#         nonlocal x
#         x=10
#         print(x)
#     under()
#     print(x)
# bahir()

# x = 10  
# y=f"{x:b}"
# print(type(y))
# print(f"{x:b}") 

# print("\u0072")

# print("Hello,\b World!")
# print("Shurem".center(17,"$"))
# print("Shurem".partition("S"))
# print("".isidentifier())
# print("Hello".center(10, "*"))
# string=b"Python".decode()
# print(type(string))

# print("123".isdigit());print("123".isdigit())

# print("shurem".zfill(7))

# print(complex(2,3))

# print("shurem ".join(["A", "B", "C"]))
# string1="apple banana cherry".split()
# string2="apple,banana,cherry".split(",")
# print(string1)
# print(string2)
# s="This is the cat"
# print(s.split())
# print(s.replace("cat", "dog"))

# var1=3
# var2=4
# var3="f"
# print("num 1 is {} number 2 is {} value 3 is {}".format(var1, var2, var3))

# print("Hello\nWorld".splitlines())
# print("Hello World".splitlines(True))
# print("Hello\nWorld")
# print("shurem"[::-1])
# print(int("12"))
# a = "hello"
# b = "hello"
# print(a is b)
# print("Pi: {:.2f}".format(3.14159))
# print("Shurem".lower().find("re"))
# print("123" == 123)
# print("Hello, {}".format("World"))
# x = 10  
# while x > 0:  
#     print(x)
#     x -= 1  

# for i in range(3):  
#         pass  
# print(i)

# while True  
#     print("Looping")
# x = 0  
# while x < 3:  
#     x += 1  
# print(x) 
# print(any([False, 1, ""]))
# tup = (1, [2, 3]); 
# tup[0] = 3
# print(tup)
# # tup[1]={"name":"Naimal"}
# tup[1][1]={"name":"Naimal"}
# print(type(tup))
# print(tup)

# print((1, 2) + (3))
# print(sorted((3, 1, 2)))
# lst=[2,4,6,6,9,7,8]
# print(lst.__contains__(4))

# print([1, 'a'].sort())

# lst=[2,3,54,5,6]
# del lst[1]
# print(lst)

# print([1, 2] * 2)

# print(sum([(1, 2), (3, 4)], ()))
# lst = ['a', 'b']
# result=list(zip(lst, range(len(lst))))
# print(result)

# a = ([1, 2],);
# print([1, 2] += [3])
# print(a)

# a=[1,2,4]
# b=a.copy()
# b[0]=3
# print(a)
# print(b)
# a=(1,)
# b=(1,)
# print(id(a), id(b))
# print(a is b)
# print((1,) == (1,))

# lst=[(1,3), (4,5)]
# # lst[0], lst[1] = lst[1], lst[0]
# # print(lst)
# print(sum(lst,()))

# print(len([[[1, 2]]]))

# a=[1,2,5,3,6]
# b=[6,3,2,5,1]
# print(sorted(a)==sorted(b))
# print(set(a)==set(b))

# x, y = (1)
# print(x,y)
# d = {"a": 1}; print(d["b"])
# d = {"a": 1, "b": 2}
# d.update({"c": 3})
# print(d)
# d = {"1": "pehla", "1": "dusra"}; print(d["1"])

# keys = ["a", "b"]
# print({k.upper(): i+1 for i, k in enumerate(keys)})
# print({k: v for k in keys for v in [1, 2]})
# print(dict(zip(keys, [1, 2])))


# d = {"a": 1, "b": 2}
# print(d.pop("b", None))
# print(d)

# d = {"a": 1}
# d={}
# # del d
# print(d)
# print(d.get("a", 0))

# d = {1: "a"}
# # print(d)

# d = dict.fromkeys("123", 0)
# print(d)

# print(len({"1":[2,3,4], 3:(2,4,5)}))

# d = {i: i**2 for i in range(3)}
# # {0:0,1:1,2:4}
# print(d[2])

# print({k: v for k, v in [("a", 1), ("b", 2)]})

# dct = dict(a=1, b=2)
# dct.pop("a")
# print(dct)

# words = ["a", "b", "a", "A"]
# freq = {w:words.count(w) for w in words}
# print(freq)

# keys = ["a", "b"]
# d = dict(enumerate(keys))
# print(d)
# obj={"apple":4,"banana":3,"orange":6}
# print(dict(sorted(obj.items(), key=lambda x: x[1])))
# d = {}
# d[1] = "a"
# d[1.0] = "b"
# print(d)

# d = {0: "a"}; print(d[False])

# print(dict([(1, 2), (3, 4)]))
# dct={**{"a": 1}}
# print(dct)

# lst=["a=1", "b=2"]
# # print(dict(pair.split("=") for pair in lst))
# dct={}
# for pair in lst:
#     for k,v in (pair.split("=")):
#         print(k,v)

# print({k: v for k, v in (s.split("=") for s in lst)})
# print(eval(f"dict({','.join(lst)})"))

# d = {k: v for k, v in []}
# print(d)

# a: str = "Hello!    World"
# b: str = ("3")

# print("id(a) = ", id(a))
# print("id(b) = ", id(b))
# print(a.__hash__())
# print(hash(b))

# my_set: set   = {1,2,3,4,5, "Hello! World"}
# my_dict: dict = {my_set: "Hello! World"} # dictionary only accept immutable objects as a key
# print(my_dict)
# print(my_dict.keys())

# print(len([1,2,3]))
# tple=("apple", "banana", "cherry")
# print(tple[0])
# ST =set([1, 2, 3, 2])
# print(ST)
# print({1, 2} ^ {2, 3})
# print({1, 2}.issuperset({1}))

# print(set(1, 2, 3))
# s = {1, 2}
# s.update([4, 5])
# print(s)
# s = {1, 2, 3}
# s.difference_update({2}, {3})
# print(s)

# a = {1, 2}
# b = a
# a.add(3)
# print(b)

# s = set()
# s.add(s)
# print(s)
# numbers = [1, 2, 3, 4]
# # even=set(filter(lambda x: x%2==0, numbers))
# even={x for x in numbers if x % 2 == 0}
# print(even)

# numbers = [1, 2, 3, 4]
# evens=set(filter(lambda x: x%2==0, numbers))
# print(evens)  # Output: {2, 4}
# s = {1, 2, 3}
# s.update([4, (5,)])
# print(s)
# print(set('hello'))
# s = {1, 2}
# s |= {3}
# print(s)
# print(frozenset({1, 2}) == set({1, 2}))

# print(type(lambda x: x)

# from math import sqrt as s
# import math as m
# print(m.sqrt(9))
# def greet():
#     return "Hello"
# print(greet())
# x = 10
# def func():
#     x = 5
# func()
# print(x)
# def func(a, b=[]):
#     b.append(a)
#     return b
# print(func(1), func(2))
# print(globals() is locals())
# def func():
#     try:
#         return 1
#     finally:
#         return 2
# print(func())
# import sys
# print(type(sys.version))

# import math
# help(math.sqrt)
# a = [1, 2]
# def func(x=a):
#     return x
# a.append(3)
# print(func())
# def func():
#     yield from [1, 2, 3, 4]
# g = func()
# print(list(g))

# def func2():
    
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# g2=func2()
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))

# def func():
#     return lambda x: x + 1
# f = func()
# print(f(2))

# def outer():
#     x = 5
#     def inner():
#         nonlocal x
#         x += 1
#         return x
#     return inner
# f = outer()
# print(f(), f())

# def test_func(*args):
#     return sum(args)
# print(test_func(1, 2, 3, 4))

# def my_function(a, b=3):
#     return a + b
# print(my_function(1, 2))
# def function():
#     print("Hello")
#     return 5
# x = function()
# print(x)

# import math.sqrt
# def func(a, b):
#     return a * b
# print(func(2, "3"))


# def outer():
#         x = "outer variable"
#         def inner():
#             nonlocal x
#             x = "inner variable"
#         inner()
#         return x
# print(outer())

# var="global"
# print("before global ", var)
# def global_Var():
#     global var
#     var="Inner"
#     return var
# print("after global ",global_Var())

# def add(a, b):
#     return a + b
# add(2, 3)

# try:
#     print(5/0)
# except : 
#     print("DAFA HOJAO")
# else:
#     print("HELLO FROM ELSE")
# finally:
#     print("hELLO FROM FINALLY")


# try:
#     raise TypeError("value error")
# except (TypeError, ValueError):
#     print("hello from except")
# def MyError(Exception): pass
# MyError()

# class MyError(Exception):
#     print("this is custom error")

# try:
#     raise ValueError()
# except Exception as e:
#     e.add_note("Type is invalid")
#     raise 


# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     raise Exception("Custom error") from e

# import warnings

# warnings.warn("DEPRECATED")

# try:
#     file = open("test.txt")
#     file.read()
# except FileNotFoundError:
#     print("File missing")
# finally:
#     file.close()
import sys
# while True:
#     print("Infinity")
# print(1)
# print(2)
# print(3)
# print(4)
# sys.exit()

# try:
#     raise ValueError
# except ValueError:
#     print("A")
#     raise

# try:
#     try:
#         raise ValueError
#     except:
#         raise TypeError
# except Exception as e:
#     print(type(e))
    
# try:
#     raise ValueError
# except:
#     raise TypeError
# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# print("Hello"[::-1])
# print({1, "a", 2, "b"})

# lst=[1,2,3,4]
# lst[0]=50
# print(lst)

# print("Hello".replace("l", "z"))
# print(0.1 + 0.2 == 0.3)

# dct={
#     "name":"Naimal",
#     "isStudent":True
# }
# if "name" in dct:
#     print("Name is Here")
# var=10
# def func(pos1, pos2, pos3, / ,*,NAME, AGE, ):
#     print(var)
#     var=19
# func()    
    

# for i , v in enumerate(["a", "b"]):
#     print

# for i , v in zip((1,2),("a", "b")):
#     print


# def func(abc=[1,2,4]):
#     sum(abc)
    
# func()