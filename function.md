Here are 50 MCQs on Python functions and modules, covering beginner to advanced levels:

---

### **Beginner Level**

1. **What is a Python module primarily used for?**  
A) Storing data  
B) Organizing and reusing code  
C) Creating loops  
D) Defining variables  
"B"
2. **Which keyword is used to import a module?**  
A) `include`  
B) `require`  
C) `import`  
D) `use`  
"C"
3. **What is the output of `print(type(lambda x: x))`?**  
A) `<class 'function'>`  
B) `<class 'lambda'>`  
C) `SyntaxError`  
D) `<class 'int'>`  
"A"
4. **Which line correctly defines a function?**  
A) `def my_func:`  
B) `function my_func():`  
C) `def my_func():`  
D) `define my_func():`  
"D"
5. **What is the result of `math.sqrt(9)` after `import math`?**  
A) `3`  
B) `3.0`  
C) `9`  
D) `Error`  
"A"
6. **Which code imports only the `sqrt` function from `math`?**  
A) `import sqrt from math`  
B) `from math import sqrt`  
C) `import math.sqrt`  
D) `include math.sqrt`  
"B"
7. **What is the output of:**  
```python
def greet():
    return "Hello"
print(greet())
```  
A) `Hello`  
B) `None`  
C) `Error`  
D) No output  
"A"
8. **What is the default return value of a function without a `return` statement?**  
A) `0`  
B) `None`  
C) `True`  
D) `Error`  
"B"
9. **Which code creates a function with a default argument?**  
A) `def func(a=5):`  
B) `def func(a, 5):`  
C) `def func(a:5):`  
D) `def func(a, default=5):`  
"A"
10. **What is the scope of a variable defined inside a function?**  
A) Global  
B) Local  
C) Module-level  
D) Universal  
"B"
---

### **Intermediate Level**

11. **What does `*args` represent in a function definition?**  
A) Keyword arguments  
B) Positional arguments as a tuple  
C) Mandatory arguments  
D) Return values  
"B"
12. **Which code uses a lambda function to double a number?**  
A) `lambda x: x * 2`  
B) `def double(x): return x*2`  
C) `lambda double: x*2`  
D) `lambda (x): x*2`  
"A"
13. **What is the output of:**  
```python
def func(a, b=2):
    return a + b
print(func(5))
```  
A) `7`  
B) `5`  
C) `Error`  
D) `2`  
"A"
14. **Which code correctly uses `**kwargs`?**  
A) `def func(**args):`  
B) `def func(**kwargs):`  
C) `def func(***kwargs):`  
D) `def func(**kw):`  
"B"
15. **What is the result of:**  
```python
x = 10
def func():
    x = 5
func()
print(x)
```  
A) `10`  
B) `5`  
C) `None`  
D) `Error`  
"A"
16. **Which method modifies a list in-place?**  
A) `.append()`  
B) `+` operator  
C) `.copy()`  
D) `return new_list`  
"A"
17. **What is the output of:**  
```python
def func(a, /, b):
    return a + b
print(func(1, 2))
```  
A) `3`  
B) `Error`  
C) `1`  
D) `2`  
"A"
18. **Which code imports a module with an alias?**  
A) `import math as m`  
B) `from math import sqrt as s`  
C) `import math from m`  
D) `alias math = m`  
"A"
19. **What is the purpose of `__init__.py` in a folder?**  
A) Marks the folder as a Python package  
B) Runs code on module import  
C) Initializes variables  
D) Both A and B  
"D"
20. **What is the output of:**  
```python
print(__name__)
```  
A) `__main__`  
B) `__name__`  
C) `main`  
D) Depends on execution context  
"D"
---

### **Advanced Level**

21. **What is a closure in Python?**  
A) A nested function capturing outer variables  
B) A built-in decorator  
C) A module-level function  
D) A type of exception  
"A"
22. **Which code uses a decorator?**  
A) `@decorator def func(): ...`  
B) `def decorator(func): ...`  
C) `decorate(func)`  
D) `func = decorator(func)`  
"A"
23. **What is the output of:**  
```python
def gen():
    yield 1
    yield 2
g = gen()
print(next(g), next(g))
```  
A) `1 2`  
B) `2 1`  
C) `1 1`  
D) `Error`  
"A"
24. **Which code creates a generator expression?**  
A) `(x for x in range(5))`  
B) `[x for x in range(5)]`  
C) `{x for x in range(5)}`  
D) `x: for x in range(5)`  
"A"
25. **What is the result of:**  
```python
def func(a, b=[]):
    b.append(a)
    return b
print(func(1), func(2))
```  
A) `[1] [2]`  
B) `[1] [1, 2]`  
C) `[1, 2] [1, 2]`  
D) `Error`  
"C"
---

### **Code Correction/Completion**

26. **Fix the error:**  
```python
def add(a, b)
    return a + b
```  
A) Add `:` after `b)`  
B) Replace `def` with `function`  
C) Use `return a,b`  
D) Indent `return`  
"A"
27. **Complete the code to import `sqrt` and `pi`:**  
```python
from math import ______  
```  
A) `sqrt, pi`  
B) `sqrt & pi`  
C) `sqrt; pi`  
D) `sqrt + pi`  
"A"
28. **Fix the code:**  
```python
def func():
print("Hello")
```  
A) Add parentheses to `print`  
B) Indent `print`  
C) Add `return`  
D) Use `printf`  
"B"
29. **Complete the code to unpack `args`:**  
```python
def func(*args):
    return sum(______)
```  
A) `args`  
B) `*args`  
C) `**args`  
D) `args[]`  
"C"
30. **What is wrong with:**  
```python
def func(a, b=[]):
    b.append(a)
    return b
```  

A) Default mutable argument  
B) Missing `return`  
C) Incorrect parameter syntax  
D) No issue  
"D"
---

### **Conceptual Questions**

31. **How are arguments passed in Python?**  
A) Pass by value  
B) Pass by reference  
C) Pass by object reference  
D) Pass by pointer  
"C"
32. **What is the purpose of `if __name__ == "__main__":`?**  
A) Run code only when the script is executed directly  
B) Import modules  
C) Define global variables  
D) Create a loop  
"A"
33. **What is a generator’s advantage?**  
A) Memory efficiency  
B) Faster execution  
C) Simplifies recursion  
D) Handles exceptions  
"A"
34. **Which is a valid use of `functools.lru_cache`?**  
A) Memoization  
B) Code formatting  
C) File handling  
D) Data serialization  
"A"
35. **What is the output of:**  
```python
print(globals() is locals())
```  
A) `True` in module scope  
B) `False` in function scope  
C) Depends on context  
D) Always `False`  
"C"
---

### **Code Execution**

36. **What is the output of:**  
```python
def func(x):
    return x ** 2
print(func(3))
```  
A) `9`  
B) `6`  
C) `3`  
D) `27`  
"A"
37. **What does `print(list(range(3)))` output?**  
A) `[0, 1, 2]`  
B) `[1, 2, 3]`  
C) `[3]`  
D) `Error`  
"A"
38. **What is the result of:**  
```python
def func():
    try:
        return 1
    finally:
        return 2
print(func())
```  
A) `1`  
B) `2`  
C) `None`  
D) Error  
"B"
39. **What is the output of:**  
```python
import sys
print(sys.version)
```  
A) Python version string  
B) `sys` module path  
C) `None`  
D) Error  
"A"
40. **What does `help(math.sqrt)` display?**  
A) Documentation for `sqrt`  
B) `math` module path  
C) `sqrt` source code  
D) Error  
"A"

---

### **Expert Level**

41. **What is the output of:**  
```python
a = [1, 2]
def func(x=a):
    return x
a.append(3)
print(func())
```  
A) `[1, 2]`  
B) `[1, 2, 3]`  
C) `Error`  
D) `None`  
"B"
42. **Which code uses a decorator to time a function?**  
A) `@timeit def func(): ...`  
B) `timeit(func())`  
C) `func = timeit(func)`  
D) `def timeit(func): ...`  
"A"
43. **What is the result of:**  
```python
def func():
    yield from [1, 2]
g = func()
print(list(g))
```  
A) `[1, 2]`  
B) `[ ]`  
C) `1`  
D) `Error`  
"A"
44. **Which code uses `functools.partial`?**  
A) `partial(func, arg=5)`  
B) `func.partial(arg=5)`  
C) `from functools import partial`  
D) Both A and C  
"D"
45. **What is the output of:**  
```python
def func():
    return lambda x: x + 1
f = func()
print(f(2))
```  
A) `3`  
B) `2`  
C) `1`  
D) `Error`  
"A"
---

### **Advanced Concepts**

46. **What is monkey patching?**  
A) Modifying code at runtime  
B) A debugging technique  
C) A type of recursion  
D) An exception handler  
"A"
47. **What is the purpose of `__slots__`?**  
A) Optimize memory in classes  
B) Define module exports  
C) Create decorators  
D) Handle exceptions  
"A"
48. **Which code uses `inspect` module?**  
A) `inspect.getsource(func)`  
B) `import inspect`  
C) `inspect(func)`  
D) `from inspect import *`  
"A"
49. **What is the result of:**  
```python
def func():
    return (x for x in range(3))
print(type(func()))
```  
A) `<class 'generator'>`  
B) `<class 'function'>`  
C) `<class 'list'>`  
D) `<class 'tuple'>`  
"A"
50. **What is the output of:**  
```python
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        return x
    return inner
f = outer()
print(f(), f())
```  
A) `6 7`  
B) `6 6`  
C) `5 5`  
D) `Error`  
"A"
---

These questions cover a wide range of topics, from basic syntax to advanced concepts like decorators and generators. Let me know if you need further refinements!