def isAnagram(s: str, t: str) -> bool:
    # if s and t are not of same length, return false
    # make 2 hashes of s and t where value: no of occurrences
    # check if union of set is same
    if len(s) != len(t):
        return False

    # map characters in s
    s_char = {}
    for char in s:
        s_char[char] = s_char.get(char, 0) + 1

    # iterate through t
    for letter in t:
        if letter not in s_char:
            return False
        else:
            if s_char[letter] == 0:
                return False
            else:
                s_char[letter] -= 1

    return True
