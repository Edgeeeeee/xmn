'''
algorithmName: 01 bag
author: Xu Mengnan
date: 2019/10/21
input: Backpack capacity, Item weight sequence, Item value sequence
output: The selected item number, the total weight of the item, and the total value of the item
'''
def bag(w, v, c):
    p = {}
    q = {}
    n = len(w)
    for i in range(1, n+2):
        p[i] = []
        q[i] = []
    p[n+1].append((0,0))
    for a,b in p[n+1]:
        if a + w[n - 1] <= c:
            q[n+1].append((a+w[n-1], b+v[n-1]))

    for i in range(n, 0, -1):
        # 取并集
        for item in p[i+1]:
            p[i].append(item)
        for item in q[i+1]:
            p[i].append(item)
        # 消除
        p[i].sort(key=lambda x :x[0])

        templen = len(p[i])-1
        templist = []
        for n in range(templen):
            if p[i][n][0] == p[i][n+1][0]:
                templist.append(p[i][n])
        for item in templist:
            p[i].remove(item)

        templen = len(p[i])-1
        templist = []
        for n in range(templen):
            if p[i][n][1] >= p[i][n+1][1]:
                templist.append(p[i][n+1])

        for item in templist:
            p[i].remove(item)

        p[i].sort(key=lambda x: x[1])
        templen = len(p[i])-1
        templist = []
        for n in range(templen):
            if p[i][n][0] >= p[i][n+1][0]:
                templist.append(p[i][n])

        for item in templist:
            p[i].remove(item)

        p[i].sort(key=lambda x: x[0])


        for a, b in p[i]:
            if a + w[i-2] <= c:
                q[i].append((a + w[i-2], b + v[i-2]))

    return p[1][-1]





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
    #
    # c = 10
    # v = [6, 3, 5, 4, 6]
    # w = [2, 2, 6, 5, 4]
    _, b = bag(w, v, c)
    print(f'最大价值为{b}')