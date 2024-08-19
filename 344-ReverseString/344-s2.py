from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s


def main():
    # declaration and input
    s = Solution()
    nums = input("\nEnter characters (seperated by space): ").split()

    # processing
    res = s.reverseString(nums)

    # output
    print("\nResult:")
    print(res)


if __name__ == "__main__":
    main()
