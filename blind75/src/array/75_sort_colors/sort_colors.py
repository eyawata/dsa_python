def sortColors(self, nums):
    # two pointer
    # swap fn

    # O(n) time
    # O(1) space

    left = 0
    right = len(nums) - 1
    i = 0

    def swap(j, k):
        temp = nums[j]
        nums[j] = nums[k]
        nums[k] = temp

    # left pointer has to always be the furthest zero value
    # so if i = 0, swap and advance left
    # but if i = 2 (the highest val), then swap with right (because 2s are always right most in the array)
    # else (i = 1) - advance i as per normal without any swapping

    # base case - when i is past right pointer, exit loop

    while i <= right:
        if nums[i] == 0:
            swap(i, left)
            left += 1
            i += 1
        elif nums[i] == 2:
            swap(i, right)
            right -= 1
        else:
            i += 1
