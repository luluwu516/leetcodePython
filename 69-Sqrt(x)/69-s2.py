class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left = 1
        right = x
        while left < right:
            mid = (left + right) // 2 + 1
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid
            else:
                right = mid - 1

        return left


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
