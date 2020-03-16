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

import bShelf

if __name__ == "__main__":
    bShelf.Shelf()
