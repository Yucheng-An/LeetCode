class MyStack:

    def __init__(self):
        self.stackList = []

    def push(self, x: int) -> None:
        self.stackList.append(x)

    def pop(self) -> int:
        t = self.stackList.pop()
        return t
    def top(self) -> int:
        return self.stackList[-1]

    def empty(self) -> bool:
        if len(self.stackList) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()