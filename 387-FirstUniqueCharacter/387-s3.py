class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniq_letters = set(s)
        uniq_letters_indexes = []
        for c in uniq_letters:
            if s.count(c) == 1:
                uniq_letters_indexes.append(s.index(c))

        return min(uniq_letters_indexes) if uniq_letters_indexes else -1


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
