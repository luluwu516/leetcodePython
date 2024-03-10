class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = bin(int(a, 2) + int(b, 2))
        return s[2:]


def main():
    # declaration and input
    s = Solution()
    binary_num1 = input("Enter a binary number: ")
    binary_num2 = input("Enter another binary number: ")

    # processing
    result = s.addBinary(binary_num1, binary_num2)

    # output
    print("\nResult:")
    print("The sum of two binary numbers is:", result)


if __name__ == "__main__":
    main()
