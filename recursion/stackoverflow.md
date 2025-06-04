The **default recursion limit** in Python refers to the maximum depth of the call stack, i.e., the maximum number of recursive function calls that Python allows before raising a `RecursionError`. This limit is typically set to **1000** in most Python implementations (e.g., CPython), though it can vary slightly depending on the system or Python version.

### What Does This Mean?
- **Call Stack**: Each time a function calls itself recursively, Python adds a new frame to the **call stack** to keep track of the function's state (variables, return address, etc.). The recursion limit caps how many such frames can be stacked.
- **Purpose**: The limit prevents infinite recursion or excessively deep recursion from consuming too much memory, which could crash the program or system.
- **Default Value (1000)**: By default, Python allows up to 1000 nested recursive calls. If a recursive function exceeds this depth, Python raises a `RecursionError: maximum recursion depth exceeded`.

### Example of Hitting the Recursion Limit
```python
def infinite_recursion(n):
    return infinite_recursion(n + 1)

# This will cause a RecursionError after ~1000 calls
infinite_recursion(1)
```

**Output**:
```
RecursionError: maximum recursion depth exceeded
```

### Checking and Modifying the Recursion Limit
You can check or modify the recursion limit using the `sys` module:
```python
import sys

# Check the current recursion limit
print(sys.getrecursionlimit())  # Output: 1000 (typically)

# Set a new recursion limit
sys.setrecursionlimit(2000)  # Increase to 2000
print(sys.getrecursionlimit())  # Output: 2000
```

### Implications
- **Why It Exists**: The limit protects against stack overflow, as each recursive call consumes memory on the call stack. Without a limit, infinite recursion could crash the program.
- **Increasing the Limit**: You can increase the limit for deeper recursion, but this should be done cautiously. Setting it too high can lead to a stack overflow crash, depending on system memory.
- **Practical Considerations**: For very deep recursion, consider:
  - Using **iteration** instead of recursion.
  - Optimizing with **tail recursion** or **memoization** (though Python doesn’t optimize tail recursion).
  - Breaking the problem into smaller parts to reduce recursion depth.

### Example with a Deep Recursive Function
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# May fail for very large n (e.g., n > 1000)
try:
    print(factorial(1000))  # Likely fine
    print(factorial(2000))  # May exceed default limit
except RecursionError:
    print("RecursionError: maximum recursion depth exceeded")
```

### When Does It Matter?
- **Deep Recursion**: Problems like recursive tree traversals, graph algorithms, or mathematical computations (e.g., Fibonacci) with large inputs can hit the limit.
- **Infinite Recursion**: Forgetting a base case or incorrect logic can cause infinite recursion, triggering the error quickly.

### Best Practices
1. **Ensure a Base Case**: Always define a proper base case to stop recursion.
2. **Optimize Recursion**: Use memoization or iteration for efficiency (e.g., Fibonacci with memoization).
3. **Increase Limit Cautiously**: If you must increase the limit, test thoroughly to avoid crashes.
4. **Consider Iteration**: For large inputs, iterative solutions are often more memory-efficient.

If you need further clarification or examples (e.g., optimizing a specific recursive function), let me know!