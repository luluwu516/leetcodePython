class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_dict = dict()
        for c in s:
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] += 1
        for c in t:
            if c not in char_dict:
                return False
            char_dict[c] -= 1
        for count in char_dict.values():
            if count != 0:
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
