from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        # for r in ransomNote_counter.keys():
        #     if magazine_counter[r] < ransomNote_counter[r]:
        #         return False

        # return True

        # return ransomNote_counter & magazine_counter == ransomNote_counter

        return ransomNote_counter <= magazine_counter


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
