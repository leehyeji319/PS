# def permutation(arr, N):
#     result = []
#
#     if N == 0:
#         return [[]]
#     for i in range(len(arr)):
#         elem = arr[i]
#
#         for rest in permutation(arr[:i] + arr[i + 1:], N - 1):
#             result.append([elem] + rest)
#     return result
#
# def combination(arr, N):
#     result = []
#
#     if N == 0:
#         return [[]]
#
#     for i in range(len(arr)):
#         elem = arr[i]
#
#         for rest in combination(arr[i+1:], N - 1):
#             result.append([elem] + rest)
#     return result
#
# N, R = map(int, input().split())
# numbers = list(map(int, input().split()))
#
# permutation_res = permutation(numbers, R)
# combination_res = combination(numbers, R)
#
# print(permutation_res)
# print(combination_res)

# # 부분조합
# N = int(input())
# numbers = list(map(int, input().split()))
#
# for flag in range(1 << N):
#     for i in range(N):
#         if (flag & 1 << i) != 0:
#             print(numbers[i], end=' ')
#     print()


# 넥퍼
def np(numbers):
    i, j, k = N - 1, N - 1, N - 1

    while i > 0 and numbers[i - 1] >= numbers[i]: i -= 1
    if i == 0: return False

    while numbers[i - 1] >= numbers[j]: j -= 1

    numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]

    while k > i:
        numbers[i], numbers[k] = numbers[k], numbers[i]
        i += 1; k -= 1
    return True

N = int(input())
numbers = sorted(list(map(int, input().split())))

while True:
    print(*numbers)
    if not np(numbers): break
