### **Beginner Level (1-15)**  
1. What is the output of `print(5 // 2)`?  
   a) 2.5  
   b) 2  
   c) 3  
   d) 2.0  
"B"
2. Which operator is used for exponentiation?  
   a) `^`  
   b) `**`  
   c) `//`  
   d) `%`  
"B"
3. Which variable name is **invalid**?  
   a) `_total`  
   b) `2nd_value`  
   c) `userName`  
   d) `MAX_SPEED`  
"B"
4. What does `not True` evaluate to?  
   a) `True`  
   b) `False`  
   c) `None`  
   d) Error  
"B"
5. Which code correctly assigns `x = 5` and `y = "hello"` in one line?  
   a) `x, y = 5, "hello"`  
   b) `x = 5 y = "hello"`  
   c) `x; y = 5; "hello"`  
   d) `x and y = 5, "hello"`  
"A"
6. What is the result of `"Hello" not in "Hello World"`?  
   a) `True`  
   b) `False`  
   c) Error  
   d) `None`  
"B"
7. Which operator checks if two variables point to the same object?  
   a) `==`  
   b) `=`  
   c) `is`  
   d) `in`  
"C"
8. What does `print(type(3.14))` output?  
   a) `<class 'int'>`  
   b) `<class 'float'>`  
   c) `<class 'str'>`  
   d) Syntax Error  
"B"
9. Which code deletes a variable `count`?  
   a) `remove count`  
   b) `del count`  
   c) `delete(count)`  
   d) `count = None`  
"B"
10. What is the output of `print(10 % 3)`?  
    a) 1  
    b) 0  
    c) 3  
    d) 10  
"A"
11. Which is a valid way to write `x = x + 5` as a shorthand?  
    a) `x += 5`  
    b) `x =+ 5`  
    c) `x ++ 5`  
    d) `x = 5+`  
"A"
12. What is the value of `y` after `y = -x` if `x = 7`?  
    a) `7`  
    b) `-7`  
    c) `0`  
    d) Error  
"B"
13. Which code checks if `a` and `b` have the same value?  
    a) `a = b`  
    b) `a is b`  
    c) `a == b`  
    d) `a & b`  
"C"
14. What is the result of `print(3 * "ab")`?  
    a) `ababab`  
    b) `3ab`  
    c) `ab3`  
    d) Error  
"A"
15. Which keyword is used to define a function?  
    a) `func`  
    b) `def`  
    c) `function`  
    d) `lambda`  

---
"B"
### **Intermediate Level (16-35)**  
16. What does `print(~~5)` output?  
    a) `5`  
    b) `-5`  
    c) `-6`  
    d) Error  
"A"
<!-- ~5 = -(x+1) ==> -(5+1) ==> -6
~~5 = -(x+1) ===> -(-6+1)==>-(-5)==>5 -->
17. Which code uses the walrus operator correctly?  
    a) `if x := 5 > 3:`  
    b) `if (x = 5) > 3:`  
    c) `if (x := 5) > 3:`  
    d) `if x :== 5 > 3:`  
"C"
18. What is the output of:  
    ```python  
    a = [1, 2]  
    b = a  
    b.append(3)  
    print(a)  
    ```  
    a) `[1, 2]`  
    b) `[1, 2, 3]`  
    c) `[3]`  
    d) Error  
"B"
19. Which code snippet creates a list of squares of even numbers from `data = [1,2,3,4]`?  
    a) `[x**2 for x in data if x%2==0]`  
    b) `[x^2 for x in data if x%2==0]`  
    c) `[x*2 for x in data if even]`  
    d) `[x for x in data if x%2==0]**2`  
"A"
20. What is the result of `print(5 > 3 and 10 < 5)`?  
    a) `True`  
    b) `False`  
    c) `None`  
    d) Error  
"B"
21. Which code raises a `NameError`?  
    a) `print(int("5"))`  
    b) `print(undeclared_var)`  
    c) `print(3 + 2)`  
    d) `print("Hello".lower())`  
"B"
22. What does `print("Python"[1:3])` output?  
    a) `Py`  
    b) `yth`  
    c) `yt`  
    d) `th`  
"C"
23. Which operator is used for floor division?  
    a) `/`  
    b) `//`  
    c) `%`  
    d) `**`  
"B"
24. What is the output of:  
    ```python  
    x = 10  
    y = 5  
    
    print(x //= 3)  
    ```  
    a) `3`  
    b) `3.333`  
    c) Syntax Error  
    d) `1`  
"C"
25. Which code correctly interns a small integer?  
    a) `a = 1000; b = 1000; print(a is b)`  
    b) `a = 5; b = 5; print(a is b)`  
    c) `a = "hello"; b = "hello"; print(a is b)`  
    d) `a = []; b = []; print(a is b)`  
"B" 
26. What does `print(bin(5))` output?  
    a) `0b101`  
    b) `101`  
    c) `5`  
    d) `0b110`  
"A"
27. Which code uses a membership operator?  
    a) `if x == 5:`  
    b) `if x in [1,2,3]:`  
    c) `if x is None:`  
    d) `if x and y:`  
"B"
28. What is the output of:  
    ```python  
    x = 10  
    
    print(f"{x:b}")  
    ```  
    a) `1010`  
    b) `10`  
    c) `b10`  
    d) Error  
"A"
29. Which code snippet uses logical NOT?  
    a) `if not x:`  
    b) `if x != y:`  
    c) `if x or y:`  
    d) `if x is not None:`  
"A"
30. What is the value of `y` after `y = ~5`?  
    a) `5`  
    b) `-5`  
    c) `-6`  
    d) `6`  
"C"
31. Which code correctly assigns multiple variables with type hints?  
    a) `x: int = 5, y: str = "a"`  
    b) `x, y: int, str = 5, "a"`  
    c) `x: int; y: str = 5, "a"`  
    d) Syntax Error  
"b"
32. What does `print("Hello", end=" ")` do?  
    a) Prints "Hello" with a space at the end  
    b) Raises an error  
    c) Prints "Hello" on a new line  
    d) Skips printing "Hello"  
"A"
33. Which code uses the walrus operator in a list comprehension?  
    a) `[x for x in data if x > 0]`  
    b) `[y := x**2 for x in data]` 
    c) `[y for x in data if (y := x**2) > 10]`  
    d) `[x**2 as y for x in data]`  
"C"
34. What is the output of:  
    ```python  
    a = [1, 2]  
    b = a.copy()  
    print(a is b)  
    ```  
    a) `True`  
    b) `False`  
    c) `None`  
    d) Error  
"B"
35. Which code snippet uses a ternary operator?  
    a) `x = 5 if condition else 0`  
    b) `if x > 5: print("Yes")`  
    c) `x = (5, 0)[condition]`  
    d) `x = for i in range(5)`  

---
"A"
### **Advanced Level (36-50)**  
36. Which code demonstrates name mangling?  
    a) `__password = "secret"`  
    b) `_internal = True`  
    c) `class_var = 10`  
    d) `def __init__():`  
"A"
37. What is the output of:  
    ```python  
    def f(x):  
        return x * 2  
    print([f(x) for x in range(3) if f(x) > 2])  
    ```  
    a) `[0, 2, 4]`  
    b) `[4]`  
    c) `[2, 4]`  
    d) `[0, 2]`  
"B"
38. Which code raises a `SyntaxError`?  
    a) `print("Hello, World!")`  
    b) `x = 5, y = 10`  
    c) `if 5 in [1,2,3]: print("No")`  
    d) `x = (1, 2, 3)`  
"B"
39. What does `print(__name__)` output when running a script directly?  
    a) `__main__`  
    b) `None`  
    c) `__name__`  
    d) Error  
"D"
40. Which code snippet uses a lambda function?  
    a) `lambda x: x**2`  
    b) `def f(x): return x**2`  
    c) `lambda = 5`  
    d) `x = (lambda: 5)()`  
"A"
41. What is the output of:  
    ```python  
    x = 10  
    def func():  
        global x  
        x = 5  
    func()  
    print(x)  
    ```  
    a) `10`  
    b) `5`  
    c) `None`  
    d) Error  
"5"
42. Which code snippet uses a decorator?  
    a) `@decorator`  
       `def func(): ...`  
    b) `def decorator(func): ...`  
    c) `func = decorator(func)`  
    d) All of the above  
"A"
43. What does `print("Python".find("th"))` return?  
    a) `2`  
    b) `3`  
    c) `-1`  
    d) `True`  
"A"
44. Which code correctly handles an exception?  
    a) `try: x = 5/0`  
    b) `try: x = 5/0 except: print("Error")`  
    c) `try: x = 5/0; except ZeroDivisionError: ...`  
    d) `try: ... except: ... finally: ...`  
"B"
45. What is the output of:  
    ```python  
    x = [1, 2]  
    y = x  
    y += [3]  
    print(x)  
    ```  
    a) `[1, 2]`  
    b) `[1, 2, 3]`  
    c) `[3]`  
    d) Error  
"B"
46. Which code uses `__init__` correctly?  
    a) `class Test: def __init__(): ...`  
    b) `class Test: def __init__(self): ...`  
    c) `class Test: def init(self): ...`  
    d) `class Test: def constructor(self): ...`  
"B"
47. What does `print("Hello".upper())` output?  
    a) `HELLO`  
    b) `hello`  
    c) `hElLo`  
    d) `None`  
"A"
48. Which code snippet uses a generator?  
    a) `(x**2 for x in range(5))`  
    b) `[x**2 for x in range(5)]`  
    c) `{x**2 for x in range(5)}`  
    d) `def gen(): yield x**2`  
""D"
49. What is the output of:  
    ```python  
    x = 5  
    def func():  
        x = 10  
        print(x)  
    func()  
    ```  
    a) `5`  
    b) `10`  
    c) `None`  
    d) Error  
"B"
50. Which code uses `nonlocal` correctly?  
    a) `nonlocal x = 5`  
    b) `def outer(): x=5; def inner(): nonlocal x`  
    c) `x = 5; nonlocal x`  
    d) `global nonlocal x`  
"B"
--- 

Let me know if you'd like explanations for specific questions!