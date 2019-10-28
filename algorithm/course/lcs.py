'''
algorithmName: Longest common subsequence
author: Xu Mengnan
date: 2019/10/17
input: two sequences
output: longest common subsequence
'''

def lcsLengeh(x, y):
    m = len(x) - 1
    n = len(y) - 1
    c = [[0]*(n+1) for i in range(m+1)]
    b = [[0]*(n+1) for i in range(m+1)]
    for i in range(m):
        c[i][0] = 0
    for i in range(n):
        c[0][i] = 0
    for i in range(m+1):
        for j in range(n+1):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 3

    return c[m][n], b

def lcs(i, j, x, b):
    if i == 0 or j == 0:
        return
    if b[i-1][j-1] == 1:
        lcs(i-1, j-1, x, b)
        print(x[i-1], end=' ')
    elif b[i-1][j-1] == 2:
        lcs(i-1, j, x, b)
    else:
        lcs(i, j-1, x, b)

if __name__ == '__main__':
    seq1 = input("请输入第一个序列，中间用逗号分开：").strip().split(",")
    seq2 = input("请输入第二个序列，中间用逗号分开：").strip().split(",")
    length, b = lcsLengeh(seq1, seq2)
    print(f"子序列长度为{length}")
    lcs(len(seq1), len(seq2), seq1, b)  # 前两个参数表示序列中的第几个字符，取len则表示最后一个。

# a,b,c,b,d,a,b
# b,d,c,a,b,a