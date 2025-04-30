Here are 50 MCQs covering Python strings, ranging from beginner to advanced levels. The questions include code correction, execution prediction, completion, error identification, and conceptual understanding:

---

### **Beginner Level**

1. **Which code creates a multi-line string?**  
   a) `s = "Hello\nWorld"`  
   b) `s = '''Hello World'''`  
   c) `s = 'Hello', 'World'`  
   d) `s = "Hello" + "World"`  
"B"
2. **What does `print("Hello\tWorld")` output?**  
   a) `HelloWorld`  
   b) `Hello    World` (with a tab space)  
   c) `Hello\tWorld`  
   d) Error  
"B"
3. **Which method converts a string to uppercase?**  
   a) `upper()`  
   b) `to_upper()`  
   c) `capitalize()`  
   d) `casefold()`  
"A"
""
4. **What is the result of `len("Python")`?**  
   a) 5  
   b) 6  
   c) 7  
   d) Error  
"B"
5. **What does `"Hello"[1:4]` return?**  
   a) `"ell"`  
   b) `"elo"`  
   c) `"Hel"`  
   d) `"llo"`  

---"A"

### **Intermediate Level**

6. **Which code joins a list of words with commas?**  
   a) `", ".join(["A", "B", "C"])`  
   b) `join(", ", ["A", "B", "C"])`  
   c) `["A", "B", "C"].join(", ")`  
   d) `list.join(["A", "B", "C"], ", ")`  
"A"
7. **What does `"apple,banana,cherry".split(",")` return?**  
   a) `["apple", "banana", "cherry"]`  
   b) `["apple,banana,cherry"]`  
   c) `["apple,", "banana,", "cherry"]`  
   d) Error  
"A"
8. **Which code replaces "cat" with "dog" in a string?**  
   a) `s.replace("cat", "dog")`  
   b) `s.swap("cat", "dog")`  
   c) `s.substitute("cat", "dog")`  
   d) `s.find("cat").insert("dog")`  
"A"
9. **What is the output of `print(f"{5:b}")`?**  
   a) `5`  
   b) `101`  
   c) `0b101`  
   d) Error  
"B"
10. **Which code checks if a string starts with "Py"?**  
    a) `s.startswith("Py")`  
    b) `s.first("Py")`  
    c) `s.find("Py") == 0`  
    d) `s[0:2] == "Py"`  
"A"
---

### **Advanced Level**

11. **What is the result of `"Hello" == "hello"`?**  
    a) `True`  
    b) `False`  
    c) Error  
    d) `None`  
"B"
12. **Which code demonstrates name mangling?**  
    a) `__var = 10` inside a class  
    b) `_var = 10` inside a class  
    c) `var__ = 10` inside a class  
    d) `def __init__():`  
"A"
13. **What does `sys.intern("hello")` do?**  
    a) Forces the string into the string pool  
    b) Encrypts the string  
    c) Compresses the string  
    d) Converts it to bytes  
"A"
14. **Which code raises an error?**  
    a) `int("123")`  
    b) `float("12.3")`  
    c) `int("12a")`  
    d) `str(123)`  
"C"
15. **What is the output of `print("A" > "A")`?**  
    a) `True`  
    b) `False`  
    c) Error  
    d) `None`  
"B"
---

### **Code Correction**

16. **Fix the code:**  
    ```python
    s = "Hello"
    print(s[5])
    ```  
    a) Change `s[5]` to `s[4]`  
    b) Use `s[-1]`  
    c) Both a and b  
    d) No error  
"B"
17. **What’s wrong with `print("Age: " + 25)`?**  
    a) Use `str(25)`  
    b) Use `25 + "Age: "`  
    c) Replace `+` with `,`  
    d) Both a and c  
"D"
18. **Fix the string formatting:**  
    ```python
    print("Name: %d" % "Alice")
    ```  
    a) Replace `%d` with `%s`  
    b) Replace `%d` with `%c`  
    c) Use `format()` instead  
    d) Both a and c  
"D"
---

### **Code Execution**

19. **What does `print("Hello\nWorld".splitlines())` output?**  
    a) `["Hello", "World"]`  
    b) `["Hello\nWorld"]`  
    c) `["Hello\\nWorld"]`  
    d) Error  
"A"
20. **What is the result of `"ab" + "cd" * 2`?**  
    a) `"abcdcd"`  
    b) `"ababcd"`  
    c) `"abababcd"`  
    d) `"abcdab"`  
"A"
21. **What does `print(r"\u0041")` output?**  
    a) `A`  
    b) `\u0041`  
    c) Error  
    d) `41`  
"A"
---

### **Conceptual Questions**

22. **Why is `myVar = x:b` invalid?**  
    a) `:` is not allowed in variable names  
    b) `x:b` is only valid inside f-strings  
    c) Missing quotes  
    d) `b` is undefined  
"B"
23. **What is immutability in strings?**  
    a) Strings cannot be changed after creation  
    b) Strings can be modified in-place  
    c) Strings use less memory  
    d) Strings are automatically interned  
"A"
24. **Which operator checks object identity?**  
    a) `==`  
    b) `is`  
    c) `=`  
    d) `equals()`  
"B"
---

### **Advanced String Operations**

25. **What does `"  Hello  ".strip()` return?**  
    a) `"Hello"`  
    b) `"  Hello  "`  
    c) `"Hello  "`  
    d) `"  Hello"`  
"A"
26. **Which code reverses a string?**  
    a) `s[::-1]`  
    b) `reverse(s)`  
    c) `s.reverse()`  
    d) `reversed(s)`  
"A"
27. **What is the output of `"hello".title()`?**  
    a) `"Hello"`  
    b) `"HELLO"`  
    c) `"Hello "`  
    d) `"Hello World"`  
"A"
---

### **Type Casting**

28. **What does `int(3.9)` return?**  
    a) `3`  
    b) `4`  
    c) `3.0`  
    d) Error  
"A"
29. **Which conversion is invalid?**  
    a) `str(True) → "True"`  
    b) `int("12.3") → 12`  
    c) `float("3") → 3.0`  
    d) `bool("") → False`  
"B"
30. **What is `bool("0")`?**  
    a) `True`  
    b) `False`  
    c) Error  
    d) `None`  
"A"
---

### **String Pool & Interning**

31. **What is the output?**  
    ```python
    a = "hello"
    b = "hello"
    print(a is b)
    ```  
    a) `True`  
    b) `False`  
    c) Error  
    d) `None`  
"A"
32. **Which string is NOT interned automatically?**  
    a) `"x"`  
    b) `"hello_world"`  
    c) `"A" * 20`  
    d) `"A" * 21`  
"B"
---

### **Logical Operations**

33. **Which code uses logical NOT?**  
    a) `if not x:`  
    b) `if x != y:`  
    c) `if x or y:`  
    d) `if x is None:`  
"A"
34. **What does `print(not "Hello")` output?**  
    a) `True`  
    b) `False`  
    c) `None`  
    d) Error  
"B"
---

### **String Formatting**

35. **Which code uses f-strings correctly?**  
    a) `f"Value: {5}"`  
    b) `f"Value: {5:b}"`  
    c) `f"Value: {5}"`  
    d) All of the above  
"D"
36. **What is the output of `print("Pi: {:.2f}".format(3.14159))`?**  
    a) `Pi: 3.14`  
    b) `Pi: 3.14159`  
    c) `Pi: 3.15`  
    d) Error  
"A"
---

### **Error Identification**

37. **Which code causes a `TypeError`?**  
    a) `"Hello" + 123`  
    b) `"Hello" + str(123)`  
    c) `"Hello" * 3`  
    d) `int("123")`  
"A"
38. **What is wrong with `s = 'It's a test'`?**  
    a) Missing escape for `'`  
    b) Should use double quotes  
    c) Both a and b  
    d) No error  
"C"
---

### **Code Completion**

39. **Complete the code to split a string by commas:**  
    ```python
    s = "A,B,C"
    result = s._____(",")
    ```  
    a) `split`  
    b) `join`  
    c) `partition`  
    d) `separate`  
"A"
40. **Complete the code to check if "py" is in a string (case-insensitive):**  
    ```python
    s = "Python"
    result = s.lower()._____("py")
    ```  
    a) `find`  
    b) `contains`  
    c) `startswith`  
    d) `in`  
"A"
---

### **Advanced Methods**

41. **What does `"hello".encode()` return?**  
    a) `b'hello'`  
    b) `"hello"` as bytes  
    c) `104 101 108 108 111`  
    d) Error  
"A"
42. **Which method checks if a string is numeric?**  
    a) `isnumeric()`  
    b) `isdigit()`  
    c) `isdecimal()`  
    d) All of the above  
"D"
---

### **Tricky Outputs**

43. **What is the output of `print("Hello\bWorld")`?**  
    a) `HelloWorld`  
    b) `HellWorld`  
    c) `Hello World`  
    d) `HellWorld`  
"B"
44. **What does `print("Hello, World!".count("l"))` return?**  
    a) 2  
    b) 3  
    c) 4  
    d) 5  
""B"
---

### **Advanced Comparisons**

45. **What is `print("apple" < "Banana")`?**  
    a) `True`  
    b) `False`  
    c) Error  
    d) `None`  
"B"
46. **What is the result of `"123" == 123`?**  
    a) `True`  
    b) `False`  
    c) Error  
    d) `None`  
"B"
---

### **Miscellaneous**

47. **Which code creates a raw string?**  
    a) `s = r"Hello\nWorld"`  
    b) `s = "Hello\\nWorld"`  
    c) `s = raw"Hello\nWorld"`  
    d) Both a and b  
"A"
48. **What is the output of `print("Hello, {}".format("World"))`?**  
    a) `Hello, World`  
    b) `Hello, {}`  
    c) Error  
    d) `Hello, "World"`  
""
"A"
49. **Which method removes leading/trailing whitespace?**  
    a) `strip()`  
    b) `trim()`  
    c) `clean()`  
    d) `remove()`  
"A"
50. **What does `"Hello".center(10, "*")` return?**  
    a) `**Hello***`  
    b) `***Hello**`  
    c) `**Hello**`  
    d) `****Hello****`  
"A"
--- 

Let me know if you’d like explanations for any specific question! 😊