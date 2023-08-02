

# 1208. Flatten

# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int,input().split()))

#     for idx in range(N):    # 1번 할때마다
#         max_value = arr[0]  # arr의 최댓값 초기 설정
#         min_value = arr[0]  # arr의 최솟값 초기 설정
#         idx_max = 0         # 최댓값의 인덱스 초기 설정
#         idx_min = 0         # 최솟값의 인덱스 초기 설정

#         for i in range(len(arr)):
#             if max_value < arr[i]:
#                 max_value = arr[i]
#                 idx_max = i             # 최댓값과 그때의 인덱스를 추출
#             else:
#                 continue

#         for j in range(len(arr)):
#             if min_value > arr[j]:
#                 min_value = arr[j]
#                 idx_min = j             # 최솟값과 그때의 인덱스를 추출
#             else:
#                 continue

#         arr[idx_max] -= 1               # 최댓값일 때의 arr의 인덱스로 가서 그 값을 -1
#         arr[idx_min] += 1               # 최솟값일 때의 arr의 인덱스로 가서 그 값을 +1

#     def Max_Min(my_arr):
#         my_max = 0
#         my_min = my_arr[0]
#         for i in range(len(my_arr)):
#             if my_max < my_arr[i]:
#                 my_max = my_arr[i]
#             else:
#                 continue
#         for j in range(len(my_arr)):
#             if my_min > my_arr[j]:
#                 my_min = my_arr[j]
#             else:
#                 continue

#         result = my_max - my_min      # 덤프가 모두 끝난 후 arr의 최댓값 및 최솟값의 차를 구함

#         return result



#     print(f'#{tc} {Max_Min(arr)}')



# 18053. 4834. 숫자카드

# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int,input().split()))
#
#     case = [0] * 10
#
#
#     for i in range(N):
#         remain = arr[0] % 10
#         arr[0] //= 10
#         case[remain] += 1
#         remain = 0
#
#     max_num = 0
#     idx_num = 0
#     for j in range(len(case)):
#         if max_num <= case[j]:
#             max_num = case[j]
#             idx_num = j
#
#     print(f'#{tc} {idx_num} {max_num}')



# 18058. 4831. 전기버스

# T = int(input())
# for tc in range(1,T+1):
#     K, N, M = map(int,input().split())
#     arr = list(map(int,input().split()))
    
#     print (K, N, M)


# N - my_max > K 









# 1945. 간단한 소인수분해

# 6485. 삼성시의 버스 노선

# 9386. 연속한 1의 개수

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input()))

#     num = 0
#     max_num = 0
#     for i in range(N):
#         if arr[i] == 1:
#             num += 1
#             if max_num < num:
#                 max_num = num
#         else:
#             num = 0

#     print(f'#{tc} {max_num}')


