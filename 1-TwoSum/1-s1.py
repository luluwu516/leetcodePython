from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size - 1):
            second = nums[i] - target
            for j in range(i + 1, size):
                if nums[j] == second:
                    return {i, j}

        return {}


def main():
    s = Solution()
    nums = []
    num = int(input("Enter a number, -1 to stop: "))
    while num != -1:
        nums.append(num)
        num = int(input("Enter a number, -1 to stop: "))

    target = int(input("\nEnter the target: "))
    result = s.twoSum(nums, target)

    print("\nThe user input: ", nums)
    if result == {}:
        print("No two sum solution\n")
    else:
        print("Result:", result)


if __name__ == "__main__":
    main()
