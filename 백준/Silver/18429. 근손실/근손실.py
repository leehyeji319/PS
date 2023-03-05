from itertools import permutations

N, K = map(int, input().split())
machines = list(map(int ,input().split()))

answer = 0
for perm in permutations(machines):
    lis = list(perm)
    now_muscle = 500
    for i in range(N):
        if now_muscle - K + lis[i] < 500:
            break
        else:
            if i == N - 1:
                answer += 1
            now_muscle = now_muscle - K + lis[i]

print(answer)