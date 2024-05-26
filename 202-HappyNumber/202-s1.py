class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n, seen):
            if n == 1:
                return True
            if n in seen:
                return False

            seen.add(n)
            digits = [int(d) for d in str(n)]
            total = 0
            for d in digits:
                total += d**2

            return helper(total, seen)

        return helper(n, set())


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
