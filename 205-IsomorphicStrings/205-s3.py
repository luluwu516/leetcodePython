class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for c1, c2 in zip(s, t):
            if c1 in dict1:
                if dict1[c1] != c2:
                    return False
            if c2 in dict2:
                if dict2[c2] != c1:
                    return False

            dict1[c1] = c2
            dict2[c2] = c1

        return True


def main():
    # declaration
    solution = Solution()

    # input
    s = input("Enter a string: ")
    t = input("Enter another string: ")

    # processing
    res = solution.isIsomorphic(s, t)

    # output
    print("\nResult:")
    print("Two strings are", ("isomorphic" if res else "not isomorphic"))


if __name__ == "__main__":
    main()
