from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        # print(counter) # Output: Counter({2: 4, 1: 3})
        return max(counter, key=counter.get)

        # counter = Counter(nums).most_common()
        # print(counter) # Output: [(2, 4), (1, 3)]
        # return counter[0][0]


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
