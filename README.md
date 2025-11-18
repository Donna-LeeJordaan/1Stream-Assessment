# 1Stream-Assessment

# 📂 String and Sorting Utilities

A Python application providing three utility functions for string manipulation and sorting operations.

## 🔖  Overview

This project implements three core functions:
- **String reversal**: Reverse any input string
- **Palindrome detection**: Check if a string is a palindrome (ignoring case and non-alphanumeric characters)
- **Bubble sort**: Sort lists of integers using the bubble sort algorithm

The solution includes comprehensive test coverage and follows Python best practices.

## ✏️  Functions

### 1. `reverse_string(s: str) -> str`
Returns the reverse of the input string.

**Example:**
```python
reverse_string("hello")  # Returns "olleh"
reverse_string("")       # Returns ""
```

### 2. `is_palindrome(s: str) -> bool`
Determines if a string is a palindrome, ignoring case, spaces, and punctuation.

**Example:**
```
is_palindrome("A man, a plan, a canal: Panama")  # Returns True
is_palindrome("racecar")                         # Returns True
is_palindrome("hello")                           # Returns False
```

### 3. `bubble_sort(nums: list[int]) -> list[int]`
Sorts a list of integers in ascending order using bubble sort algorithm. Returns a new sorted list without modifying the original.

**Example:**
```
bubble_sort([3, 1, 4, 1, 5])  # Returns [1, 1, 3, 4, 5]
bubble_sort([5, 4, 3, 2, 1])  # Returns [1, 2, 3, 4, 5]
```

#  💻  Running the Application

## ✏️ Using the Functions
From solution import reverse_string, is_palindrome, bubble_sort

**Example:**
```
print(reverse_string("hello world"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
```

##  📈  Running Tests
  **Using pytest**
  ```
  pytest test_solution.py -v
  ```
  

##  📒  Test Coverage
The test suite includes:

- **reverse_string**

  ✅ Normal string reversal
  
  ✅ Empty string (edge case)
  
  ✅ Single character
  
  ✅ String with spaces

- **is_palindrome**
  
  ✅ Valid palindrome with punctuation
  
  ✅ Empty string (edge case)
  
  ✅ Non-palindrome strings
  
  ✅ Single character

- **bubble_sort**
  
  ✅ Normal unsorted list
  
  ✅ Empty list (edge case)
  
  ✅ Already sorted list
  
  ✅ Single element list


## 🔨  Testing Strategy Explanation

**How I ensure the functions work correctly:**
- **reverse_string**: Test with normal strings, empty strings, single characters, and strings with numbers
- **is_palindrome**: Test with classic palindromes (with punctuation), non-palindromes, edge cases like empty strings and single characters
- **bubble_sort**: Test with unsorted lists, already sorted lists, empty lists, single elements, and lists with duplicate values

**Why unit testing is the best fit:**
- Automated and repeatable
- Catches regressions when code changes
- Provides immediate feedback
- Easy to add new test cases
- Works well with small, focused functions like these

**To use this solution:**
1. Save each code block in separate files with the specified names
2. Run the tests as shown in the README
3. All tests should pass, confirming your functions work correctly

------------------------------------------------------------------------------------------------------------------------------------------
 📝 *This solution was created as part of a technical assessment demonstrating Python programming skills, testing practices, and documentation.*
