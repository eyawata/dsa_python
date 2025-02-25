def lengthOfLongestSubstring(s):
    # sliding window technique
    # set to keep track of unique characters - O(n) memory
    # left and right pointers to keep track of substring ends
    # if duplicate encountered, remove from leftmost pointer and advance left

    charSet = set()
    res = 0
    left = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        res = max(res, right - left + 1)

    return res
