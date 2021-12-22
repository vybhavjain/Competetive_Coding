# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, K):
    # write your code in Python 3.6
    one_digit = N % 10
    ten_digit = ( N % 100 ) // 10
    hundred_digit = N //100

    while hundred_digit != 9 and K != 0:
        hundred_digit = hundred_digit + 1
        K = K - 1
    while ten_digit != 9 and K != 0:
        ten_digit = ten_digit + 1
        K = K - 1
    while one_digit != 9 and K != 0:
        one_digit = one_digit + 1
        K = K - 1
    final_num = 100*hundred_digit + 10*ten_digit + one_digit

    return final_num
    pass