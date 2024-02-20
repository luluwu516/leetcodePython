class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0

        # Solution form hgrsd
        # https://leetcode.com/problems/roman-to-integer/solutions/264743/clean-python-beats-99-78
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        for char in s:
            sum += roman_to_int[char]

        return sum


def main():
    s = Solution()
    roman = input("Enter Roman numerals (I, V, X, L, C, D, or M): ")
    print(f"Result: {s.romanToInt(roman)}")


if __name__ == "__main__":
    main()
