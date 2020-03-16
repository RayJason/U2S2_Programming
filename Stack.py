# coding=utf-8

class Stack:

    # 初始化栈
    def __init__(self, initSize):
        self.stack = []
        self.maxSize = initSize

    # 析构
    def __del__(self):
        del self.stack

    # 返回栈顶
    def top(self):
        return None if self.isEmpty() else self.stack[-1]

    # 压入
    def push(self, obj):
        self.stack.append(obj)

    # 弹出
    def pop(self):
        return None if self.isEmpty() else self.stack.pop()

    # 清空栈
    def clear(self):
        self.stack.clear()

    # 判断空栈 bool
    def isEmpty(self):
        return self.length() == 0

    # 返回长度
    def length(self):
        return len(self.stack)