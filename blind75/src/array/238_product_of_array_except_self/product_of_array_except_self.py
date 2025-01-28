def productExceptSelf(nums):
    # solution is from Neetcode

    res = [1] * (len(nums))

    # iterate from beginning
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    # iterate from end
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res
