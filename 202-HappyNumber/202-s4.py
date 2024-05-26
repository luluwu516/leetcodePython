class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sumOfSquareDigits(n)
            if n == 1:
                return True
        return False

    def sumOfSquareDigits(self, n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit**2
            n //= 10
        return total


def main():
    # declaration
    s = Solution()

    # input
    num = int(input("Enter a positive number: "))

    # processing
    res = s.isHappy(num)

    # output
    print("\nResult:")
    print(
        "The number is ",
        ("a" if res else "not a"),
        " happy number.",
        sep="",
    )


if __name__ == "__main__":
    main()
