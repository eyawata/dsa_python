def longestPalindrome(s):
    tracker = set()
    counter = 0

    for letter in s:
        if letter in tracker:
            tracker.remove(letter)
            counter += 2
        else:
            tracker.add(letter)

    if tracker:
        counter += 1

    return counter
