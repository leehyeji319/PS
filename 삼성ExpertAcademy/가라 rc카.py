# 0현재 속도 유지, 1가속, 2감속
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    distance = 0
    now_speed = 0

    for i in range(N):
        commands = list(map(int, input().split()))
        if len(commands) == 1:
            command = 0
        else:
            command = commands[0]
            acceleration = commands[1]

        if command == 1:
            now_speed += acceleration
            distance += now_speed
        elif command == 2:
            now_speed -= acceleration
            if now_speed < 0: now_speed = 0
            distance += now_speed
        else:
            distance += now_speed
    print(f"#{t} {distance}")
