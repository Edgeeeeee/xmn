'''
AlgorithmName: Cpair
Author: Xu Mengnan
date: 2019/10/14
Input: the amount of point and point coordinate.
Output: the closest two points and distance
'''
from math import sqrt
import sys

class Point():
    def __init__(self, xx, yy, pp):
        self.x = xx
        self.y = yy
        self.p = pp

class Pair():
    def __init__(self, aa, bb, dd):
        self.a = aa
        self.b = bb
        self.dis = dd

def getDis(a, b):
    return sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

def cpair2(pointList):
    if len(pointList) < 2:
        return None
    orderPointList_x = sorted(pointList, key=lambda a: a.x)
    orderPointList_y = sorted(pointList, key=lambda a: a.y)
    return clostestPair(pointList, orderPointList_x, orderPointList_y, 0, len(pointList)-1)

def clostestPair(orderPointList_x, orderPointList_y, l, r):
    # 两个点的情况
    if r-1 == 0:
        return Pair(orderPointList_x[l], orderPointList_x[r], getDis(orderPointList_x[l], orderPointList_x[r]))
    # 三个点的情况
    if r-1 == 1:
        d1 = getDis(orderPointList_x[l], orderPointList_x[l+1])
        d2 = getDis(orderPointList_x[l+1], orderPointList_x[r])
        d3 = getDis(orderPointList_x[l], orderPointList_x[r])
        if d1 < d2 and d1 < d3:
            return Pair(orderPointList_x[l], orderPointList_x[l+1], d1)
        elif d2 < d3:
            return Pair(orderPointList_x[l+1], orderPointList_x[r], d2)
        else:
            return Pair(orderPointList_x[l], orderPointList_x[r], d3)
    # 多于三个点的情况 用分治法。
    m = (l+r) // 2
    z_left, z_right = [], []
    for i in range(l, r+1):
        if orderPointList_y[i].p > m:
            z_left.append(orderPointList_y[i])
        else:
            z_right.append(orderPointList_y[i])
        z = z_left + z_right

    best = clostestPair(orderPointList_x, z, l, m)
    right = clostestPair(orderPointList_x, z, m+1, r)
    if(right.dis<best.dis):
        best = right
    orderPointList_y = sorted(z, key=lambda a: a.y)

    k = l
    for i in range(l,r+1):
        if abs(orderPointList_x[m].x - orderPointList_y[i].x) < best.dis:
            z.append(orderPointList_y[i])
            k += 1

    for i in range(l, k+1):
        j = i + 1
        while j < k and z[j].y - z[i].y < best.dis:
            dp = getDis(z[i], z[j])
            if dp < best.dis:
                best = Pair(orderPointList_x[z[i].p], orderPointList_x[z[j].p], dp)
                j += 1

    return best



if __name__ == '__main__':
    pointList = []
    amount = int(input("输入点的数量"))
    if amount < 2:
        print(float("inf"))
        sys.exit()
    for i in range(amount):
        temp = input("请输入第{}个点的x，y坐标".format(i))
        x,y = temp.strip(' ').split(" ")
        a = Point(int(x),int(y),i)
        pointList.append(a)
    orderedPointList_x = sorted(pointList, key=lambda a: a.x)
    orderedPointList_y = sorted(pointList, key=lambda a: a.y)
    l = 0
    r = amount - 1
    best = clostestPair(orderedPointList_x, orderedPointList_y, l, r)
    print("({},{})".format(best.a.x, best.a.y))
    print("({},{})".format(best.b.x, best.b.y))
    print(best.dis)







