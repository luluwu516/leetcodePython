class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


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
