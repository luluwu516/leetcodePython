import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        s = s.lower()

        return s == s[::-1]


def main():
    # declaration
    s = Solution()

    # input
    string = input("Enter the string: ")

    # processing
    res = s.isPalindrome(string)

    # output
    print("\nResult:")
    print("The string is", "" if res else " not", " a palindrome", sep="")


if __name__ == "__main__":
    main()
