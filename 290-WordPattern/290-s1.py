class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        if len(set(pattern)) != len(set(s)):
            return False

        d = dict()
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = s[i]
            else:
                if d[pattern[i]] != s[i]:
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
