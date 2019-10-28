'''
algorithmName: Convex polygon triangulation
author: Xu Mengnan
date: 2019/10/17
input: point dict
output: Minimum triangulation of weights
'''
from math import sqrt
class Point():
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

def getDis(pointA, pointB):
    return sqrt((pointA.x - pointB.x)**2 + (pointA.y - pointB.y)**2)

def weight(pointA, pointB, pointC):
    return getDis(pointB, pointC) + getDis(pointA, pointB) + getDis(pointA, pointC)

def minWeightTriangulation(p):
    n = len(p) - 1
    # 定义t[i][j]为凸子多边形vi，vi+1,...,vj的最优三角剖分的权函数值
    t = [[0]*(n+1) for i in range(n+1)]
    s = [[0]*(n+1) for i in range(n+1)]
    for i in range(1, n+1):
        t[i][i] = 0
    for r in range(2, n+1):
        for i in range(1, n-r+2):
            j = i + r - 1
            t[i][j] = t[i+1][j] + weight(p[i-1], p[i], p[j])
            s[i][j] = i
            k = i + 1
            while k < j:

                u = t[i][k] + t[k+1][j] + weight(p[i-1], p[k], p[j])
                if u < t[i][j]:
                    t[i][j] = u
                    s[i][j] = k
                k += 1
    return s, t

def traceback(s, i, j):
    if i == j :
        print(f'A{i}',end='')
        return
    print("(", end='')
    traceback(s, i ,s[i][j])
    traceback(s, s[i][j]+1, j)
    print(f")",end='')

if __name__ == '__main__':
    amount = int(input('请输入点的个数：'))
    p = []
    for i in range(amount):
        x, y = input(f"请输入第{i+1}个点的坐标：").strip().split(' ')
        print(x,y)
        tempPoint = Point(int(x), int(y))
        p.append(tempPoint)

    s, t= minWeightTriangulation(p)
    traceback(s,0,amount-1)