'''
algorithmName: 01 bag
author: Xu Mengnan
date: 2019/10/21
input: Backpack capacity, Item weight sequence, Item value sequence
output: The selected item number, the total weight of the item, and the total value of the item
'''


def knaosack(v, w, c):
    n = len(v) # 物品数量
    m = [[0]*(c+1) for i in range(n+1)] # n行c列的数组
    for i in range(1, n+1):
        for j in range(1, c+1):
            m[i][j] = m[i-1][j]
            if j >= w[i-1] and m[i][j] <= m[i-1][j-w[i-1]] + v[i-1]:
                m[i][j] = m[i-1][j-w[i-1]] + v[i-1]
    return m





def traceback(m, w, c):
    n = len(w) - 1
    x = [0] * (n+1)
    for i in range(n):
        if m[i][c] == m[i+1][c]:
            x[i] = 0
        else:
            x[i] = 1
            c -= w[i]
    if m[n][c] > 0:
        x[n] = 1
    else:
        x[n] = 0
    return x

if __name__ == '__main__':
    c = int(input("输入背包容量"))
    v = []
    w = []
    temp = input('输入商品价格(整数)，中间用空格分开').strip().split(' ')
    for i in temp:
        v.append(int(i))
    temp = input('输入商品重量，中间用空格分开').strip().split(' ')
    for i in temp:
        w.append(int(i))
    m = knaosack(v, w, c)
    for i in m:
        print(i)
    x = traceback(m, w, c)
    choose_price = []
    choose_weight = []
    print("选择了",end='')
    for i in range(len(v)):
        if x[i] == 1:
            print(i,end=' ')
            choose_price.append(v[i])
            choose_weight.append(w[i])
    print('号商品')
    print('总价格为{}'.format(sum(choose_price)))
    print('总重量为{}'.format(sum(choose_weight)))

    # 1 4 5 13 2 4
    # 2 3 4 20 4 6