# coding=utf-8
# 栈和队列在python中的实现：https://www.cnblogs.com/yiduobaozhiblog1/p/9272556.html

# 21. 商品货架管理
# 【问题描述】
# 商品货架可以看成一个栈，栈顶商品的生产日期最早，栈底商品的生产日期最近。上货时，需要倒货架，以保证生产日期较近的商品在较下的位置。
# 【基本要求】
# 针对一种特定商品，实现上述管理过程。
# 【实现提示】
# 用两个栈模拟货架和周转空间。
# 【测试数据】
# 略，注意栈空和栈满的情况。

# 初始化栈


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


def Shelf():

    print("***********************\n")
    print("\n")
    print("*****商品货架管理系统*****\n")
    print("\n")
    print("***********************\n")
    print("\n")

    # 设置货架容量
    maxSize = int(input("请输入货架的容量："))

    # 初始化货架
    shelf = Stack(maxSize)

    # 初始化临时栈
    tempShelf = Stack(maxSize)

    print("货架的容量是：" + str(maxSize))

if __name__ == "__main__":
    Shelf()
