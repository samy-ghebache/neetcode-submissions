class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_values[-1] if self.min_values else val)
        self.min_values.append(val)

    def pop(self) -> None:
        self.stack.pop()
        if self.min_values:
            self.min_values.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]