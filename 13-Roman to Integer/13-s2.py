class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = roman_to_int[s[0]]

        for i in range(1, len(s)):
            if s[i] == "V" and s[i - 1] == "I":
                sum -= 2
            elif s[i] == "X" and s[i - 1] == "I":
                sum -= 2
            elif s[i] == "L" and s[i - 1] == "X":
                sum -= 20
            elif s[i] == "C" and s[i - 1] == "X":
                sum -= 20
            elif s[i] == "D" and s[i - 1] == "C":
                sum -= 200
            elif s[i] == "M" and s[i - 1] == "C":
                sum -= 200

            sum += roman_to_int[s[i]]

        return sum


def main():
    s = Solution()
    roman = input("Enter Roman numerals (I, V, X, L, C, D,and M): ")
    print(f"Result: {s.romanToInt(roman)}")


if __name__ == "__main__":
    main()
