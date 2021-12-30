import sys
n = int(input())

score = list(map(int, sys.stdin.readline().split()))
m = max(score)
new_score = []
for i in score:
    new_score.append(float(i) / float(m) * 100)

print(float(sum(new_score)) / n)