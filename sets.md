Here are 50 MCQs covering Python sets from beginner to advanced levels:

---

### **Beginner Level**

1. **What is the primary characteristic of a set in Python?**  
A) Ordered collection  
B) Allows duplicate elements  
C) Mutable and indexed  
D) Unordered and unique elements  
"D"
2. **Which code creates an empty set?**  
A) `{}`  
B) `set()`  
C) `[]`  
D) `()`  
"B"
3. **What is the output of `print(len({1, 2, 2, 3}))`?**  
A) 4  
B) 3  
C) Error  
D) 2  
"3"
4. **Which line causes an error?**  
```python
A) s = {1, 2, 3}  
B) s.add([4])  
C) s.remove(2)  
D) s.discard(5)  
```
"B"
5. **What does `{1, 2, 3} | {3, 4}` return?**  
A) `{1, 2, 3, 4}`  
B) `{3}`  
C) `{1, 2}`  
D) `{4}`  
"A"
6. **Which method raises an error if an element is not found?**  
A) `discard()`  
B) `pop()`  
C) `remove()`  
D) `clear()`  
"C"
7. **What is the output of `print(3 in {1, 2, 3})`?**  
A) `True`  
B) `False`  
C) `Error`  
D) `None`  
"A"
8. **Which is a valid set element?**  
A) `[1, 2]`  
B) `{"key": "value"}`  
C) `(1, 2)`  
D) `{1, 2}`  
"D"
9. **What does `set([1, 2, 3, 2])` return?**  
A) `{1, 2, 3}`  
B) `[1, 2, 3]`  
C) `Error`  
D) `{1, 2, 2, 3}`  
"A"
10. **Which code adds 4 to the set `s = {1, 2, 3}`?**  
A) `s.append(4)`  
B) `s += {4}`  
C) `s.add(4)`  
D) `s.update(4)`  
"C"
---

### **Intermediate Level**

11. **What is the output of `{1, 2} ^ {2, 3}`?**  
A) `{1, 3}`  
B) `{2}`  
C) `{1, 2, 3}`  
D) `∅`  
"A"
12. **Which method updates a set with the intersection of itself and another set?**  
A) `intersection()`  
B) `union()`  
C) `intersection_update()`  
D) `update()`  
"C"
13. **What is the result of `frozenset([1, 2, 3])`?**  
A) Immutable set  
B) Mutable set  
C) List  
D) Error  
"A"
14. **Which code checks if `s1` is a subset of `s2`?**  
A) `s1 <= s2`  
B) `s1 >= s2`  
C) `s1.isdisjoint(s2)`  
D) `s1.difference(s2)`  
"A"
15. **What does `s = {x for x in [1, 2, 1, 3]}` create?**  
A) `{1, 2, 3}`  
B) `[1, 2, 3]`  
C) `{1, 2, 1, 3}`  
D) `Error`  
"A"
16. **Which code removes all elements from `s = {1, 2, 3}`?**  
A) `s.clear()`  
B) `del s`  
C) `s.remove_all()`  
D) `s.empty()`  
"A"
17. **What is the output of `print({1, 2}.issuperset({1}))`?**  
A) `True`  
B) `False`  
C) `Error`  
D) `None`  
"A"
18. **Which code creates a set with elements `1`, `2`, and `3`?**  
A) `set(1, 2, 3)`  
B) `set([1, 2, 3])`  
C) `{1; 2; 3}`  
D) `set( (1) )`  
"B"
19. **What does `s.update([4, 5])` do for `s = {1, 2}`?**  
A) Adds `4` and `5` to `s`  
B) Replaces `s` with `[4, 5]`  
C) Raises an error  
D) Creates a new set  
"A"
20. **Which code returns `True` if two sets have no common elements?**  
A) `s1.isdisjoint(s2)`  
B) `s1.union(s2) == set()`  
C) `s1.difference(s2) == s1`  
D) `s1.intersection(s2)`  
"A"
---

### **Advanced Level**

21. **Why can’t a set contain a list?**  
A) Lists are mutable  
B) Lists are unhashable  
C) Sets only accept tuples  
D) Lists are ordered  
"B"
22. **What is the time complexity of checking membership in a set?**  
A) O(1)  
B) O(n)  
C) O(log n)  
D) O(n²)  
"A"
23. **Which code uses a frozenset as a dictionary key?**  
A) `{frozenset({1, 2}): "value"}`  
B) `{{1, 2}: "value"}`  
C) `{(1, 2): "value"}`  
D) `{[1, 2]: "value"}`  
"A"
24. **What is the output of:**  
```python
s = {1, 2, 3}
s.add(s)
```  
A) `{1, 2, 3, {...}}`  
B) `TypeError`  
C) `RecursionError`  
D) `{1, 2, 3}`  
"D"
25. **Which code creates a set of frozensets?**  
A) `{frozenset({1}), frozenset({2})}`  
B) `{{1}, {2}}`  
C) `set([set([1]), set([2])])`  
D) `{[1], [2]}`  
"A"
26. **What does `gc.collect()` do?**  
A) Manually triggers garbage collection  
B) Counts set elements  
C) Deletes all sets  
D) Disables memory management  
"A"
27. **How does Python handle hash collisions in sets?**  
A) Uses linked lists  
B) Resizes the hash table  
C) Ignores collisions  
D) Raises an error  
"B"
28. **Which code correctly removes duplicates from a list?**  
A) `list(set([1, 2, 2, 3]))`  
B) `set(list([1, 2, 2, 3]))`  
C) `[x for x in set([1, 2, 2, 3])]`  
D) `sorted(set([1, 2, 2, 3]))`  
"B"
29. **What is the result of:**  
```python
s = {1, 2, 3}
s.difference_update({2}, {3})
```  
A) `{1}`  
B) `{2, 3}`  
C) `Error`  
D) `{1, 2, 3}`  
"A"
30. **Which code creates a nested set?**  
A) `{{1, 2}, {3}}`  
B) `{frozenset({1, 2}), frozenset({3})}`  
C) `set([set([1]), set([2])])`  
D) `{[1, 2], [3]}`  
"C"
---

### **Expert Level**

31. **What is the output of:**  
```python
a = {1, 2}
b = a
a.add(3)
print(b)
```  
A) `{1, 2}`  
B) `{1, 2, 3}`  
C) `Error`  
D) `None`  
"B"
32. **Which method has O(n) time complexity for sets?**  
A) `union()`  
B) `add()`  
C) `pop()`  
D) `issubset()`  
"A"
33. **What is the result of:**  
```python
s = set()
s.add(s)
```  
A) `{set()}`  
B) `TypeError`  
C) `RecursionError`  
D) `{{...}}`  
"B"
34. **Which code uses a weak reference to a set?**  
A) `import weakref; weakref.ref(set())`  
B) `weakref.WeakSet()`  
C) `set.ref()`  
D) `weakref.proxy(set())`  
"A"
35. **What is the output of:**  
```python
s1 = {1, 2, 3}
s2 = s1.copy()
s1.add(4)
print(s2)
```  
A) `{1, 2, 3}`  
B) `{1, 2, 3, 4}`  
C) `Error`  
D) `None`  
"B"
---

### **Code Correction/Completion**

36. **Fix the error:**  
```python
s = {[1, 2], 3}
```  
A) Use `tuple([1, 2])`  
B) Replace `[1, 2]` with `1`  
C) Use `frozenset([1, 2])`  
D) Remove `3`  
"A, B, C"
37. **Complete the code to create a set of even numbers from a list:**  
```python
numbers = [1, 2, 3, 4]
evens = ___  
```  
A) `{x for x in numbers if x % 2 == 0}`  
B) `set(filter(lambda x: x%2==0, numbers))`  
C) `set(evens for x in numbers)`  
D) Both A and B  
"D"
38. **Fix the code:**  
```python
s = {1, 2, 3}
s[0] = 4
```  
A) Use `s.add(4)`  
B) Replace with `s.update([4])`  
C) Use `s.remove(0)`  
D) Sets are immutable  
"A, B"
39. **Complete the code to find common elements in two sets:**  
```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
common = ___  
```  
A) `s1 & s2`  
B) `s1.intersection(s2)`  
C) `s1.union(s2)`  
D) Both A and B  
"D"
40. **What is wrong with:**  
```python
s = {{1: 'a'}, 'b'}
```  
A) Dict cannot be a set element  
B) Syntax error  
C) Use `frozenset({1: 'a'})`  
D) No issue  
"A"
---

### **Conceptual Questions**

41. **Which is true about `frozenset`?**  
A) Mutable  
B) Unhashable  
C) Can be a dictionary key  
D) Allows `add()`  
"C"
42. **What ensures a set’s uniqueness?**  
A) Hashing  
B) Indexing  
C) Ordering  
D) Mutability  
"A"
43. **Which is faster for membership checks: list or set?**  
A) List  
B) Set  
C) Same speed  
D) Depends on size  
"B"
44. **What is a hash table?**  
A) Data structure for key-value pairs  
B) A sorted list  
C) A type of set  
D) A cryptographic function  
"A"
45. **Why might set order change after rehashing?**  
A) Elements are reindexed  
B) Hash collisions  
C) Garbage collection  
D) Immutable elements  
"B"
---

### **Code Execution**

46. **What is the output of:**  
```python
s = {1, 2, 3}
s.update([4, (5,)])
print(s)
```  
A) `{1, 2, 3, 4, 5}`  
B) `{1, 2, 3, 4, (5,)}`  
C) `Error`  
D) `{1, 2, 3, 4}`  
"B"
47. **What does `print(set('hello'))` output?**  
A) `{'h', 'e', 'l', 'l', 'o'}`  
B) `{'h', 'e', 'l', 'o'}`  
C) `{'hello'}`  
D) `Error`  
"B"
48. **What is the result of:**  
```python
s = {1, 2}.symmetric_difference_update({2, 3})
print(s)
```  
A) `{1, 3}`  
B) `None`  
C) `{1, 2, 3}`  
D) `Error`  
"C"
49. **What is the output of:**  
```python
s = {1, 2}
s |= {3}
print(s)
```  
A) `{1, 2, 3}`  
B) `{3}`  
C) `Error`  
D) `None`  
"A"
50. **What does `print(frozenset({1, 2}) == set({1, 2}))` return?**  
A) `True`  
B) `False`  
C) `Error`  
D) `None`  
"A"
--- 

These questions cover a range of topics from basic syntax to advanced concepts like hashing and garbage collection. Let me know if you need explanations for any specific question!