class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n % 2 == 0:
            return self.isUgly(n / 2)
        elif n % 3 == 0:
            return self.isUgly(n / 3)
        elif n % 5 == 0:
            return self.isUgly(n / 5)
        else:
            return False


def main():
    # declaration and input
    s = Solution()
    num = int(input("Enter an integer: "))

    # processing
    res = s.isUgly(num)

    # output
    print("\nResult:")
    print("The integer is%s a ugly number", ("" if res else " not"))


if __name__ == "__main__":
    main()
