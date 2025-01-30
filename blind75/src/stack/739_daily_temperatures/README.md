# 739 Daily Temperatures

https://leetcode.com/problems/daily-temperatures/description/

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

## Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]

Output: [1,1,4,2,1,1,0,0]

## Example 2:

Input: temperatures = [30,40,50,60]

Output: [1,1,1,0]

## Example 3:

Input: temperatures = [30,60,90]

Output: [1,1,0]
 

## Solution notes:
Why is a Stack applicable?

1. **Monotonic Stack**: In this problem, we maintain a decreasing stack, which means the elements from bottom to top are in decreasing order. This is because we only push the current temperature into the stack when it’s less than or equal to the temperature at the top of the stack. Otherwise, we pop the top element until we find a temperature that’s higher or the stack becomes empty.

2. **Next Greater Element Pattern**: The problem is essentially asking for the “Next Greater Element” but with a twist. Instead of returning the next greater element, it’s asking for the distance (days) to the next greater element. This pattern is a classic use-case for a stack.

## How does it improve efficiency?

In the brute force approach, for each temperature, we would check all the following temperatures until we find a higher one. This means we may end up doing unnecessary comparisons that have been done in previous iterations.

However, by using a Stack, we can significantly improve efficiency:

1. **Store Unresolved Temperatures**: The Stack stores the indices of temperatures for which we haven’t yet found a higher temperature. Once we find a higher temperature, we immediately know how many days we have to wait (by calculating the difference in indices), and we don’t need to consider that temperature again.

2. **Avoid Repeated Comparisons**: With the Stack, we only compare each temperature with the following ones once, and we do not do the comparison again in the future. In other words, once an element is popped from the Stack, it’s guaranteed we have found a higher temperature for it and we won’t push it back into the Stack.