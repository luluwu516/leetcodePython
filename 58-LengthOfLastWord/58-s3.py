class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        last_word_count = 0

        for i in range(len(s)):
            if s[i] != " ":
                count += 1
                last_word_count = count
            else:
                count = 0
        return last_word_count


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
