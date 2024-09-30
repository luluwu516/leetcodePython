class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sortedS = sorted(s)
        sortedT = sorted(t)
        for i in range(len(s)):
            if sortedS[i] != sortedT[i]:
                return sortedT[i]

        return sortedT[-1]


def main():
    # declaration and input
    s = Solution()
    string1 = input("\nEnter a s: ")
    string2 = input("Enter a t: ")

    # processing
    res = s.findTheDifference(string1, string2)

    # output
    print("\nResult:")
    print(f"'{res}' is the letter that was added\n")


if __name__ == "__main__":
    main()
