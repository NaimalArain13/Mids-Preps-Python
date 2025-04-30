Here are 50 MCQs on Python exception handling, organized by difficulty level:

---

### **Beginner Level**

1. **Which keyword is used to handle exceptions in Python?**  
A) `catch`  
B) `except`  
C) `handle`  
D) `resolve`  
"B"
2. **What is the output if `10 / 0` is executed without exception handling?**  
A) `0`  
B) `Infinity`  
C) `ZeroDivisionError`  
D) `SyntaxError`  
"C"
3. **Which block is used to test code for errors?**  
A) `try`  
B) `check`  
C) `test`  
D) `validate`  
"A"
4. **What does the `finally` block do?**  
A) Runs only if no errors occur  
B) Runs regardless of errors  
C) Catches specific errors  
D) Skips code execution  
"B"
5. **Which exception is raised for invalid type operations?**  
A) `ValueError`  
B) `TypeError`  
C) `IndexError`  
D) `KeyError`  
"B"
6. **What is the output of:**  
```python
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
else:
    print("Success")
```  
A) `5.0`  
B) `Success`  
C) `5.0` followed by `Success`  
D) `Error`  
"B"
7. **Which code catches all exceptions?**  
A) `except:`  
B) `except Exception:`  
C) `except BaseException:`  
D) All of the above  
"D"
8. **What is the purpose of `else` in exception handling?**  
A) Handle errors  
B) Execute code if no errors occur  
C) Clean up resources  
D) Rerun the `try` block  
"B"
9. **Which exception is raised for accessing a non-existent list index?**  
A) `KeyError`  
B) `IndexError`  
C) `ValueError`  
D) `NameError`  
"B"
10. **What is the output of:**  
```python
try:
    print("Hello")
except:
    print("Error")
```  
A) `Hello`  
B) `Error`  
C) `SyntaxError`  
D) No output  
"A"
---

### **Intermediate Level**

11. **How to catch multiple exceptions in one `except` block?**  
A) `except (TypeError, ValueError)`  
B) `except [TypeError, ValueError]`  
C) `except TypeError or ValueError`  
D) `except TypeError, ValueError`  
"A"
12. **What is the output of:**  
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("A")
except ArithmeticError:
    print("B")
```  
A) `A`  
B) `B`  
C) Both `A` and `B`  
D) Error  
"A"
13. **Which keyword raises a custom exception?**  
A) `throw`  
B) `raise`  
C) `except`  
D) `assert`  
"B"
14. **What is the output of:**  
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
15. **Which code correctly creates a custom exception?**  
A) `class MyError(Exception): pass`  
B) `def MyError(Exception): pass`  
C) `MyError = Exception()`  
D) `create MyError(Exception)`  
"A"
16. **What is the output of:**  
```python
try:
    print(int("text"))
except ValueError:
    print("A")
except Exception:
    print("B")
```  
A) `A`  
B) `B`  
C) `SyntaxError`  
D) No output  
"A"
17. **Which code ensures a file is closed after operations?**  
A) `finally: file.close()`  
B) `with open(...) as file:`  
C) Both A and B  
D) `except: file.close()`  
"C"
18. **What does `raise ValueError("Invalid")` do?**  
A) Catches an error  
B) Creates a warning  
C) Triggers a custom error  
D) Logs a message  
"C"
19. **Which exception is NOT part of the built-in hierarchy?**  
A) `FileNotFoundError`  
B) `ConnectionError`  
C) `NetworkError`  
D) `MemoryError`  
"C"
20. **What is the output of:**  
```python
try:
    print(undefined_var)
except NameError:
    print("A")
```  
A) `A`  
B) `NameError`  
C) `SyntaxError`  
D) No output  
"A"
---

### **Advanced Level**

21. **What is the purpose of `__context__` in exceptions?**  
A) Track exception chains  
B) Store error messages  
C) Define custom exceptions  
D) Replace `try` blocks  
"A"
22. **Which method is used to add notes to exceptions (Python 3.11+)?**  
A) `add_note()`  
B) `append_note()`  
C) `Exception.__notes__`  
D) `annotate()`  
"A"
23. **What is the output of:**  
```python
try:
    raise ValueError
except:
    raise TypeError
```  
A) `ValueError`  
B) `TypeError`  
C) Both errors  
D) `RuntimeError`  
"C"
24. **Which code uses `assert` correctly?**  
A) `assert x > 0, "x must be positive"`  
B) `assert (x > 0): "Invalid"`  
C) `assert if x < 0`  
D) `assert x > 0 else "Error"`  
"A"
25. **What does `sys.exc_info()` return?**  
A) Current exception details  
B) List of all exceptions  
C) Stack trace  
D) Error codes  
"A"
26. **Which code re-raises the current exception?**  
A) `raise`  
B) `raise current`  
C) `raise Exception`  
D) `pass`  
"C"
27. **What is the output of:**  
```python
class CustomError(Exception): pass
try:
    raise CustomError
except Exception as e:
    print(isinstance(e, CustomError))
```  
A) `True`  
B) `False`  
C) `Error`  
D) `None`  
"A"
28. **Which context manager handles exceptions?**  
A) `@contextmanager`  
B) `with`  
C) `try`  
D) All of the above  
"D"
29. **What is the purpose of `ExceptionGroup` (Python 3.11+)?**  
A) Handle multiple exceptions  
B) Create exception hierarchies  
C) Replace `finally`  
D) Log errors  
"A"
30. **Which code uses `warnings.warn()` correctly?**  
A) `warnings.warn("Deprecated")`  
B) `warn("Deprecated")`  
C) `raise Warning("Deprecated")`  
D) `alert("Deprecated")`  
"A"
---

### **Code Correction/Completion**

31. **Fix the code:**  
```python
try:
    print(10 / 0)
except:
    print("Error")
finally
    print("Done")
```  
A) Add `:` after `finally`  
B) Indent `print("Done")`  
C) Add `except ZeroDivisionError`  
D) Remove `finally`  
"A"
32. **Complete the code to catch `KeyError`:**  
```python
try:
    d = {"key": "value"}
    print(d["invalid"])
______ KeyError:
    print("Missing key")
```  
A) `except`  
B) `catch`  
C) `handle`  
D) `resolve`  
"A"
33. **Fix the code:**  
```python
raise "Custom error message"
```  
A) `raise Exception("Custom error message")`  
B) `raise "Custom error message" as e`  
C) `except "Custom error message"`  
D) `pass`  
"A"
34. **Complete the code to raise a custom error:**  
```python
class MyError(______): pass
raise MyError("Error")
```  
A) `BaseException`  
B) `Exception`  
C) `object`  
D) `Error`  
"B"
35. **What is wrong with:**  
```python
try:
    file = open("test.txt")
    file.read()
except FileNotFoundError:
    print("File missing")
finally:
    file.close()
```  
A) Missing `else` block  
B) `file` may be undefined in `finally`  
C) No `raise` statement  
D) Incorrect exception order  
"B"
---

### **Conceptual Questions**

36. **What is exception "chaining"?**  
A) Linking multiple exceptions  
B) Raising new exceptions while preserving original traceback  
C) Grouping exceptions  
D) Catching nested exceptions  
"B"
37. **When should `BaseException` be caught?**  
A) Never  
B) For keyboard interrupts  
C) For system exits  
D) All of the above  
"D"
38. **What is "EAFP" in Python?**  
A) Error Handling and Failsafe Procedures  
B) Easier to Ask for Forgiveness than Permission  
C) Exception Avoidance for Fast Performance  
D) Explicitly Asserting Function Parameters  
"B"
39. **Which is a checked exception in Python?**  
A) `SyntaxError`  
B) `IndexError`  
C) Python has no checked exceptions  
D) `IOError`  
"C"
40. **What is the base class for all exceptions?**  
A) `Exception`  
B) `BaseException`  
C) `object`  
D) `Error`  
"B"
---

### **Code Execution**

41. **What is the output of:**  
```python
try:
    print(1 + "1")
except TypeError:
    print("A")
except ValueError:
    print("B")
```  
A) `A`  
B) `B`  
C) `TypeError`  
D) `SyntaxError`  
"A"
42. **What does `print(issubclass(ZeroDivisionError, ArithmeticError))` return?**  
A) `True`  
B) `False`  
C) `Error`  
D) `None`  
"A"
43. **What is the output of:**  
```python
try:
    raise ValueError
except ValueError:
    print("A")
    raise
```  
A) `A` followed by `ValueError`  
B) `A`  
C) `ValueError`  
D) `RuntimeError`  
"A"
44. **What is the output of:**  
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
45. **What does `assert False, "Message"` do?**  
A) Raises `AssertionError`  
B) Prints "Message"  
C) Returns `False`  
D) Passes silently  
"A"
---

### **Expert Level**

46. **What is the purpose of `__traceback__` in exceptions?**  
A) Store stack trace details  
B) Compare exceptions  
C) Create new exceptions  
D) Log errors  
"A"
47. **Which code uses `contextlib.suppress` correctly?**  
A) `with suppress(ValueError): ...`  
B) `try: ... except suppress:`  
C) `from contextlib import suppress`  
D) Both A and C  

48. **What is the output of:**  
```python
try:
    try:
        raise ValueError
    except:
        raise TypeError
except Exception as e:
    print(type(e))
```  
A) `<class 'ValueError'>`  
B) `<class 'TypeError'>`  
C) `<class 'Exception'>`  
D) `<class 'RuntimeError'>`  
"B"
49. **Which code uses `sys.excepthook`?**  
A) `sys.excepthook = custom_handler`  
B) `except sys.excepthook:`  
C) `raise excepthook()`  
D) `import excepthook`  

50. **What does `raise ...` (ellipsis) do in Python 3.11+?**  
A) Re-raises the current exception  
B) Raises `EllipsisError`  
C) Skips code  
D) Creates a placeholder  

---

These questions cover syntax, behavior, best practices, and advanced features of Python exception handling. Let me know if you need further explanations!