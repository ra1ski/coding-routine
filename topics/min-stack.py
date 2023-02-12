class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        stack_sorted = sorted(self.stack)

        return stack_sorted[0]


s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)

print(s.getMin())
