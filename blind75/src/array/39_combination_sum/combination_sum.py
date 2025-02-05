def combinationSum(candidates, target):
    # recursive helper fn
    def find_combinations(index, target_sum):
        if target_sum == 0:
            results.append(temp_arr[:])
            return
        # if i exceeds or current candidate > target: return
        if index >= len(candidates) or candidates[index] > target_sum:
            return

        # recursively call on next candidate and current target sum
        find_combinations(index + 1, target_sum)
        # append candidate to temp arr
        temp_arr.append(candidates[index])
        # recursively call on candidate but look for difference to targetsum
        find_combinations(index, target_sum - candidates[index])
        # pop last element from temp arr
        temp_arr.pop()

    candidates.sort()
    results = []
    temp_arr = []
    find_combinations(0, target)
    return results
