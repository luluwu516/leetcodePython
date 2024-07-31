class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1, map2 = {}, {}
        s = s.split()
        if len(pattern) != len(s):
            return False

        for c, word in zip(pattern, s):
            if (c in map1 and map1[c] != word) or (word in map2 and map2[word] != c):
                return False
            map1[c] = word
            map2[word] = c

        return True


def main():
    # declaration and input
    s = Solution()
    pattern = input("\nEnter pattern (only lower-case English letters): ")
    inputs = input("Enter words (seperated by space): ")

    # processing
    res = s.wordPattern(pattern, inputs)

    # output
    print("\nResult:")
    print(res, "\n")


if __name__ == "__main__":
    main()
