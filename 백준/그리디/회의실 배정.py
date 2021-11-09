# 1931번
n = int(input())
meetings = []
for _ in range(n):
    a, b = map(int, input().split())
    meetings.append((a, b))
meetings.sort(key=lambda x: (x[1], x[0]))
# 0번째 인덱스에 대해 오름차순, 동일하 값의 경우 내림차순

cnt = 1
end_time = meetings[0][1]
for i in range(1, n):
    if meetings[i][0] >= end_time:
        cnt += 1
        end_time = meetings[i][1]
print(cnt)