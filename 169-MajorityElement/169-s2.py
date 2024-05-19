from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = nums[0]
        for n in nums:
            if count == 0:
                majority = n
                count += 1
            elif majority == n:
                count += 1
            else:
                count -= 1

        return majority


def main():
    # declaration
    s = Solution()

    # input
    nums = input("Enter the numbers (seperated by comma): ").split(",")
    nums = [int(n) for n in nums]

    # processing
    res = s.majorityElement(nums)

    # output
    print("\nResult:")
    print(f"The majority element is {res}")


if __name__ == "__main__":
    main()
