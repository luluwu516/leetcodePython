from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        sorted_strs = sorted(strs)

        for i in range(len(sorted_strs[0])):
            check_set = set()
            for j in range(0, len(sorted_strs)):
                if sorted_strs[0][i] != sorted_strs[j][i]:
                    return prefix
                else:
                    check_set.add(sorted_strs[0][i])
            if len(check_set) == 1:
                prefix += sorted_strs[0][i]

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
