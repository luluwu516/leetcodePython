class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        for i in range(size - 1):
            for j in range(i + 1, size):
                if nums[i] + nums[j] == target:
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
