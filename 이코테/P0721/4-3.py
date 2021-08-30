#왕실의 나이트 문제
#현재 나이트의 위치 입력받기
#2차원 리스트 2차원 배열을 사용하는 전형적인 문제
input_data = input()
row = int(input_data[1])
#ord 아스키 코드형태의 값으로 바꾸는것 
column = int(ord(input_data[0])) - int(ord('a')) + 1

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 2)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    #해당 위치로 이동이 가능한가 확인
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)