Here are 50 MCQs covering Python control flow and loops, ranging from beginner to advanced levels:

---

### **Beginner Level**

1. **Which keyword is used to handle alternative conditions after `if`?**  
   a) `elseif`  
   b) `elif`  
   c) `otherwise`  
   d) `alt`  
"B"
2. **What does `print(5 > 3 and 2 < 1)` output?**  
   a) `True`  
   b) `False`  
   c) `Error`  
   d) `None`  
"B"
3. **Which loop iterates over a sequence?**  
   a) `for`  
   b) `while`  
   c) `repeat`  
   d) `do-while`  
"A"
4. **What is the output of `for i in range(3): print(i)`?**  
   a) `0 1 2`  
   b) `1 2 3`  
   c) `3`  
   d) `Error`  
"A"
5. **Which operator checks equality?**  
   a) `=`  
   b) `==`  
   c) `===`  
   d) `!=`  
"B"
---

### **Intermediate Level**

6. **What does this code do?**  
   ```python  
   x = 10  
   while x > 0:  
       x -= 1  
   ```  
   a) Creates an infinite loop  
   b) Counts from 10 to 1  
   c) Counts from 9 to 0  
   d) Causes an error  
"B"
7. **Which code snippet correctly uses `continue`?**  
   a)  
   ```python  
   for i in range(5):  
       if i == 2:  
           continue  
       print(i)  
   ```  
   b)  
   ```python  
   for i in range(5):  
       continue if i == 2  
   ```  
   c)  
   ```python  
   for i in range(5):  
       break if i == 2  
   ```  
   d) None  
"A"
8. **What is the output of:**  
   ```python  
   nums = [1, 2, 3]  
   for n in nums:  
       print(n * 2)  
   ```  
   a) `2 4 6`  
   b) `1 2 3`  
   c) `[2, 4, 6]`  
   d) `Error`  
"A"
9. **Which code checks if a number is even?**  
   a) `if num / 2 == 0:`  
   b) `if num % 2 == 0:`  
   c) `if num // 2 == 0:`  
   d) `if num * 2 == 0:`  
"B"
10. **What does `range(2, 10, 2)` generate?**  
    a) `2 4 6 8`  
    b) `2 4 6 8 10`  
    c) `0 2 4 6 8`  
    d) `2 3 4 5 6 7 8 9`  
"A"
---

### **Advanced Level**

11. **What is the output of:**  
    ```python  
    for i in range(3):  
        pass  
    print(i)  
    ```  
    a) `0 1 2`  
    b) `2`  
    c) `3`  
    d) `Error`  
"B"
12. **Which code uses `match-case` correctly?**  
    a)  
    ```python  
    match x:  
        case 1: print("One")  
    ```  
    b)  
    ```python  
    match x:  
        1: print("One")  
    ```  
    c)  
    ```python  
    case x:  
        match 1: print("One")  
    ```  
    d) None  
"A"
13. **What does `print(not (True or False))` output?**  
    a) `True`  
    b) `False`  
    c) `Error`  
    d) `None`  
"B"
14. **Which code snippet is equivalent to:**  
    ```python  
    x = 5 if a > b else 10  
    ```  
    a)  
    ```python  
    if a > b:  
        x = 5  
    else:  
        x = 10  
    ```  
    b)  
    ```python  
    x = (a > b) ? 5 : 10  
    ```  
    c) Both a and b  
    d) None  
"A"
15. **What is the result of:**  
    ```python  
    for i in range(2):  
        for j in range(2):  
            print(i + j)  
    ```
    my solution:  
    i,j=result
    0,0=  0
    0,1=  1
    1,0=  1
    1,1=  2

    a) `0 1 1 2`  
    b) `0 1 2 3`  
    c) `1 2 2 3`  
    d) `0 1 1 1`  
"A"
---

### **Code Correction**

16. **Fix the code:**  
    ```python  
    if x = 5:  
        print("Five")  
    ```  
    a) Change `=` to `==`  
    b) Add `:` after `5`  
    c) Both a and b  
    d) No error  
"A"
17. **What's wrong with:**  
    ```python  
    while True  
        print("Looping")  
    ```  
    a) Missing `:`  
    b) Missing condition  
    c) Infinite loop  
    d) Both a and c  
"D"
18. **Correct the `match-case` statement:**  
    ```python  
    match x:  
        case 1  
            print("One")  
    ```  
    a) Add `:` after `case 1`  
    b) Indent the print statement  
    c) Both a and b  
    d) Use `if` instead  
"A"
---

### **Code Execution**

19. **What does `print([i**2 for i in range(3)])` output?**  
    a) `[0, 1, 4]`  
    b) `[1, 4, 9]`  
    c) `[0, 1, 2]`  
    d) `Error`  
"A"
20. **What is the result of:**  
    ```python  
    x = 0  
    while x < 3:  
        x += 1  
    print(x)  
    ```  
    a) `3`  
    b) `2`  
    c) `0`  
    d) Infinite loop  
"A"
21. **What does `print(any([False, 0, ""]))` output?**  
    a) `True`  
    b) `False`  
    c) `Error`  
    d) `None`  
"B"
---

### **Conceptual Questions**

22. **What is short-circuit evaluation?**  
    a) Skipping unnecessary condition checks  
    b) Breaking loops early  
    c) Optimizing arithmetic operations  
    d) All of the above  
"A"
23. **Which data type is falsy in Python?**  
    a) `0`  
    b) `"False"`  
    c) `[1]`  
    d) `None`  
"D"
24. **What does `pass` do?**  
    a) Terminates the loop  
    b) Acts as a placeholder  
    c) Skips iterations  
    d) Prints output  
"B"
---

### **Advanced Loops**

25. **Which code generates all even numbers between 0-10?**  
    a) `[i for i in range(10) if i%2==0]`  
    b) `[i*2 for i in range(5)]`  
    c) Both a and b  
    d) None  
"C"
26. **What is the output of:**  
    ```python  
    for i in range(3):  
        if i == 1:  
            break  
    else:  
        print("Done")  
    ```  
    a) `Done`  
    b) No output  
    c) `1`  
    d) Error  

27. **Which code flattens a 2D list?**  
    a)  
    ```python  
    matrix = [[1,2], [3,4]]  
    [num for row in matrix for num in row]  
    ```  
    b)  
    ```python  
    [row for row in matrix]  
    ```  
    c) Both  
    d) None  

---

### **Error Identification**

28. **What's wrong with:**  
    ```python  
    for i in 5:  
        print(i)  
    ```  
    a) `5` is not iterable  
    b) Missing `range()`  
    c) Both a and b  
    d) No error  

29. **Which code causes an infinite loop?**  
    a)  
    ```python  
    x = 0  
    while x < 5:  
        x += 1  
    ```  
    b)  
    ```python  
    while True:  
        break  
    ```  
    c)  
    ```python  
    x = 10  
    while x > 0:  
        x += 1  
    ```  
    d) None  

30. **What error occurs here?**  
    ```python  
    if 10 < "5":  
        print("Invalid")  
    ```  
    a) `TypeError`  
    b) `ValueError`  
    c) `SyntaxError`  
    d) No error  

---

### **Code Completion**

31. **Complete the code to print odd numbers:**  
    ```python  
    for i in range(10):  
        if _______:  
            print(i)  
    ```  
    a) `i % 2 != 0`  
    b) `i // 2 == 1`  
    c) `i % 2 == 0`  
    d) `i in [1,3,5,7,9]`  

32. **Fill in the blank to exit the loop when `x` is 5:**  
    ```python  
    x = 0  
    while True:  
        x += 1  
        if x == 5:  
            ______  
    ```  
    a) `break`  
    b) `continue`  
    c) `exit()`  
    d) `pass`  

33. **Complete the match-case for HTTP status codes:**  
    ```python  
    match status:  
        ______:  
            print("Not Found")  
    ```  
    a) `case 404`  
    b) `case "404"`  
    c) `case == 404`  
    d) `case 404:`  

---

### **Tricky Outputs**

34. **What does `print(3 * 'a' in 'banana')` output?**  
    a) `True`  
    b) `False`  
    c) `Error`  
    d) `None`  

35. **What is the result of:**  
    ```python  
    for i in range(2):  
        pass  
    print(i)  
    ```  
    a) `1`  
    b) `2`  
    c) `NameError`  
    d) `0`  

36. **What does `print(1 < 2 < 3)` output?**  
    a) `True`  
    b) `False`  
    c) `Error`  
    d) `None`  

---

### **Advanced Concepts**

37. **Which is a generator expression?**  
    a) `(i for i in range(5))`  
    b) `[i for i in range(5)]`  
    c) `{i for i in range(5)}`  
    d) `i for i in range(5)`  

38. **What does `enumerate()` do?**  
    a) Returns index-value pairs  
    b) Counts elements  
    c) Creates a dictionary  
    d) Skips elements  

39. **Which code uses `zip()` correctly?**  
    a)  
    ```python  
    for a, b in zip([1,2], [3,4]):  
        print(a + b)  
    ```  
    b)  
    ```python  
    for a in zip([1,2], [3,4]):  
        print(a)  
    ```  
    c) Both  
    d) None  

40. **What is the output of:**  
    ```python  
    print(all([True, 1, "a"]))  
    ```  
    a) `True`  
    b) `False`  
    c) `Error`  
    d) `None`  

---

### **Miscellaneous**

41. **Which code reverses a list?**  
    a) `reversed(lst)`  
    b) `lst[::-1]`  
    c) Both  
    d) None  

42. **What does `"Hello".isalpha()` return?**  
    a) `True`  
    b) `False`  
    c) `Error`  
    d) `None`  

43. **Which method removes whitespace?**  
    a) `strip()`  
    b) `trim()`  
    c) `clean()`  
    d) `remove()`  

44. **What is the output of:**  
    ```python  
    x = 10  
    while x > 5:  
        x -= 1  
    print(x)  
    ```  
    a) `5`  
    b) `6`  
    c) `4`  
    d) `10`  

45. **Which code checks for a prime number?**  
    a)  
    ```python  
    def is_prime(n):  
        for i in range(2, n):  
            if n % i == 0:  
                return False  
        return True  
    ```  
    b)  
    ```python  
    def is_prime(n):  
        return all(n % i != 0 for i in range(2, n))  
    ```  
    c) Both  
    d) None  

46. **What does `print(round(4.5))` output?**  
    a) `4`  
    b) `5`  
    c) `4.5`  
    d) `Error`  

47. **Which code converts `"123"` to an integer?**  
    a) `int("123")`  
    b) `float("123").to_int()`  
    c) `str.to_int("123")`  
    d) All  

48. **What is the output of:**  
    ```python  
    print("Hello" * 2)  
    ```  
    a) `HelloHello`  
    b) `Hello2`  
    c) `Error`  
    d) `None`  

49. **Which code uses a walrus operator?**  
    a) `(x := 5)`  
    b) `x = 5`  
    c) `x == 5`  
    d) None  

50. **What does `__init__` do?**  
    a) Initializes class objects  
    b) Terminates programs  
    c) Imports modules  
    d) Handles exceptions  

---

Let me know if you need explanations for any specific question! 😊