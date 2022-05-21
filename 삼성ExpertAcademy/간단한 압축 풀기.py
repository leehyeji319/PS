T = int(input())
for t in range(1, T + 1):
    N = int(input())
    document = ""
    for n in range(1, N + 1):
        word, number = input().split()
        document += word * int(number)
    print(f"#{t}")
    for i in range(0, len(document), 10):
        print(document[i:i + 10])


