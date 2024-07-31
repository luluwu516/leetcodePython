class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        d1 = dict()
        d2 = dict()

        for i in range(len(pattern)):
            if pattern[i] not in d1:
                d1[pattern[i]] = s[i]
            if s[i] not in d2:
                d2[s[i]] = pattern[i]
            if d1[pattern[i]] != s[i] or d2[s[i]] != pattern[i]:
                return False

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
