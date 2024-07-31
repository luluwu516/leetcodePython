from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        seen = defaultdict(str)
        i = 0
        for word in words:
            if word in seen and seen[word] != pattern[i]:
                return False
            elif word not in seen and pattern[i] in seen.values():
                return False
            seen[word] = pattern[i]
            i += 1

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
