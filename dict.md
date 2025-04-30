Here are 50 MCQs covering Python dictionaries, ranging from beginner to advanced levels:

---

### **Beginner Level**

1. **How do you create an empty dictionary?**  
   - A. `{}`  
   - B. `dict()`  
   - C. `[]`  
   - D. Both A and B  
"D"
2. **What is the output of `d = {"a": 1}; print(d["b"])`?**  
   - A. `None`  
   - B. `KeyError`  
   - C. `0`  
   - D. `1`  
"B"
3. **Which method safely returns `None` if a key is missing?**  
   - A. `get()`  
   - B. `keys()`  
   - C. `pop()`  
   - D. `values()`  
"A"
4. **How do you add a key-value pair `"c": 3` to `d = {"a": 1, "b": 2}`?**  
   - A. `d.append("c": 3)`  
   - B. `d["c"] = 3`  
   - C. `d.add("c", 3)`  
   - D. `d.update("c": 3)`  
"B"
5. **What is the output of `d = {1: "a", 1.0: "b"}; print(d[1])`?**  
   - A. `"a"`  
   - B. `"b"`  
   - C. `KeyError`  
   - D. `TypeError`  
"B"
---

### **Intermediate Level**

6. **What does `d = {"a": 1}; d.update({"b": 2})` do?**  
   - A. Replaces `"a"` with `"b"`  
   - B. Adds `"b": 2` to `d`  
   - C. Raises `KeyError`  
   - D. Merges `{"b": 2}` into `d` and returns a new dict  
"B"
7. **Which code creates `{"A": 1, "B": 2}` from `keys = ["a", "b"]`?**  
   - A. `{k.upper(): i+1 for i, k in enumerate(keys)}`  
   - B. `{k: v for k in keys for v in [1, 2]}`  
   - C. `dict(zip(keys, [1, 2]))`  
   - D. Both A and C  
"A"
8. **What is the output of `d = {"x": {"y": 5}}; print(d["x"]["y"])`?**  
   - A. `5`  
   - B. `{"y": 5}`  
   - C. `KeyError`  
   - D. `TypeError`  
"A"
9. **What does `d.pop("key", None)` do?**  
   - A. Removes `"key"` and returns its value, or `None` if missing  
   - B. Removes the last item  
   - C. Deletes the entire dictionary  
   - D. Raises `KeyError`  
"A"
10. **How do you check if `"name"` is a key in `d`?**  
    - A. `"name" in d`  
    - B. `d.exists("name")`  
    - C. `d.has_key("name")`  
    - D. `d.contains("name")`  

---

### **Advanced Level**

11. **Which key type is invalid?**  
    - A. `(1, 2)`  
    - B. `frozenset([1, 2])`  
    - C. `{"a": 1}`  
    - D. `100`  

12. **What is the output of `print({True: "a", 1: "b"})`?**  
    - A. `{True: "a", 1: "b"}`  
    - B. `{True: "b"}`  
    - C. `TypeError`  
    - D. `{1: "b"}`  

13. **Which code creates a deep copy of a nested dictionary?**  
    - A. `copy.deepcopy(d)`  
    - B. `d.copy()`  
    - C. `dict(d)`  
    - D. `d[:]`  

14. **What is the result of `d = {}; d[[1, 2]] = 5`?**  
    - A. `{[1,2]: 5}`  
    - B. `TypeError`  
    - C. `KeyError`  
    - D. `{1: 5, 2: 5}`  

15. **Which code converts `["a", "b"]` to `{"a": 0, "b": 1}`?**  
    - A. `{k: v for v, k in enumerate(lst)}`  
    - B. `{k: i for i, k in enumerate(lst)}`  
    - C. `dict(enumerate(lst))`  
    - D. Both B and C  

---

### **Code Correction**

16. **Which line causes an error?**  
    ```python
    d = {[1]: "a"}
    print(d[[1]])
    ```  
    - A. Line 1  
    - B. Line 2  
    - C. Both  
    - D. No error  

17. **What is wrong with `d = {"a": 1}; d.get("b", 0) = 2`?**  
    - A. `get()` cannot assign values  
    - B. Missing colon  
    - C. Invalid default value  
    - D. No error  
"A"
18. **Which code removes all items from `d`?**  
    - A. `d = {}`  
    - B. `d.clear()`  
    - C. `del d`  
    - D. Both A and B  
"D"
19. **What is the output of `d = {1: "a"}; d[2] += "b"`?**  
    - A. `{1: "a", 2: "b"}`  
    - B. `KeyError`  
    - C. `TypeError`  
    - D. `{1: "ab"}`  
"B"
20. **Which code reverses keys and values?**  
    - A. `{v: k for k, v in d.items()}`  
    - B. `dict(zip(d.values(), d.keys()))`  
    - C. `d.items()[::-1]`  
    - D. Both A and B  
"D"
---

### **Conceptual Questions**

21. **Why are lists invalid as dictionary keys?**  
    - A. Lists are mutable  
    - B. Lists are unhashable  
    - C. Lists are ordered  
    - D. Both A and B  
"D"
22. **What is the output of `d = dict.fromkeys("abc", 0)`?**  
    - A. `{"a": 0, "b": 0, "c": 0}`  
    - B. `{"abc": 0}`  
    - C. `["a", "b", "c"]`  
    - D. `TypeError`  
"A"
23. **What does `d.setdefault("key", []).append(1)` do?**  
    - A. Adds `1` to `d["key"]` if it exists  
    - B. Creates `"key": [1]` if missing  
    - C. Both A and B  
    - D. Raises `KeyError`  

24. **Which method returns key-value pairs?**  
    - A. `keys()`  
    - B. `values()`  
    - C. `items()`  
    - D. `pairs()`  
"C"
25. **What is the result of `len({"a": [1, 2, 3]})`?**  
    - A. `1`  
    - B. `3`  
    - C. `4`  
    - D. `TypeError`  
"A"
---

### **Advanced Code Execution**

26. **What is the output of:**  
    ```python
    d = {i: i**2 for i in range(3)}
    print(d[2])
    ```  
    - A. `4`  
    - B. `9`  
    - C. `KeyError`  
    - D. `{2: 4}`  
"A"
27. **What does `print({k: v for k, v in [("a", 1), ("b", 2)]})` output?**  
    - A. `{"a": 1, "b": 2}`  
    - B. `["a", "b"]`  
    - C. `TypeError`  
    - D. `[("a", 1), ("b", 2)]`  
"A"
28. **Which code merges `d1` and `d2`, prioritizing `d2`?**  
    - A. `{**d1, **d2}`  
    - B. `d1.update(d2)`  
    - C. `dict(d1, **d2)`  
    - D. All of the above  
"D"
29. **What is the result of `d = {"a": 1}; del d["a"]; print(d["a"])`?**  
    - A. `None`  
    - B. `KeyError`  
    - C. `1`  
    - D. `0`  
"B"
30. **What does `print(dict(a=1, b=2))` output?**  
    - A. `{"a": 1, "b": 2}`  
    - B. `{"a": "1", "b": "2"}`  
    - C. `SyntaxError`  
    - D. `["a", "b"]`  
"A"
---

### **Error Identification**

31. **Which code raises an error?**  
    - A. `d = {(1,): "a"}`  
    - B. `d = {[1]: "a"}`  
    - C. `d = {1: "a"}`  
    - D. All are valid  
"B"
32. **What happens when `d.pop()` is called?**  
    - A. Removes the last item  
    - B. `TypeError`  
    - C. Removes a random item  
    - D. `KeyError`  
"B"
33. **Which code creates a shallow copy?**  
    - A. `d.copy()`  
    - B. `dict(d)`  
    - C. `d[:]`  
    - D. Both A and B  
"D"
34. **What is the output of `d = {"a": 1}; d.setdefault("a", 2)`?**  
    - A. `1`  
    - B. `2`  
    - C. `{"a": 2}`  
    - D. `KeyError`  

35. **Which code deletes all keys starting with "a"?**  
    - A. `[d.pop(k) for k in d if k.startswith("a")]`  
    - B. `for k in d: if k[0] == "a": del d[k]`  
    - C. `d = {k: v for k, v in d.items() if not k.startswith("a")}`  
    - D. All of the above  
"D"
---

### **Code Completion**

36. **Complete the code to invert keys/values:**  
    ```python
    inverted = __________
    ```  
    - A. `{v: k for k, v in d.items()}`  
    - B. `dict(zip(d.values(), d.keys()))`  
    - C. `{d[k]: k for k in d}`  
    - D. All of the above  
"D"
37. **Complete the code to count word frequencies:**  
    ```python
    words = ["a", "b", "a"]
    freq = __________
    ```  
    - A. `{w: words.count(w) for w in words}`  
    - B. `Counter(words)`  
    - C. `defaultdict(int); for w in words: freq[w] += 1`  
    - D. All of the above  
"A"
38. **Complete the code to flatten `{"a": {"b": 1}}` to `{"a.b": 1}`:**  
    ```python
    def flatten(d):
        result = {}
        for k, v in d.items():
            if isinstance(v, dict):
                for inner_k, inner_v in flatten(v).items():
                    result[f"{k}.{inner_k}"] = inner_v
            else:
                __________
        return result
    ```  
    - A. `result[k] = v`  
    - B. `result.update({k: v})`  
    - C. `result[k] += v`  
    - D. `result.append((k, v))`  

39. **Complete the code to create `{"a": 0, "b": 1}`:**  
    ```python
    keys = ["a", "b"]
    d = __________
    ```  
    - A. `{k: i for i, k in enumerate(keys)}`  
    - B. `dict(enumerate(keys))`  
    - C. `dict(zip(keys, range(2)))`  
    - D. Both A and C  
"D"
40. **Complete the code to sort a dictionary by values:**  
    ```python
    sorted_d = __________
    ```  
    
    - A. `dict(sorted(d.items(), key=lambda x: x[1]))`  
    - B. `{k: v for k, v in sorted(d.values())}`  
    - C. `OrderedDict(sorted(d.items()))`  
    - D. Both A and C  
"A"
---

### **Advanced Concepts**

41. **What is the output of:**  
    ```python
    d = {}
    d[1] = "a"
    d[1.0] = "b"
    print(d)
    ```  
    - A. `{1: "a", 1.0: "b"}`  
    - B. `{1: "b"}`  
    - C. `TypeError`  
    - D. `{1.0: "b"}`  
"B"
42. **Which code creates a dictionary with default value 0?**  
    - A. `defaultdict(int)`  
    - B. `dict.fromkeys(keys, 0)`  
    - C. `{k: 0 for k in keys}`  
    - D. All of the above  
"D"
43. **What is the result of `d = {True: "a"}; print(d[1])`?**  
    - A. `"a"`  
    - B. `KeyError`  
    - C. `1`  
    - D. `True`  
"A"
44. **Which code uses a tuple as a key?**  
    - A. `d[(1, 2)] = "a"`  
    - B. `d[[1, 2]] = "a"`  
    - C. `d[{1, 2}] = "a"`  
    - D. All of the above  
"A"
45. **What does `d = {k: v for k, v in []}` create?**  
    - A. `{}`  
    - B. `[]`  
    - C. `KeyError`  
    - D. `SyntaxError`  
"A"
---

### **Tricky Scenarios**

46. **What is the output of:**  
    ```python
    d = {"a": 1, "b": 2}
    d.update({"b": 3, "c": 4})
    print(d["b"] + d.get("c", 0))
    ```  
    - A. `7`  
    - B. `5`  
    - C. `3`  
    - D. `KeyError`  
"A"
47. **What does `print({**{"a": 1}, **{"b": 2}})` output?**  
    - A. `{"a": 1, "b": 2}`  
    - B. `{"a": 1}`  
    - C. `TypeError`  
    - D. `[("a", 1), ("b", 2)]`  
"A"
48. **What is the result of `dict([(1, 2), (3, 4)])`?**  
    - A. `{1: 2, 3: 4}`  
    - B. `[1, 2, 3, 4]`  
    - C. `TypeError`  
    - D. `{1, 3}`  
"A"
49. **Which code converts `["a=1", "b=2"]` to a dictionary?**  
    - A. `dict(pair.split("=") for pair in lst)`  
    - B. `{k: v for k, v in (s.split("=") for s in lst)}`  
    - C. `eval(f"dict({','.join(lst)})")`  
    - D. All of the above  
"D"
50. **What is the output of `d = {0: "a"}; print(d[False])`?**  
    - A. `"a"`  
    - B. `KeyError`  
    - C. `0`  
    - D. `False`  
"A"
--- 

These questions cover syntax, methods, immutability, comprehensions, nesting, and advanced dictionary operations.