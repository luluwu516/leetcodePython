from typing import List


# Time Limit Exceeded
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d and (i - d[nums[i]]) <= k:
                return True
            d[nums[i]] = i

        return False

        # d = {}
        # for i, num in enumerate(nums):
        #     if num in d and (i - d[num]) <= k:
        #         return True
        #     d[num] = i

        # return False


def main():
    # declaration
    s = Solution()

    # input
    nums = input("Enter the numbers (seperated by comma): ").split(",")
    nums = [int(n) for n in nums]

    k = int(input("Enter an integer k: "))

    # processing
    res = s.containsNearbyDuplicate(nums, k)

    # output
    print("\nResult:")
    print("The array", ("contains" if res else "doesn't contain"), "duplicate")


if __name__ == "__main__":
    main()
