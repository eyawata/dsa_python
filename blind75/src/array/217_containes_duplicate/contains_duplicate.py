def containsDuplicate(self, nums):
    nums_visited = set()

    for num in nums:
        if num in nums_visited:
            return True
        else:
            nums_visited.add(num)

    return False
