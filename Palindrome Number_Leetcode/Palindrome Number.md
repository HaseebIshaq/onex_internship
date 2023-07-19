# Palindrome Number
This is an **Easy Level** Leetcode problem.
## Problem Description
Given an integer x, you need to determine if it is a palindrome or not. A palindrome is a number that remains the same when its digits are reversed.

## Python Solution
Here's the python solution for the above given problem:
```py
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
```
The given Python solution provides a class Solution with a method isPalindrome that takes in an integer x. The method checks if the integer x is a palindrome.
### Working
- The given code in could be executed on any standardized python environment or IDE e.g. *VScode, Jupyter Notebook, Leetcode IDE etc*, by typing the following command in the terminal:
```py
python streamlit.py
```
- The method converts the integer x to a string using str(x).
- It then compares the string representation of x with its reverse using string slicing (str(x)[::-1]).
- If the string representation of x is equal to its reverse, it means x is a palindrome, and the method returns True.
- If the string representation of x is not equal to its reverse, it means x is not a palindrome, and the method returns False.
- This solution converts the integer to a string and compares it with its reverse to determine if it is a palindrome or not.
  
## Results
This solution converts the integer to a string and compares it with its reverse to determine if it is a palindrome or not. This memory usage gives a **94.44%** of the Beat score among other solutions and beats **95.88%** of the runtime.