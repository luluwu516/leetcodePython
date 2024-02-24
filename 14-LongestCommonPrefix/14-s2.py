from typing import List


class Solution:
    # Solution from sagarsindhu36
    # https://leetcode.com/problems/longest-common-prefix/solutions/4711312/simple-and-easy-solution-in-java-python-c-c
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                # Check if the current index i is out of bounds for the current string (strs[j])
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]

        return prefix


def main():
    # declaration
    s = Solution()

    # input
    strs = input("Enter a list of strings separated by space: ").split()

    # processing
    result = s.longestCommonPrefix(strs)

    # output
    print("\nThe longest common prefix:", result)


if __name__ == "__main__":
    main()
