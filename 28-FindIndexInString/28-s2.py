class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


def main():
    # declaration and input
    s = Solution()
    haystack = input("Enter the first string: ")
    needle = input("Enter the second string: ")

    # processing
    index = s.strStr(haystack, needle)

    # output
    print("\nResult: ")
    if index != -1:
        print('The first "', needle, '" occurs at index ', index, sep="")
    else:
        print('"', needle, '" did not occur in "', haystack, '"', sep="")


if __name__ == "__main__":
    main()
