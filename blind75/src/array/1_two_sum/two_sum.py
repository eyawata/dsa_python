# https://leetcode.com/problems/two-sum/description/


def twoSum(nums, target):
    # generate a hashmap of visited numbers as we iterate
    # check if remainder is in the hashmap

    # time complexity is O(n) as we only visit each elemeent once
    # space complexity is O(n) worse case

    visited = {}  # value: index

    for i in range(len(nums)):
        remainder = target - nums[i]

        if remainder in visited:
            return [visited[remainder], i]

        # else add to visited hash
        visited[nums[i]] = i

    return -1
