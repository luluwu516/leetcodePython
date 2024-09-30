from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counterS = Counter(s)
        counterT = Counter(t)

        for item, count in counterT.items():
            if count > counterS[item]:
                return item


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


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        size = len(s)
        sumS, sumT = 0, 0
        for i in range(size):
            sumS += ord(s[i])
            sumT += ord(t[i])
        sumT += ord(t[size])

        return chr(sumT - sumS)


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
