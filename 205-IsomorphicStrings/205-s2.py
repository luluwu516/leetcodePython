class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_index = []
        t_index = []
        for c in s:
            s_index.append(s.index(c))
        for c in t:
            t_index.append(t.index(c))

        return s_index == t_index


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
