class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        return str(x) == str(x)[::-1]


def main():
    num = int(input("Enter a number: "))
    s = Solution()

    if s.isPalindrome(num):
        print(f"The number {num} is Palindrome.")
    else:
        print(f"The number {num} is not Palindrome.")


if __name__ == "__main__":
    main()
