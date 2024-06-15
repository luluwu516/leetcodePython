from typing import List


# Time Limit Exceeded
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and j - i <= k:
                    print(i, j)
                    return True

        return False


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
