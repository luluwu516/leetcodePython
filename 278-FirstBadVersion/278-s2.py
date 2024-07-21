class Solution:
    def __init__(self, n: int, bad: int):
        self.n = n
        self.bad_version = bad

    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        def helper(n, left, right):
            mid = (left + right) // 2
            if not self.isBadVersion(mid - 1) and self.isBadVersion(mid):
                return mid

            if self.isBadVersion(mid):
                return helper(mid, 1, mid)
            elif not self.isBadVersion(mid):
                return helper(n, mid + 1, n)

        return helper(n, left, right)

    def isBadVersion(self, version: int) -> bool:
        return self.bad_version == version


def main():
    # declaration and input
    num = int(input("Enter n: "))
    bad = int(input("Enter the bad version: "))
    s = Solution(num, bad)

    # processing
    res = s.firstBadVersion(num)

    # output
    print("\nResult:")
    print(f"Then {res} is the first bad version")


if __name__ == "__main__":
    main()
