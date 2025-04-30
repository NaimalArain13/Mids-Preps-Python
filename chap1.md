Here are 40 MCQs covering basic to advanced Python concepts from the document:

### **Basic Level (1-15)**
1. **What is Python primarily known for?**  
   a) Speed  
   b) Simplicity and readability  
   c) Low-level memory access  
   d) Static typing  
   "b" 

2. **Which programming paradigms does Python support?**  
   a) Only procedural  
   b) Procedural, object-oriented, and functional  
   c) Only functional  
   d) Only object-oriented  
   "b" 

3. **Python’s role in Agentic AI includes:**  
   a) Image recognition only  
   b) Enabling autonomous decision-making with frameworks like LangChain  
   c) Hardware programming  
   d) Database management  
   "b" 

4. **Which is a practical application of Python in cybersecurity?**  
   a) Web development  
   b) Penetration testing  
   c) Data visualization  
   d) Robotics  
   "b" 

5. **Python bytecode is stored in:**  
   a) `.py` files  
   b) `.pyc` files  
   c) `.exe` files  
   d) `.txt` files  
   "b" 

6. **What is the purpose of the `dis` module?**  
   a) Compile code  
   b) Disassemble bytecode  
   c) Debug runtime errors  
   d) Optimize performance  
   "b" 

7. **Incorrect indentation in Python leads to:**  
   a) A warning  
   b) A syntax error  
   c) A runtime error  
   d) No effect  
   "b" 

8. **What does `x: int = 5` demonstrate?**  
   a) Dynamic typing  
   b) Type hinting  
   c) Inheritance  
   d) Polymorphism  
   "b" 

9. **Python is a:**  
   a) Statically-typed language  
   b) Dynamically-typed language  
   c) Compiled language  
   d) Assembly language  
   "b" 

10. **Which feature is absent in object-based languages?**  
    a) Encapsulation  
    b) Inheritance  
    c) Objects  
    d) Methods  
    "b" 

11. **In Python, all data types are:**  
    a) Primitives  
    b) Objects  
    c) Static  
    d) Immutable  
    "b" 

12. **Duck typing focuses on an object’s:**  
    a) Type  
    b) Capabilities  
    c) Memory address  
    d) Class hierarchy  
    "b" 

13. **What is the output of `print(type("5"))`?**  
    a) `<class 'int'>`  
    b) `<class 'str'>`  
    c) `<class 'float'>`  
    d) `<class 'list'>`  
    "b" 

14. **Which is used to create a class in Python?**  
    a) `class` keyword  
    b) `def` keyword  
    c) `struct` keyword  
    d) `new` keyword  
    "a" 

15. **What does `self` represent in a class method?**  
    a) The class itself  
    b) The instance of the class  
    c) A static method  
    d) A global variable  
    "b" 

---

### **Intermediate Level (16-30)**
16. **Which framework is used for Agentic AI?**  
    a) Django  
    b) Flask  
    c) LangChain  
    d) Pandas  
    "c" 

17. **The Python Virtual Machine (PVM) executes:**  
    a) Source code  
    b) Bytecode  
    c) Machine code  
    d) Assembly code  
    "b" 

18. **What is the standard indentation in Python?**  
    a) 2 spaces  
    b) 4 spaces  
    c) 8 spaces  
    d) Tabs  
    "b"

19. **Which is a valid type hint for a list of integers?**  
    a) `list<int>`  
    b) `list[int]`  
    c) `List[Int]`  
    d) `Array[int]`  
    "b" 

20. **Which principle is NOT part of OOP?**  
    a) Encapsulation  
    b) Inheritance  
    c) Duck typing  
    d) Polymorphism  
    "c" 

21. **What is the output of `100.bit_length()`?**  
    a) 3  
    b) 7  
    c) 100  
    d) Error  
    "d"  (Correct syntax: `(100).bit_length()`)

22. **First-class functions in Python can be:**  
    a) Only called  
    b) Assigned to variables  
    c) Stored in lists  
    d) Both b and c  
    "b" 

23. **Which method initializes an object?**  
    a) `__init__`  
    b) `__main__`  
    c) `__self__`  
    d) `__new__`  
    "a" 

24. **What does `def greet() -> str:` specify?**  
    a) Return type hint  
    b) Parameter type  
    c) Dynamic typing  
    d) Static compilation  
    "a" 

25. **In duck typing, an object with a `speak()` method can:**  
    a) Only be a `Human` class  
    b) Be treated as any type with `speak()`  
    c) Not be used polymorphically  
    d) Cause a syntax error  
    "b" 

26. **Which tool checks type hints at compile time?**  
    a) Python interpreter  
    b) `mypy`  
    c) `dis` module  
    d) PVM  
    "b" 

27. **Bytecode is generated during:**  
    a) Runtime  
    b) Compilation  
    c) Interpretation  
    d) Debugging  
    "b" 

28. **Which is NOT a Python application?**  
    a) Web development  
    b) Quantum computing  
    c) Data analysis  
    d) Automation  
    "b" 

29. **The `__pycache__` directory stores:**  
    a) Source code  
    b) Bytecode  
    c) Logs  
    d) Documentation  
    "b" 

30. **Which is true about Python’s OOP?**  
    a) Supports multiple inheritance  
    b) No polymorphism  
    c) No encapsulation  
    d) Uses `extends` keyword  
    "a" 

---

### **Advanced Level (31-40)**
31. **What does `LOAD_FAST` in bytecode indicate?**  
    a) Loading a global variable  
    b) Loading a local variable  
    c) Loading a constant  
    d) Loading an attribute  
    "b" 

32. **Which code uses duck typing correctly?**  
    ```python
    def func(obj):
        obj.quack()
    ```  
    a) Requires `obj` to be a `Duck`  
    b) Works if `obj` has `quack()`  
    c) Causes a syntax error  
    d) Uses inheritance  
    "b" 

33. **What is the result of `dis.dis(func)`?**  
    a) Compiles `func`  
    b) Disassembles `func`’s bytecode  
    c) Executes `func`  
    d) Optimizes `func`  
    "b" 

34. **Which is a valid complex type hint?**  
    a) `dict[str: int]`  
    b) `dict[str, int]`  
    c) `dict[str -> int]`  
    d) `dict[str, int]` (Python 3.9+)  
    "d" 

35. **What is the purpose of `@staticmethod`?**  
    a) Access instance variables  
    b) Define a method without `self`  
    c) Enable inheritance  
    d) Replace `__init__`  
    "b" 

36. **Which statement about Python bytecode is false?**  
    a) Platform-independent  
    b) Requires a Python interpreter  
    c) Machine-specific  
    d) Cached in `.pyc` files  
    "c" 

37. **In Python, polymorphism is achieved via:**  
    a) Function overloading  
    b) Duck typing  
    c) Static methods  
    d) Private variables  
    "a" 

38. **What is the output of:**
    ```python
    def test():
        return "Hello"
    print(type(test))
    ```  
    a) `<class 'function'>`  
    b) `<class 'str'>`  
    c) `<class 'method'>`  
    d) `<class 'NoneType'>`  
    "a" 

39. **Which is true about type hints?**  
    a) Enforced at runtime  
    b) Improve code readability  
    c) Required for all variables  
    d) Slow down execution  
    "b" 

40. **Which code block follows PEP8 indentation?**  
    a) 
    ```python
    if True:
        print("Hello")
    ```  
    b) 
    ```python
    if True:
    print("Hello")
    ```  
    c) 
    ```python
    if True:
      print("Hello")
    ```  
    "a"  

---

These questions cover Python syntax, concepts, bytecode, OOP, type hints, and advanced features, suitable for a comprehensive test.