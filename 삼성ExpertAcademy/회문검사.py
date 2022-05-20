T = int(input())
for t in range(1, T + 1):
    s = input()
    if s == s[::-1]:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")