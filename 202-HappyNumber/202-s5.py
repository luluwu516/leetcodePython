class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        slow = self.square(slow)
        fast = self.square(self.square(fast))
        while fast != 1 and fast != slow:
            slow = self.square(slow)
            fast = self.square(self.square(fast))
        return fast == 1

    def square(self, n):
        ans = 0
        while n > 0:
            ans += (n % 10) ** 2
            n //= 10
        return ans


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
