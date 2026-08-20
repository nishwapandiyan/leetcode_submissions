# 220. Contains Duplicate III

[![LeetCode Link](https://img.shields.io/badge/LeetCode-Problem_Link-FFA116?style=flat-square&logo=leetcode)](https://leetcode.com/problems/contains-duplicate-iii/)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-22c55e?style=flat-square)

## Problem Statement

You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:


	i != j,
	abs(i - j) <= indexDiff.
	abs(nums[i] - nums[j]) <= valueDiff, and


Return true if such pair exists or false otherwise.

 
Example 1:

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0


Example 2:

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.


 
Constraints:


	2 <= nums.length <= 105
	-109 <= nums[i] <= 109
	1 <= indexDiff <= nums.length
	0 <= valueDiff <= 109

## Examples

```
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.
```

## Constraints

- i != j,
- abs(i - j) <= indexDiff.
- abs(nums[i] - nums[j]) <= valueDiff, and

---
*Synced automatically with [AlgoVault](https://github.com/mr-sanjai-offl/AlgoVault)*