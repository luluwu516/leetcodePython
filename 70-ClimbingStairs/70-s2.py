class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        prev = 1
        curr = 1
        for i in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp

        return curr


def main():
    # declaration and input
    s = Solution()
    num = int(input("Enter how many steps in a staircase: "))

    # processing
    result = s.climbStairs(num)

    # output
    print("\nResult:")
    print(f"There are {result} ways to climb to the top.")


if __name__ == "__main__":
    main()
