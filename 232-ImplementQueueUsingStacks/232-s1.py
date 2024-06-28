class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0


def main():
    # declaration
    myQueue = MyQueue()

    # processing
    myQueue.push(1)
    myQueue.push(2)
    param_2 = myQueue.top()
    param_3 = myQueue.pop()
    param_4 = myQueue.empty()

    # output
    print("\nResult:")
    print(f"top: {param_2}")
    print(f"pop: {param_3}")
    print("The stack now is", ("empty" if param_4 else "not empty"))


if __name__ == "__main__":
    main()
