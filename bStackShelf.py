# coding=utf-8
# 参考文章
# 栈和队列在python中的实现：https://www.cnblogs.com/yiduobaozhiblog1/p/9272556.html
# Python数据结构篇（一）—— 顺序栈和链栈的实现 https://blog.csdn.net/jackandsnow/article/details/101390919

# 21. 商品货架管理
# 【问题描述】
# 商品货架可以看成一个栈，栈顶商品的生产日期最早，栈底商品的生产日期最近。上货时，需要倒货架，以保证生产日期较近的商品在较下的位置。
# 【基本要求】
# 针对一种特定商品，实现上述管理过程。
# 【实现提示】
# 用两个栈模拟货架和周转空间。
# 【测试数据】
# 略，注意栈空和栈满的情况。

# 数据结构：栈


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


# 设置货架
def Shelf():
    # 设置货架容量
    maxSize = int(input("请输入货架的容量："))
    # 初始化货架
    shelf = Stack(maxSize)
    # 初始化临时栈
    tempShelf = Stack(maxSize)
    print("货架的容量是：" + str(maxSize))

    # 菜单
    def show():
        cls()
        print("***********************\n")
        print("*****商品货架管理系统*****\n")
        print("***********************\n")
        print("*******1.存入货物*******\n")
        print("*******2.取出货物*******\n")
        print("*******3.查看货架*******\n")
        print("*******4.退出系统*******\n")
        print("***********************\n")

    # 进货
    def purchase():
        def purchaseTitle():
            cls()
            print("***********************\n")
            print("********  进货  ********\n")
            print("***********************\n")

        purchaseTitle()
        purchaseNumber = int(input("请输入进货的数量："))
        while not (purchaseNumber <= shelf.maxSize - shelf.length()):
            purchaseTitle()
            purchaseNumber = int(
                input("没有那么多位置啦～最多只有" + str(shelf.maxSize - shelf.length()) + "个货位。请重新输入："))

        print("请依次输入" + str(purchaseNumber) + "个商品的生产日期，格式<20200315>：")

        while purchaseNumber:
            Date = int(input())
            # 倒货
            while not (shelf.isEmpty()):
                # 生产日期近的在下
                if shelf.top() < Date:
                    temp = shelf.pop()
                    tempShelf.push(temp)
                else:
                    break

            shelf.push(Date)

            while not (tempShelf.isEmpty()):
                temp = tempShelf.pop()
                shelf.push(temp)
            purchaseNumber -= 1

        print("\n商品入货完毕")

    # 出货
    def sold():
        def soldTitle():
            cls()
            print("***********************\n")
            print("********  出货  ********\n")
            print("***********************\n")

        soldTitle()
        soldNumber = int(input("请输入出货的数量："))
        while True:
            if (soldNumber < 0):
                soldTitle()
                soldNumber = int(input("输入负数也不会多给你哒，请重新输入："))
            elif (soldNumber > shelf.length()):
                soldTitle()
                soldNumber = int(input("货架上没有那么多啦～请重新输入："))
            else:
                break
        while soldNumber:
            shelf.pop()
            soldNumber -= 1
        soldTitle()
        print("\n商品出货完毕")

    # 货柜状态
    def status():
        def statusTitle():
            cls()
            print("***********************\n")
            print("********货架状态********\n")
            print("***********************\n")

        statusTitle()
        if (shelf.isEmpty()):
            print("当前货架为空，请快点进货噢！")
        else:
            print("货柜容量：" + str(maxSize))
            print("货柜剩余容量：" + str(maxSize - shelf.length()))
            print("货架顶部商品的生产日期：" + str(shelf.top()))
            print("货架剩余商品由底到顶的生产日期：")
            for i in shelf.stack:
                print(i, end=" ")

    # 伪清屏
    def cls():
        print("\n"*10)

    while True:
        show()
        select = int(input("请选择功能："))
        if (select == 1):
            purchase()
        elif(select == 2):
            sold()
        elif(select == 3):
            status()
        elif(select == 4):
            break
        else:
            print("输入错误请重新输入")

        input("\n请输入回车继续")


if __name__ == "__main__":
    Shelf()
