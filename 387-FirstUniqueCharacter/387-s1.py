from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for letter, count in counter.items():
            if count == 1:
                return s.index(letter)
        return -1


def main():
    # declaration and input
    s = Solution()
    string = input("\nEnter a string: ")

    # processing
    res = s.firstUniqChar(string)

    # output
    print("\nResult:")
    if res != -1:
        print(
            f"The character {string[res]} at index {res} is the first character that does not occur at any other index.\n"
        )
    else:
        print("The non-repeating character does not exist.\n")


if __name__ == "__main__":
    main()
