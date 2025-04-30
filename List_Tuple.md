Here are 50 MCQs covering Python lists and tuples, ranging from beginner to advanced levels:

### **Beginner Level**

1. **What is the output of the following code?**
   ```python
   fruits = ['apple', 'banana', 'cherry']
   print(fruits[3])
   ```
   - A. `cherry`  
   - B. `banana`  
   - C. `IndexError`  
   - D. `None`  

2. **Which code correctly creates a tuple with one element?**  
   - A. `(1)`  
   - B. `(1,)`  
   - C. `[1]`  
   - D. `1,`  

3. **What does `list.pop()` do by default?**  
   - A. Removes the first element  
   - B. Removes the last element  
   - C. Removes a random element  
   - D. Raises an error  

4. **Which is mutable?**  
   - A. List  
   - B. Tuple  
   - C. Both  
   - D. Neither  

5. **What is the result of `[1, 2, 3] + [4, 5]`?**  
   - A. `[1, 2, 3, 4, 5]`  
   - B. `[5, 7]`  
   - C. `[[1, 2, 3], [4, 5]]`  
   - D. `TypeError`  

---


### **Intermediate Level**

6. **What is the output of `print([0, 1, 2, 3][1:3])`?**  
   - A. `[1, 2]`  
   - B. `[0, 1]`  
   - C. `[1, 2, 3]`  
   - D. `[0, 1, 2]`  

7. **Which list comprehension creates `[0, 1, 4, 9]`?**  
   - A. `[x**2 for x in range(4)]`  
   - B. `[x^2 for x in range(4)]`  
   - C. `[x*2 for x in range(4)]`  
   - D. `[x*x for x in 4]`  

8. **What is the result of `(1, 2, 3)[1]`?**  
   - A. `1`  
   - B. `2`  
   - C. `3`  
   - D. `IndexError`  

9. **Which method adds multiple elements to a list?**  
   - A. `.append()`  
   - B. `.insert()`  
   - C. `.extend()`  
   - D. `.add()`  

10. **What does `[2, 1, 3].sort()` return?**  
    - A. `[1, 2, 3]`  
    - B. `None`  
    - C. `[3, 2, 1]`  
    - D. `TypeError`  

---

### **Advanced Level**

11. **Which is more memory-efficient for fixed data?**  
    - A. List  
    - B. Tuple  
    - C. Both are equal  
    - D. Depends on Python version  

12. **What happens when you run `tup = (1, [2, 3]); tup[1][0] = 4`?**  
    - A. `tup` becomes `(1, [4, 3])`  
    - B. `TypeError`  
    - C. The list inside the tuple is modified  
    - D. Both A and C  

13. **Which code converts a list `[[1, 2], [3, 4]]` to `[1, 2, 3, 4]`?**  
    - A. `[x for sublist in lst for x in sublist]`  
    - B. `[sublist for x in lst]`  
    - C. `[lst.flatten()]`  
    - D. `[x in lst]`  

14. **What is the output of `print([i for i in range(5) if i % 2 == 0])`?**  
    - A. `[0, 2, 4]`  
    - B. `[1, 3]`  
    - C. `[0, 1, 2, 3, 4]`  
    - D. `SyntaxError`  

15. **Which is a valid use of a tuple as a dictionary key?**  
    - A. `{(1, 2): "value"}`  
    - B. `{[1, 2]: "value"}`  
    - C. `{{1, 2}: "value"}`  
    - D. All of the above  
"Ä"
---

### **Code Correction**

16. **Which line causes an error?**  
    ```python
    tup = (1, 2, 3)
    tup[1] = 4
    print(tup)
    ```
    - A. Line 1  
    - B. Line 2  
    - C. Line 3  
    - D. No error  

17. **What is wrong with `list = [1, 2]; list.append(3, 4)`?**  
    - A. `append()` takes one argument  
    - B. Missing comma  
    - C. `list` is a reserved keyword  
    - D. No error  

18. **Which code removes all elements from a list?**  
    - A. `list.clear()`  
    - B. `del list[:]`  
    - C. `list = []`  
    - D. All of the above  

19. **What is the output of `print((1, 2) + (3))`?**  
    - A. `(1, 2, 3)`  
    - B. `TypeError`  
    - C. `(4, 5)`  
    - D. `SyntaxError`  

20. **Which code reverses a list in-place?**  
    - A. `list[::-1]`  
    - B. `list.reverse()`  
    - C. `reversed(list)`  
    - D. `list.sort(reverse=True)`  

---


### **Conceptual Questions**

21. **Why are tuples hashable but lists not?**  
    - A. Tuples are immutable  
    - B. Lists are dynamic  
    - C. Tuples use less memory  
    - D. Lists can't contain other lists  

22. **What is the result of `a = [1, 2]; b = a; b[0] = 0; print(a)`?**  
    - A. `[0, 2]`  
    - B. `[1, 2]`  
    - C. `[0, 1, 2]`  
    - D. `TypeError`  

23. **What does `sorted((3, 1, 2))` return?**  
    - A. `[1, 2, 3]`  
    - B. `(1, 2, 3)`  
    - C. `TypeError`  
    - D. `[3, 1, 2]`  

24. **Which method checks if an element exists in a list?**  
    - A. `.index()`  
    - B. `in` keyword  
    - C. `.find()`  
    - D. `.contains()`  

25. **What is the result of `len((1, (2, 3)))`?**  
    - A. `2`  
    - B. `3`  
    - C. `1`  
    - D. `SyntaxError`  

---

### **Advanced Code Execution**

26. **What is the output of:**
    ```python
    a, b, *c = [1, 2, 3, 4]
    print(c)
    ```
    - A. `[3, 4]`  
    - B. `[2, 3, 4]`  
    - C. `SyntaxError`  
    - D. `4`  

27. **What does `print([i % 2 == 0 for i in range(3)])` output?**  
    - A. `[True, False, True]`  
    - B. `[0, 1, 0]`  
    - C. `[False, True, False]`  
    - D. `[1, 0, 1]`  

28. **Which code creates a list of tuples from `[1, 2]` and `[3, 4]`?**  
    - A. `zip([1, 2], [3, 4])`  
    - B. `list(zip([1, 2], [3, 4]))`  
    - C. `tuple(zip([1, 2], [3, 4]))`  
    - D. `map(zip, [1, 2], [3, 4])`  

29. **What is the result of `[x for x in 'hello' if x not in 'aeiou']`?**  
    - A. `['h', 'l', 'l']`  
    - B. `['h', 'e', 'l', 'l', 'o']`  
    - C. `['e', 'o']`  
    - D. `['h', 'll']`  

30. **What does `print(tuple(range(3)))` output?**  
    - A. `(0, 1, 2)`  
    - B. `[0, 1, 2]`  
    - C. `range(0, 3)`  
    - D. `TypeError`  

---

### **Error Identification**

31. **Which code raises an error?**  
    - A. `[1, 2][0] = 3`  
    - B. `(1, 2)[0] = 3`  
    - C. `[[1, 2]][0][0] = 3`  
    - D. All are valid  

32. **What happens when `list.remove(5)` is called on `[1, 2, 3]`?**  
    - A. `ValueError`  
    - B. `None`  
    - C. Removes `1`  
    - D. `IndexError`  

33. **Which code creates a shallow copy of a list?**  
    - A. `new = old.copy()`  
    - B. `new = old[:]`  
    - C. `new = list(old)`  
    - D. All of the above  

34. **What is the result of `print([1, 'a'].sort())`?**  
    - A. `[1, 'a']`  
    - B. `None`  
    - C. `TypeError`  
    - D. `['a', 1]`  
"C"
35. **Which code deletes the second element of a list?**  
    - A. `del list[1]`  
    - B. `list.remove(1)`  
    - C. `list.pop(2)`  
    - D. `list.delete(1)`  
"A"
---

### **Code Completion**

36. **Complete the code to reverse a list:**  
    ```python
    lst = [1, 2, 3]
    reversed_lst = __________  # Fill in
    ```
    - A. `lst[::-1]`  
    - B. `lst.reverse()`  
    - C. `reversed(lst)`  
    - D. `sorted(lst, reverse=True)`  

37. **Complete the code to count occurrences of `2`:**  
    ```python
    lst = [1, 2, 2, 3]
    count = __________
    ```
    - A. `lst.count(2)`  
    - B. `len(lst == 2)`  
    - C. `sum(x == 2 for x in lst)`  
    - D. Both A and C  
"D"
38. **Complete the code to create `(1, 3, 5)`:**  
    ```python
    tup = tuple(__________)
    ```
    - A. `[x for x in range(1, 6) if x % 2 == 1]`  
    - B. `(x for x in range(6) if x % 2 != 0)`  
    - C. `range(1, 6, 2)`  
    - D. All of the above  
"D"
39. **Complete the code to unpack `a=1, b=2`:**  
    ```python
    tup = (1, 2)
    a, b = __________
    ```
    - A. `tup`  
    - B. `*tup`  
    - C. `list(tup)`  
    - D. `tup.values()`  
"B"
40. **Complete the code to get `[('a', 0), ('b', 1)]`:**  
    ```python
    lst = ['a', 'b']
    result = __________
    ```
    - A. `list(enumerate(lst))`  
    - B. `[(i, c) for i, c in enumerate(lst)]`  
    - C. `zip(lst, range(len(lst)))`  
    - D. All of the above  

---

### **Advanced Concepts**

41. **What does `a = ([1, 2],); a[0] += [3]` do?**  
    - A. Modifies the tuple  
    - B. Raises `TypeError`  
    - C. Modifies the list inside the tuple  
    - D. Both B and C  
"B"
42. **Which creates a deep copy of a nested list?**  
    - A. `copy.deepcopy()`  
    - B. `list.copy()`  
    - C. `nested_list[:]`  
    - D. `list(nested_list)`  
"A"
43. **What is the output of `print((1,) is (1,))`?**  
    - A. `True`  
    - B. `False`  
    - C. `SyntaxError`  
    - D. `TypeError`  
"A"
44. **Which code swaps two elements in a list?**  
    - A. `lst[0], lst[1] = lst[1], lst[0]`  
    - B. `lst.swap(0, 1)`  
    - C. `swap(lst[0], lst[1])`  
    - D. `lst = lst[1] + lst[0]`  
"A"
45. **What is the result of `sum([(1, 2), (3, 4)], ())`?**  
    - A. `(1, 2, 3, 4)`  
    - B. `[1, 2, 3, 4]`  
    - C. `TypeError`  
    - D. `10`  
"A"
---

### **Tricky Scenarios**

46. **What is the output of:**
    ```python
    lst = [1, 2]
    lst.extend([3, 4])
    print(lst)
    ```
    - A. `[1, 2, 3, 4]`  
    - B. `[1, 2, [3, 4]]`  
    - C. `TypeError`  
    - D. `None`  
"A"
47. **What does `print([1, 2] * 2)` output?**  
    - A. `[1, 2, 1, 2]`  
    - B. `[2, 4]`  
    - C. `[[1, 2], [1, 2]]`  
    - D. `TypeError`  
"A"
48. **What is the result of `len([[[1, 2]]])`?**  
    - A. `1`  
    - B. `2`  
    - C. `3`  
    - D. `SyntaxError`  
"A"
49. **Which code checks if two lists have the same elements in any order?**  
    - A. `sorted(list1) == sorted(list2)`  
    - B. `list1 == list2`  
    - C. `set(list1) == set(list2)`  
    - D. Both A and C  
"A"
50. **What is the result of `x, y = (1)`?**  
    - A. `x=1, y=undefined`  
    - B. `ValueError`  
    - C. `x=1, y=None`  
    - D. `SyntaxError`  

--- 

These questions cover a wide range of topics, including syntax, methods, immutability, slicing, list comprehensions, and error handling.