# brute force approach: O(n^2) with nested for loop
# time complexity: O(n)
# space complexity: O(n)


def dailyTemperatures(self, temperatures):
    active_temps = []  # keeps track of active indexes
    result = [0] * len(temperatures)  # stores final results, initialized as n zeros

    for i in range(len(result)):

        # while stack is not empty and if current number is higher than the last
        while active_temps and temperatures[i] > temperatures[active_temps[-1]]:
            # pop last index from stack and update difference
            id_to_update = active_temps.pop()
            result[id_to_update] = i - id_to_update

        # append last index
        active_temps.append(i)

    return result
