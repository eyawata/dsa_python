def canCompleteCircuit(gas, cost):
    # greedy algorithm
    # time complexity: O(n)
    # space: O(1)

    # check first if a solution exists
    if sum(gas) < sum(cost):
        return -1

    # now we know a solution is definitely out there we iterate
    total = 0
    start_index = 0
    # for each element, if the gas supplied - cost is negative, reset total and advance starting i
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            total = 0
            start_index = i + 1

    return start_index
