now_location = input()
row = int(now_location[1]) # 행 숫자로 
column = int(ord(now_location[0])) - int(ord('a')) + 1 # 열을 유니코드 값으로 바꾼후 숫자로 변환

# 나이트가 이동할 수 있는 경우 의 수 
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (-1, 2)]

answer = 0
for step in steps:
    # 이동하고자 하는 위치
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동 가능하다면 answer 증가
    if next_row <= 8 and next_row >= 1 and next_column <= 8 and next_column >= 1:
        answer += 1

print(answer)