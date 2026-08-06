import sys

class MinStack:
    st_top = -1
    st_list = []

    def __init__(self):
        self.st_top = -1
        self.st_list = []

    def push(self, val: int) -> None:
        min_top = 0
        if self.st_top == -1:
            min_top = pow(2, 31) - 1
        else:
            min_top = self.getMin()

        self.st_top += 1

        min_top = min(min_top, val)
        self.st_list.insert(self.st_top, (val, min_top))

    def pop(self) -> None:
        self.st_top -= 1        

    def top(self) -> int:
        val, min_top = self.st_list[self.st_top]
        return val

    def getMin(self) -> int:
        val, min_top = self.st_list[self.st_top]
        return min_top
        
