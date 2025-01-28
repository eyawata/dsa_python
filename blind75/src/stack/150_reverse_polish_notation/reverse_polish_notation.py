# https://leetcode.com/problems/evaluate-reverse-polish-notation/


def evalRPN(self, tokens):
    nums = []

    for token in tokens:
        if len(token) > 1 or token.isdigit():
            nums.append(int(token))
        else:  # token is an operator
            if token == "+":
                nums[-2] += nums[-1]
            elif token == "-":
                nums[-2] -= nums[-1]
            elif token == "*":
                nums[-2] *= nums[-1]
            elif token == "/":
                # // will not work as it rounds UP
                nums[-2] = int(float(nums[-2]) / nums[-1])

            nums.pop()

    return nums[0]
