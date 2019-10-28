# python3
# find max crossing subarray
def f_m_c_s(A, low, mid, high, limit):
    left_sum = float('-inf')
    right_sum = float('-inf')
    temp_sum = 0

    for i in range(mid, low - 1, -1):
        temp_sum = temp_sum + A[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left = i
    temp_sum = 0
    for i in range(mid + 1, high + 1):
        temp_sum = temp_sum + A[i]
        if temp_sum > right_sum:
            right_sum = temp_sum
            max_right = i
    return max_left, max_right, left_sum + right_sum


# find maxmum subarray
def f_m_s(A, low, high, limit):
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = f_m_s(A, low, mid, limit)
        right_low, right_high, right_sum = f_m_s(A, mid + 1, high, limit)
        cross_low, cross_high, cross_sum = f_m_c_s(A, low, mid, high, limit)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum






if __name__ == '__main__':
    A = [-1, 2, 3, -4, 7, 6, 3, -1, 2, 3]
    print(f_m_s(A, 0, len(A) - 1))


