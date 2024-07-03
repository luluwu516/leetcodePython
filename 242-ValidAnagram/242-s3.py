class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False

        return True


def main():
    # declaration
    solution = Solution()

    # input
    s = input("Enter a string: ")
    t = input("Enter another string: ")

    # processing
    res = solution.isAnagram(s, t)

    # output
    print("\nResult:")
    print("Two strings are", ("anagram" if res else "not anagram"))


if __name__ == "__main__":
    main()
