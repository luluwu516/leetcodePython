class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = dict()
        for c in ransomNote:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1

        for c in magazine:
            if c in dict1:
                dict1[c] -= 1

        for count in dict1.values():
            if count > 0:
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
