def isPalindrome(s):
    # remove punctuations
    # lowercase
    # check if palindrom s == s[::-1]

    s = [char.lower() for char in s if char.isalnum()]
    s = "".join(s)

    print(s)

    return s == s[::-1]
