# 2884 단계별로 풀어보기 if문
H, M = map(int, input().split())

if M >= 45:
    M -= 45
else:
    H -= 1
    M += 15 

if H < 0:
    H += 24

print(H, M)


# 백준 단계별