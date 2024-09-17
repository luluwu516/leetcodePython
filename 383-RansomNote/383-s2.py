class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_list = list(ransomNote)
        for c in magazine:
            if c in ransomNote_list:
                ransomNote_list.remove(c)

        # return len(ransomNote_list) == 0
        return not ransomNote_list


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
