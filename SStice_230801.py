

# 11092. 최대 최소의 간격

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     min_idx = 0  # 최솟값의 인덱스
#     max_idx = 0  # 최대값의 인덱스
#
#     for i in range(1, N):
#         if arr[min_idx] > arr[i]:
#             min_idx = i
#         if arr[max_idx] <= arr[i]:
#             max_idx = i
#
#     ans = abs(max_idx - min_idx)
#
#
#     print(f'#{tc} {ans}')



# 9386. 연속한 1의 개수

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input()))

#     box = [0] * 2
#     num = 0
#     for i in range(N):
#         if arr[i] == 1:
#             box[0] += 1
#             num = box[0]
#         else:
#             box[0] = 0

#     print(f'#{tc} {num}')



# list = [3, 5, 7 ,8]

# list[0] = list[0] - 1
# print(list)

# for i in range(9,0,-1):
#     print(i)