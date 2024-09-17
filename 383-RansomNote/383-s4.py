class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, "", 1)
                # print(magazine)
            else:
                return False

        return True


def main():
    # declaration and input
    s = Solution()
    ransomNote = input("\nEnter ransom note: ")
    magazine = input("Enter magazine: ")

    # processing
    res = s.canConstruct(ransomNote, magazine)

    # output
    print("\nResult:")
    print(
        f"Each letter in magazine can{'' if res else ' not'} only be used once in ransom note\n"
    )


if __name__ == "__main__":
    main()
