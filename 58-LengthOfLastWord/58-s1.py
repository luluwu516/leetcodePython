class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs = s.split()
        return len(strs[-1])
        # return len(s.split()[-1])


def main():
    # declaration and input
    s = Solution()
    string = input("Enter a string: ")

    # processing
    length_of_last_word = s.lengthOfLastWord(string)

    # output
    print("\nResult: ")
    print("The length of the last word is", length_of_last_word)


if __name__ == "__main__":
    main()
