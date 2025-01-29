def maxArea(self, height):

    left = 0
    right = len(height) - 1
    max_vol = 0

    while left < right:
        # update max vol if found
        max_vol = max(max_vol, min(height[right], height[left]) * (right - left))

        # update left/right pointers
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_vol
