# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def Solution(self, pick: int = 0):
        self.__pick = pick

    def setPick(self, pick_num: int) -> None:
        self.__pick = pick_num

    def guess(self, guess_num: int) -> int:
        if guess_num == self.__pick:
            return 0
        elif guess_num > self.__pick:
            return -1
        else:
            return 1

    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            res = self.guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                low = mid + 1
            else:
                high = mid - 1

        return 0


def main():
    # declaration and input
    s = Solution()
    num = int(input("\nEnter the pick: "))
    s.setPick(num)
    num = int(input("Enter an integer: "))

    # processing
    res = s.guessNumber(num)

    # output
    print("\nResult:")
    print(f"The pick number is {res}\n")


if __name__ == "__main__":
    main()
