T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    if N == 1:
        print(f"#{t} 0")
        continue
    odd_cnt = 0
    even_cnt = 0
    stack = []
    answer = 0
    for a in arr:
        if a % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    if abs(odd_cnt - even_cnt) >= 2:
        print(f"#{t} -1")
        continue

    for i in range(len(arr)):
        idx = 0
        # 스택에 아무것도 없을 때
        if len(stack) == 0:
            stack.append(arr[i])
        # 스택에 하나 이상 존재 할때 비교하기
        elif len(stack) > 0:
            # 만일 스택에 있는거랑 홀짝 다르다면
            if arr[i] % 2 != stack[-1] % 2:
                # 스택에 넣어주기
                stack.append(arr[i])
            # 스택마지막원소랑 홀짝 같다면
            else:
                # 다른게 나올때까지 인덱스 더해주기
                while True:
                    if i + idx == len(arr):
                        break
                    elif stack[-1] % 2 == arr[i + idx] % 2:
                        idx += 1
                    elif stack[-1] % 2 != arr[i + idx] % 2 and (i + idx) < len(arr):
                        arr[i], arr[i + idx] = arr[i + idx], arr[i]  # 스와프
                        stack = []
                        answer += idx
                        idx = 0
                        break
                    else:
                        print(f"#{t} -1")
        elif len(stack) == len(arr):
            break


    print(f"#{t} {answer}")
