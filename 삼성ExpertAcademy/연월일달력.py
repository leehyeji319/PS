T = int(input())
day_31 = [1, 3, 5, 8, 10, 12]
day_30 = [4, 6, 9, 11]
day_28 = [2]
for t in range(1, T + 1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    if int(month) in day_31 and int(day) <= 31:
        print(f"#{t} {year}/{month}/{day}")
    elif int(month) in day_30 and int(day) <= 30:
        print(f"#{t} {year}/{month}/{day}")
    elif int(month) in day_28 and int(day) <= 28:
        print(f"#{t} {year}/{month}/{day}")
    else:
        print(f"#{t} -1")