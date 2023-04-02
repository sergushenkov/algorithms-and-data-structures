from typing import Any


class Stack:
    def __init__(self) -> None:
        self.stack: list = []

    def size(self) -> int:
        return len(self.stack)

    def pop(self) -> None | Any:
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def push(self, value: Any) -> None:
        self.stack.append(value)

    def peek(self) -> None | Any:
        if len(self.stack) > 0:
            return self.stack[-1]
        return None
