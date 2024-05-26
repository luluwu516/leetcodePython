class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        digits = [int(d) for d in str(n)]
        total = 0
        while total != 1:
            total = 0
            for d in digits:
                total += d**2
            if total in seen:
                return False
            seen.add(total)
            digits = [int(d) for d in str(total)]

        return True


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
