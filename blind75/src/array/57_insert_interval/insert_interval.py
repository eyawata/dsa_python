# time complexity is
# space complexity is


def insert(intervals, newInterval):
    result = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            # upper limit occurs before interval start
            result.append(newInterval)
            # insert is done, exit and append the rest
            return result + intervals[i:]

        elif newInterval[0] > intervals[i][1]:
            # insert has begun but not yet ended
            result.append(intervals[i])

        else:
            # there is overlap and we need to update the lower and upper limits in newInterval
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]

    # append the newInterval after for loop i.e. newInterval is the last in result
    result.append(newInterval)

    return result
