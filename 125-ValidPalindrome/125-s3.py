class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


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
