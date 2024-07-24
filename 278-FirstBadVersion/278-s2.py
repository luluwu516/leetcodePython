class Solution:
    def __init__(self, bad: int):
        self.bad_version = bad

    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        def helper(left, right):
            if left <= right:
                mid = (left + right) // 2
                if self.isBadVersion(mid):
                    if mid == 1 or not self.isBadVersion(mid - 1):
                        return mid
                    else:
                        return helper(left, mid - 1)
                else:
                    return helper(mid + 1, right)
            return left

        # def helper(n, left, right):
        #     mid = (left + right) // 2
        #     if not self.isBadVersion(mid - 1) and self.isBadVersion(mid):
        #         return mid

        #     if self.isBadVersion(mid):
        #         return helper(mid, 1, mid)
        #     elif not self.isBadVersion(mid):
        #         return helper(n, mid + 1, n)

        # return helper(n, left, right)
        return helper(left, right)

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
