from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)

        for i in range(length):
            if i != nums[i]:
                return i

        return length


def main():
    # declaration and input
    s = Solution()
    num = input("Enter integers (separated by spaces): ").split()
    num = [int(n) for n in num]

    # processing
    res = s.missingNumber(num)

    # output
    print("\nResult:")
    print("The missing integer is", res)


if __name__ == "__main__":
    main()
