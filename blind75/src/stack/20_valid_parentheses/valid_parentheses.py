def isValid(s):

    pairs = {"(": ")", "{": "}", "[": "]"}

    open_brackets = []

    for bracket in s:
        if bracket in pairs:
            open_brackets.append(bracket)
        elif open_brackets and pairs.get(open_brackets[-1]) == bracket:
            open_brackets.pop()
        else:
            open_brackets.append(bracket)

    if open_brackets:
        return False
    else:
        return True
