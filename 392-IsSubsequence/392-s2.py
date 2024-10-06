class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sizeS = len(s)
        sizeT = len(t)
        i = 0
        index = 0

        while i < sizeT and index < sizeS:
            if s[index] == t[i]:
                index += 1
            i += 1

        return index == sizeS


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
