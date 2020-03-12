# 04180812 古家顺 A21 语言：Python
# 用栈的思想（汉诺塔）：将M个苹果放入N个“瓶子”，有K种摆放方法。用递归法求解。

# M=7 N=3时的排列组合8种：
# 7 0 0
# 6 1 0
# 5 2 0
# 4 3 0

# 5 1 1
# 4 2 1
# 3 3 1

# 3 2 2


def func(M, N):
    # 当苹果的数量为0或盘子的数量为1时，只有一种情况返回1
    if M == 0 or N == 1:
        return 1
    # 当苹果的数量小于盘子的数量时，排列种数即func(M,M) (被摆上的盘子数不超过苹果数)
    if M < N:
        return func(M, M)
    else:
        # M个苹果在N-1个盘（至少一个空盘）的种数 + 非空盘的种数（满足条件二不重复）
        return func(M, N-1) + func(M-N, N)


t = int(input("请输入测试数据的数目:\n"))
a = []  # 存放排列种数K
print("请输入苹果和盘子的数量:")  # 苹果的数量M，盘子的数量N
for i in range(t):
    M, N = map(int, input().split())
    a.append(func(M, N))

print(*a)  # 打印结果
