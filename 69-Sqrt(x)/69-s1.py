class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        for i in range(1, x + 1):
            if i * i > x:
                return i - 1


def main():
    # declaration and input
    s = Solution()
    num = int(input("Enter a binary number: "))

    # processing
    result = s.mySqrt(num)

    # output
    print("\nResult:")
    print(f"The square root of {num} is {result}.")


if __name__ == "__main__":
    main()
