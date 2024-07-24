class Solution:
    def __init__(self, bad: int):
        self.bad_version = bad

    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

    def isBadVersion(self, version: int) -> bool:
        return self.bad_version == version


def main():
    # declaration and input
    bad = int(input("Enter the bad version: "))
    s = Solution(bad)
    num = int(input("Enter n: "))

    # processing
    res = s.firstBadVersion(num)

    # output
    print("\nResult:")
    print(f"Version {res} is the first bad version")


if __name__ == "__main__":
    main()
