class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        left, right = 0, len(s) - 1
        res = list(s)
        while left < right:
            if res[left] in vowels:
                while res[right] not in vowels:
                    right -= 1
                res[left], res[right] = res[right], res[left]
                right -= 1
            left += 1

        return "".join(res)


def main():
    # declaration and input
    s = Solution()
    str = input("Enter a string: ")

    # processing
    res = s.reverseVowels(str)

    # output
    print("\nResult:")
    print("Reverse only all the vowels in the string:", res)


if __name__ == "__main__":
    main()
