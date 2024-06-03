class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        container1 = dict()
        for i in range(len(s)):
            if s[i] not in container1:
                container1[s[i]] = [i]
            else:
                container1[s[i]].append(i)

        container2 = dict()
        for i in range(len(t)):
            if t[i] not in container2:
                container2[t[i]] = [i]
            else:
                container2[t[i]].append(i)

        list1 = list()
        list2 = list()
        for e in container1.values():
            list1.append(e)

        for e in container2.values():
            list2.append(e)

        return list1 == list2


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
