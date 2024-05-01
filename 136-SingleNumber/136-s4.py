from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = list(nums)
        queue = []

        while temp:
            current = temp.pop()
            if current not in temp and current not in queue:
                return current
            else:
                queue.append(current)


def main():
    # declaration
    s = Solution()

    # input
    nums = input("Enter the numbers (seperated by comma): ").split(",")
    nums = [int(n) for n in nums]

    # processing
    res = s.singleNumber(nums)

    # output
    print("\nResult:")
    print("Number", res, "only appears one time")


if __name__ == "__main__":
    main()
