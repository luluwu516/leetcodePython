class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        s_and_t_set = set()

        for c1, c2 in zip(s, t):
            s_and_t_set.add((c1, c2))

        return len(s_and_t_set) == len(set(s))


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
