

# Python Recursion

Recursion is a powerful programming technique where a function calls itself to solve a problem by breaking it down into smaller, manageable subproblems. In Python, recursion is widely used for tasks like traversing data structures, solving mathematical problems, and implementing algorithms. This material will guide you through the fundamentals, practical examples, and advanced considerations of recursion in Python.

---

## Table of Contents
1. **What is Recursion?**
2. **How Recursion Works in Python**
3. **Base Case and Recursive Case**
4. **Simple Examples of Recursion**
   - Factorial
   - Fibonacci Sequence
   - Sum of a List
5. **Advantages and Disadvantages of Recursion**
6. **Common Pitfalls and How to Avoid Them**
   - Stack Overflow
   - Inefficient Recursion
7. **Tail Recursion and Optimization**
8. **Advanced Examples**
   - Binary Tree Traversal
   - Tower of Hanoi
9. **Memoization for Optimizing Recursive Functions**
10. **When to Use Recursion vs. Iteration**
11. **Practice Problems**
12. **Additional Resources**

---

## 1. What is Recursion?

Recursion is a process where a function calls itself as a subroutine to solve a problem. Each recursive call works on a smaller instance of the problem until it reaches a **base case**, which is a condition that stops the recursion.

### Key Components of Recursion:
- **Base Case**: The condition under which the recursive function stops calling itself.
- **Recursive Case**: The part of the function where it calls itself with a modified input, moving closer to the base case.

### Example Analogy:
Think of recursion like opening a set of Russian nesting dolls. You open one doll (function call), find a smaller doll inside (recursive call), and continue until you reach the smallest doll (base case).

---

## 2. How Recursion Works in Python

In Python, a recursive function is defined like any other function, but it includes a call to itself within its body. Python maintains a **call stack** to keep track of recursive calls. Each recursive call adds a new frame to the stack, and when the base case is reached, the stack unwinds as the function returns values.

### General Structure of a Recursive Function:
```python
def recursive_function(input):
    # Base case: condition to stop recursion
    if base_condition:
        return base_value
    # Recursive case: function calls itself with modified input
    else:
        return recursive_function(modified_input)
```

### Call Stack Example:
For a function calculating factorial (e.g., `factorial(4)`), the call stack works as follows:
1. `factorial(4)` calls `factorial(3)`.
2. `factorial(3)` calls `factorial(2)`.
3. `factorial(2)` calls `factorial(1)`.
4. `factorial(1)` hits the base case and returns 1.
5. The stack unwinds, computing: `1 * 2 = 2`, `2 * 3 = 6`, `6 * 4 = 24`.

---

## 3. Base Case and Recursive Case

Every recursive function must have:
- **Base Case**: Prevents infinite recursion by providing a stopping point.
- **Recursive Case**: Breaks the problem into a smaller subproblem and calls the function again.

Without a proper base case, recursion can lead to a **stack overflow** error, where Python runs out of memory due to too many function calls.

---

## 4. Simple Examples of Recursion

### Example 1: Factorial
The factorial of a number `n` is the product of all positive integers less than or equal to `n`. For example, `5! = 5 * 4 * 3 * 2 * 1 = 120`.

```python
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Output: 120
```

### Example 2: Fibonacci Sequence
The Fibonacci sequence is a series where each number is the sum of the two preceding ones: `0, 1, 1, 2, 3, 5, 8, ...`.

```python
def fibonacci(n):
    # Base cases: F(0) = 0, F(1) = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
print(fibonacci(6))  # Output: 8
```

### Example 3: Sum of a List
Calculate the sum of all elements in a list using recursion.

```python
def list_sum(lst):
    # Base case: empty list has sum 0
    if not lst:
        return 0
    # Recursive case: first element + sum of rest
    else:
        return lst[0] + list_sum(lst[1:])

# Test the function
print(list_sum([1, 2, 3, 4]))  # Output: 10
```

---

## 5. Advantages and Disadvantages of Recursion

### Advantages:
- **Simpler Code**: Recursion can make complex problems (e.g., tree traversals) easier to understand and implement.
- **Natural Fit**: Ideal for problems with a recursive structure, like fractals, trees, or divide-and-conquer algorithms.
- **Readability**: Recursive solutions are often more concise than iterative ones.

### Disadvantages:
- **Performance Overhead**: Each recursive call adds a new frame to the call stack, consuming memory.
- **Risk of Stack Overflow**: Deep recursion (e.g., large inputs) can exhaust the stack.
- **Inefficiency**: Some recursive solutions (e.g., Fibonacci) recalculate the same values multiple times.

---

## 6. Common Pitfalls and How to Avoid Them

### Pitfall 1: Stack Overflow
Python has a default recursion limit (typically 1000). Exceeding this limit causes a `RecursionError`.

**Solution**: 
- Increase the recursion limit using `sys.setrecursionlimit(limit)` (use cautiously).
- Optimize the function to reduce the number of recursive calls.
- Use iteration or tail recursion where possible.

```python
import sys
sys.setrecursionlimit(2000)  # Increase limit to 2000
```

### Pitfall 2: Inefficient Recursion
The naive Fibonacci implementation recalculates values multiple times, leading to exponential time complexity (`O(2^n)`).

**Solution**: Use **memoization** to cache results (see Section 9).

---

## 7. Tail Recursion and Optimization

**Tail recursion** occurs when the recursive call is the last operation in the function. Some languages optimize tail recursion by reusing the same stack frame, but **Python does not support tail recursion optimization**.

### Example of Tail Recursion:
```python
def factorial_tail(n, accumulator=1):
    if n == 0 or n == 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

# Test the function
print(factorial_tail(5))  # Output: 120
```

In this example, the `accumulator` carries the intermediate result, reducing the need for stack unwinding. However, Python still creates new stack frames for each call.

---

## 8. Advanced Examples

### Example 1: Binary Tree Traversal
Recursion is ideal for tree-based data structures. Below is an example of an **in-order traversal** of a binary tree.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node is None:
        return
    # Recursive case: traverse left, visit node, traverse right
    inorder_traversal(node.left)
    print(node.value, end=' ')
    inorder_traversal(node.right)

# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Test the function
inorder_traversal(root)  # Output: 4 2 5 1 3
```

### Example 2: Tower of Hanoi
The Tower of Hanoi is a classic recursive problem where you move `n` disks from one rod to another, using a third rod as auxiliary.

```python
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    # Move nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# Test the function
tower_of_hanoi(3, 'A', 'B', 'C')
```

**Output**:
```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

---

## 9. Memoization for Optimizing Recursive Functions

Memoization stores the results of expensive function calls and reuses them when the same inputs occur again. This is particularly useful for problems like Fibonacci, which have overlapping subproblems.

### Memoized Fibonacci Example:
```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Test the function
print(fibonacci_memo(50))  # Much faster than naive recursion
```

Alternatively, you can use Python’s `functools.lru_cache` decorator for memoization:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

# Test the function
print(fibonacci_cached(50))
```

This reduces the time complexity of Fibonacci from `O(2^n)` to `O(n)`.

---

## 10. When to Use Recursion vs. Iteration

### When to Use Recursion:
- Problems with a natural recursive structure (e.g., tree traversals, divide-and-conquer algorithms).
- Code readability and simplicity are prioritized over performance.
- Small input sizes where stack overflow is not a concern.

### When to Use Iteration:
- Large inputs where recursion depth could cause stack overflow.
- Performance is critical, as iteration avoids call stack overhead.
- Problems that are naturally iterative (e.g., summing a list).

### Example: Iterative Factorial
```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))  # Output: 120
```

---

## 11. Practice Problems

1. **Sum of Digits**: Write a recursive function to calculate the sum of digits of a number (e.g., `123` → `1 + 2 + 3 = 6`).
2. **Power Function**: Implement a recursive function to calculate `x^n` (x raised to power n).
3. **Reverse a String**: Write a recursive function to reverse a string.
4. **Binary Search**: Implement a recursive binary search algorithm.
5. **Permutations**: Generate all permutations of a string using recursion.

**Sample Solution (Sum of Digits)**:
```python
def sum_of_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(123))  # Output: 6
```

---

## 12. Additional Resources

- **Books**:
  - *Think Like a Programmer* by V. Anton Spraul (Chapter on recursion).
  - *Introduction to Algorithms* by Cormen et al. (Divide-and-conquer algorithms).
- **Online Tutorials**:
  - Real Python: "Recursion in Python: An Introduction" (realpython.com).
  - GeeksforGeeks: "Recursion in Python" (geeksforgeeks.org).
- **Interactive Platforms**:
  - LeetCode: Solve recursion-based problems (e.g., "Climbing Stairs", "N-Queens").
  - HackerRank: Practice recursion challenges.

---

## Key Takeaways
- Recursion simplifies problems by breaking them into smaller subproblems.
- Always define a base case to prevent infinite recursion.
- Use memoization to optimize recursive functions with overlapping subproblems.
- Be cautious of Python’s recursion limit and consider iteration for large inputs.
- Practice recursive problems to build intuition for when and how to use recursion effectively.

---

This material provides a thorough understanding of recursion in Python, from basics to advanced applications. If you’d like me to expand on any section, provide more examples, or help with specific practice problems, let me know!