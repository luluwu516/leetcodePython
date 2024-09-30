class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        size = len(s)
        hash = {}
        for i in range(size):
            if s[i] in hash:
                hash[s[i]] += 1
            else:
                hash[s[i]] = 1

        for i in range(size + 1):
            if t[i] not in hash or hash[t[i]] == 0:
                return t[i]
            else:
                hash[t[i]] -= 1


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
