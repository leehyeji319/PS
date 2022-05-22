T = int(input())

for t in range(1, T + 1):
    hours_1, minutes_1, hours_2, minutes_2 = map(int, input().split())
    answer_hours = hours_1 + hours_2
    answer_minutes = minutes_1 + minutes_2

    if answer_minutes > 60:
        answer_minutes -= 60
        answer_hours += 1

    if answer_hours % 12 == 0:
        answer_hours = 12
    else:
        answer_hours %= 12

    print(f"#{t} {answer_hours} {answer_minutes}")
