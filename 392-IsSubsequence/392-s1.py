class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        size = len(t)

        def containLetter(s: str, t: str, index: int, startIndex: int):
            if index > len(s) - 1:
                return True

            for i in range(startIndex, size):
                if s[index] == t[i]:
                    return True and containLetter(s, t, index + 1, i + 1)

            return False

        return containLetter(s, t, 0, 0)


def main():
    # declaration and input
    s = Solution()
    string1 = input("\nEnter s: ")
    string2 = input("Enter t: ")

    # processing
    res = s.isSubsequence(string1, string2)

    # output
    print("\nResult:")
    print(
        f"'s' is{'' if res else ' not'} a new string that is formed from 't' by deleting some (can be none) of the characters\n"
    )


if __name__ == "__main__":
    main()
