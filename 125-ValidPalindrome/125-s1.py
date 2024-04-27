class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        for c in s:
            if c.isalnum():
                letters.append(c.lower())

        return letters == letters[::-1]


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
