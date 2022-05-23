T = 10
for t in range(1, T + 1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    while True:
        boxes.sort(reverse=True)
        boxes[-1] += 1
        boxes[0] -= 1
        dump -= 1
        if (max(boxes) - min(boxes)) <= 1:
            break
        if dump == 0:
            break
    answer = max(boxes) - min(boxes)
    print(f"#{t} {answer}")