### **Code Syntax & Error-Based MCQs**  
1. What happens when you run:  
   ```python  
   x = 5.5  
   print(int(x))  
   ```  
   a) 5.5  
   b) 5  
   c) Error  
    " "
2. Which code creates a valid bytearray?  
   a) `bytearray("hello")`  
   b) `bytearray([72, 101, 108])`  
   c) `bytearray(10)`  
    "b "

3. What is the output of:  
   ```python  
   print(bool(""))  
   ```  
   a) `True`  
   b) `False`  
    "b "
4. Which line causes an error?  
   ```python  
   a) a = {1, 2, 3}  
   b) a.add(4)  
   c) a[0] = 5  
   ```
   " c"  

5. What does `memoryview(b"test")[1:3]` return?  
   a) `b"es"`  
   b) " " memoryview object  
   c) `b"te"`  
    b
6. Which code converts "3.14" to a float?  
   a) `float(3.14)`  
   b) `float("3.14")`  
   c) `str(3.14)`  
   " "
7. What is the output of:  
   ```python  
   print(type(range(5)))  
   ```  
   a) `<class 'list'>`  
   b) `<class 'generator'>`  
   c) `<class 'range'>`  
    " "

8. Which code creates a valid frozenset?  
   a) `frozenset([1, 2, 3])`  
   b) `frozenset({1: "a"})`  
   c) `frozenset(1, 2, 3)`  
    a
9. What is the output of:  
   ```python  
   x = 300  
   y = 300  
   print(x is y)  
   ```  
   a) `True`  
   b) `False`  
" "
10. Which code snippet will raise a `TypeError`?  
    a) `"5" + 5`  
    b) `5 + 5.5`  
    c) `int("5")`  
" "
11. What does `z.imag` return if `z = 3+4j`?  
    a) 3  
    b) 4  
    c) 7  
    4
12. Which code correctly initializes a list with mixed types?  
    a) `list[str, int] = [1, "a"]`  
    b) `list = [1, "a"]`  
    c) `list: list = [1, "a"]`  
" "b
13. What is the output of:  
    ```python  
    print(bytearray(b"Hi")[0])  
    ```  
    a) `H`  
    b) `72`  
    c) `104`  
" "
14. Which code creates a valid type hint for a dictionary with integer keys and string values?  
    a) `dict[int: str]`  
    b) `dict[int, str]`  
    c) `dict[int | str]`  
b
15. What happens when you run:  
    ```python  
    my_set = {1, 1, 2}  
    print(my_set)  
    ```  
    a) `{1, 2}`  
    b) `{1, 1, 2}`  
    c) Error  
a
16. Which code snippet uses `isinstance()` correctly?  
    a) `isinstance(5, "int")`  
    b) `isinstance(5, int)`  
    c) `isinstance(int, 5)`  
b
17. What is the output of:  
    ```python  
    print(3 + 4j).real  
    ```  
    a) 3  
    b) 4  
    c) 7  
a
18. Which code truncates 8.9 to 8?  
    a) `int(8.9)`  
    b) `float(8.9)`  
    c) `str(8.9)`  

19. What does `range(1, 10, 2)[3]` return?  
    a) 5  
    b) 7  
    c) Error  
b
20. Which code modifies a bytearray?  
    a) `ba = b"hello"`  
    b) `ba[0] = 65`  
    c) `ba = bytearray(b"hello")`  
c
21. What is the output of:  
    ```python  
    print(None is None)  
    ```  
    a) `True`  
    b) `False`  
" "
22. Which code creates a valid tuple?  
    a) `(1, 2, 3)`  
    b) `tuple = 1, 2, 3`  
    c) Both a and b  
" "
23. What does `chr(65)` return?  
    a) `'A'`  
    b) `65`  
    c) `b'" "'`  

24. Which code raises an error?  
    ```python  
    a = (1, 2)  
    a[0] = 3  
    ```  
" "
25. What is the output of:  
    ```python  
    print(bool([0]))  
    ```  
    a) `True`  
    b) `False`  
" "
---

### **Conceptual MCQs**  
26. What does "duck typing" emphasize?  
    a) Object inheritance  
    b) Object capabilities  
    c) Static typing  
" "
27. What is the purpose of `memoryview`?  
    a) Store text data  
    b) Access binary data without copying  
    c) Create immutable lists  
"B"
28. Why are integers from -5 to 256 interned?  
    a) To improve performance  
    b) To enforce type safety  
    c) To enable mutation  
" a"
29. What does `id()` return?  
    a) Object type  
    b) Memory address identifier  
    c) Hash value  
" b"
30. Which is **not** a falsy value?  
    a) `""`  
    b) `[]`  
    c) `1`  
" "c
31. What distinguishes `bytes` from `bytearray`?  
    a) Mutability  
    b) Storage size  
    c) Encoding  
" "a
32. What does `__init__` handle?  
    a) Object creation  
    b) Object initialization  
    c) Memory allocation  
" "b
33. What is the primary use of `frozenset`?  
    a) Mutable storage  
    b) Immutable storage  
    c) Key-value pairs  
" "b
34. Which describes "truthy" values?  
    a) `0`, `""`, `None`  
    b) Non-zero numbers, non-empty strings  
    c) All boolean `False`  
" "b
35. What does `isinstance()` check?  
    a) Object identity  
    b) Object type/class  
    c) Object value  
" "b
36. What is the purpose of type hints?  
    a) Runtime enforcement  
    b) Documentation/static checking  
    c) Memory optimization  
" "b
37. Which is **not** a sequence type?  
    a) `list`  
    b) `set`  
    c) `tuple`  
    b
38. What does `range(5)` generate?  
    a) `[0,1,2,3,4]`  
    b) " " sequence object  
    c) " " generator  
    b
39. What is the `None` type used for?  
    a) Represent absence of value  
    b) Zero-like placeholder  
    c) Boolean `False`  
a
40. Which is true about Python strings?  
    a) Mutable  
    b) Use triple quotes for single-line  
    c) Immutable  
c
41. What does `z.imag` access?  
    a) Real part of a complex number  
    b) Imaginary part  
    c) Magnitude  
b
42. What distinguishes `tuple` from `list`?  
    a) Mutability  
    b) Ordered storage  
    c) Indexing  
a
43. Which is a valid use of `@staticmethod`?  
    a) Access instance variables  
    b) Create utility functions  
    c) Modify class state  

44. What is the purpose of `Union` in type hints?  
    a) Combine multiple types  
    b) Enforce strict typing  
    c) Replace inheritance  
a
45. Which is **not** a binary type?  
    a) `bytes`  
    b) `memoryview`  
    c) `frozenset`  
c
46. What does `LOAD_FAST` do in bytecode?  
    a) Load global variables  
    b) Load local variables  
    c) Load constants  
b
47. What is the effect of `bool(-5)`?  
    a) `False`  
    b) `True`  
b
48. What is the result of `5.5 + 2`?  
    a) `7.5`  
    b) `7`  
    c) Error  
a
49. Which describes Python integers?  
    a) Limited to 32-bit  
    b) Arbitrary precision  
    c) Always interned 
    b

50. What is the role of `chr()`?  
    a) Convert ASCII to character  
    b) Convert character to ASCII  
    c) Check encoding  
a
--- 
