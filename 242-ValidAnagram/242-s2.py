from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


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
