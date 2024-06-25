from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            left = self.q.popleft()
            self.q.append(left)

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


def main():
    # declaration
    myStack = MyStack()

    # processing
    myStack.push(1)
    myStack.push(2)
    param_2 = myStack.top()
    param_3 = myStack.pop()
    param_4 = myStack.empty()

    # output
    print("\nResult:")
    print(f"top: {param_2}")
    print(f"pop: {param_3}")
    print("The stack now is", ("empty" if param_4 else "not empty"))


if __name__ == "__main__":
    main()
