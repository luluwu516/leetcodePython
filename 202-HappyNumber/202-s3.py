class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        total = sum([int(d) ** 2 for d in str(n)])
        while total not in seen:
            seen.add(total)
            total = sum([int(d) ** 2 for d in str(total)])
            if total == 1:
                return True
        return False


def main():
    # declaration
    s = Solution()

    # input
    num = input("Enter a positive number: ")

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
