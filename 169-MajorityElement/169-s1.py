from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = dict()
        for n in nums:
            if n in num_dict:
                num_dict[n] += 1
            else:
                num_dict[n] = 0

        largest = nums[0]
        for key, value in num_dict.items():
            if num_dict[largest] < value:
                largest = key

        return largest


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
