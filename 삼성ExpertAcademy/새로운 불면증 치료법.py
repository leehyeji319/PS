# 최소 몇 번 양을 셌을 때 0~9까지 모든 수를 보는지?
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    ten_table = set()
    count = 0
    tmp_num = 0

    while True:
        count += 1
        tmp_num = N * count
        ten_table.update(str(tmp_num))
        if len(ten_table) == 10:
            break
    answer = tmp_num
    print(f"#{t} {answer}")

