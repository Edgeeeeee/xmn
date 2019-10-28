'''
algorithmName: Marge Sort
author: Xu Mengnan
input: unordered array
output: ordered array
date: 2019/10/14
'''
import sys
import json
def merge(arr1, arr2):
    i = j =0
    arr = list()
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
           arr.append(arr1[i])
           i = i + 1
        else:
            arr.append(arr2[j])
            j = j + 1
    if i >= len(arr1):
        for k in range(j,len(arr2)):
            arr.append(arr2[k])
    if j >= len(arr2):
        for k in range(i,len(arr1)):
            arr.append(arr1[k])
    return arr

def mergeSort(arr):
    mid = len(arr)//2
    if len(arr) > 1:
        temp1, temp2 = [], []
        for i in range(0,mid):
            temp1.append(arr[i])
        for i in range(mid,len(arr)):
            temp2.append(arr[i])
        arr1 = mergeSort(temp1)
        arr2 = mergeSort(temp2)
        sortarr = merge(arr1,arr2)
        return sortarr
    else:
        return arr

if __name__ == '__main__':
    temp = input("请输入整数序列，以逗号分隔:")
    a = temp.split(',')
    arr = []
    # 格式转换
    for i in a:
        try:
            arr.append(int(i))
        except Exception as e:
            print("InputError: '{}'".format(i))
            sys.exit()
    print(json.dumps(mergeSort(arr))[1:-1])

