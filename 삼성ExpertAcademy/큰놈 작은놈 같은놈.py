T = int(input())
for t in range(1, T + 1):
    num1, num2 = map(int, input().split())
    if num1 > num2:
        print(f"#{t} >")
    elif num1 < num2:
        print(f"#{t} <")
    else:
        print(f"#{t} =")
