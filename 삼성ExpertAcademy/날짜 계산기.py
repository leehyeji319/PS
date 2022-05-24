T = int(input())
day_30 = [4, 6, 9, 11]
day_31 = [1, 3, 5, 7, 8, 10, 12]
day_28 = [2]
for t in range(1, T + 1):
    month1, day1, month2, day2 = map(int,input().split())
    period_month = [n for n in range(month1, month2)]
    days = 0
    for pm in period_month:
        if pm in day_30:
            days += 30
        if pm in day_31:
            days += 31
        if pm in day_28:
            days += 28
    answer = days - day1 + day2 + 1
    print(f"#{t} {answer}")