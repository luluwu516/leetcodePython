from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]

        return shortest


def main():
    # declaration
    s = Solution()

    # input
    strs = input("Enter a list of strings separated by space: ").split()

    # processing
    result = s.longestCommonPrefix(strs)

    # output
    print("\nThw longest common prefix:", result)


if __name__ == "__main__":
    main()
