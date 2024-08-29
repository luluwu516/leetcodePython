class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        res = ""
        seen_vowels = []
        for c in s:
            if c in vowels:
                seen_vowels.append(c)

        for c in s:
            if c in vowels:
                res += seen_vowels.pop()
            else:
                res += c

        return res


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
