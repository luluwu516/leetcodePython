class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                count = 1
                if i > 0:
                    j = i - 1
                    while s[j] != " ":
                        if j < 0:
                            break
                        count += 1
                        j -= 1

                    return count

        return count


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
