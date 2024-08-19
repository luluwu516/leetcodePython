from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

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
