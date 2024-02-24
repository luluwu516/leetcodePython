class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False

        parentheses = {"{": "}", "[": "]", "(": ")"}
        stack = []

        for c in s:
            if c in parentheses:
                stack.append(c)
            else:
                if stack == [] or c != parentheses[stack[-1]]:
                    return False
                else:
                    stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False


def main():
    # declaration
    s = Solution()

    # input
    strs = input("Enter parentheses, such as '(', ')', '{', '}', '[' or ']': ")

    # processing
    result = s.isValid(strs)

    # output
    if result:
        print("\nThe parentheses is vaild.")
    else:
        print("\nThe parentheses is invaild.")


if __name__ == "__main__":
    main()
