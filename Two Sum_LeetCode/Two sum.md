# Two Sum
This is an **Easy Level** Leetcode problem.
## Problem Description
Given an array of integers nums and an integer target, you need to find two numbers in the array such that they add up to the target.

You can assume that each input will have exactly one solution, and you cannot use the same element twice.

You need to return the indices of the two numbers that add up to the target. The order of the indices does not matter.

## Python Solution
Here's the python solution for the above given problem:
```py
class Solution(object):
    def twoSum(self, nums, target):
        num_indices = {}  # Dictionary to store numbers and their indices

        for index, num in enumerate(nums):
            complement = target - num

            if complement in num_indices:
                return [num_indices[complement], index]

            num_indices[num] = index  # Store the current number and its index

        return []  # Return an empty list if no solution is found
```
The given Python solution provides a *class Solution* with a method twoSum that takes in an array of integers nums and an integer target. The method finds two numbers in the array that add up to the target.
### Working
- The given code in could be executed on any standardized python environment or IDE e.g. *VScode, Jupyter Notebook, Leetcode IDE etc*, by typing the following command in the terminal:
```py
python streamlit.py
```
- The method utilizes a dictionary num_indices to store numbers and their indices as we iterate through the array.
- For each number num in the array, we calculate the complement (target - num).
- If the complement is already present in the dictionary, it means we have found the two numbers that add up to the target. We return their indices from the dictionary.
- If the complement is not present in the dictionary, we store the current number num and its index in the dictionary.
- If no solution is found after iterating through the entire array, we return an empty list.

## Results
This solution has a time complexity of O(n), where n is the length of the input array nums.This memory usage gives a **93.67%** of the Beat score among other solutions.