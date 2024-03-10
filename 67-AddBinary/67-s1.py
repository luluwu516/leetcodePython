class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            sum_digits = digit_a + digit_b + carry

            result_digit = sum_digits % 2
            carry = sum_digits // 2

            result.insert(0, str(result_digit))

            i -= 1
            j -= 1

        return "".join(result)


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
