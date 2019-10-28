'''
algorithmName: matrixChain
author: Xu Mengnan
date: 2019/10/17
input: matrix chain
output: order of operations
'''


def matrixChain(p):
    #  n为矩阵个数
    n = len(p) - 1
    # 创建二维数组
    m = [[0]*(n+1) for i in range(n+1)]
    s = [[0]*(n+1) for i in range(n+1)]
    for i in range(1, n+1):
        m[i][i] = 0
    for r in range(2, n+1):
        for i in range(1, n-r+2):
            j = i + r - 1
            m[i][j] = m[i+1][j] + p[i-1] * p[i] * p[j]
            s[i][j] = i
            k = i + 1
            while k<j:
                t = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if t < m[i][j]:
                    m[i][j] = t
                    s[i][j] = k
                k += 1
    return s, m

def traceback(s, i, j):
    if i == j :
        print(f'A{i}',end='')
        return
    print("(", end='')
    traceback(s, i ,s[i][j])
    traceback(s, s[i][j]+1, j)
    print(f")",end='')

if __name__ == '__main__':
    amount = int(input('请输入矩阵的个数'))
    p = []
    temp = input("请输入第1个矩阵的行数以及第1到第{}个矩阵的列数，用逗号分开".format(amount))
    lis = temp.strip().split(',')
    for i in lis:
        p.append(int(i))
    s, m= matrixChain(p)
    traceback(s,1,amount)

# 30,35,15,5,10,20,25

