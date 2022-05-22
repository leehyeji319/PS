T = int(input())
for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    a_company = W * P
    b_company = Q
    answer = 0
    if W > R:
        b_company += (W - R) * S
    if a_company > b_company:
        answer = b_company
    else: answer = a_company
    print(f"#{t} {answer}")