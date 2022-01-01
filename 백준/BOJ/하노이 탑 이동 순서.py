# 재귀 알고리즘 
# 일반적으로 원판이 n개 일 때, 2n - 1번의 이동으로 원판을 모두 옮길 수 있다(2n - 1는 메르센 수)
n = int(input())

def hanoi(n, from_pos, to_pos, aux_pos): #출발점 기둥, 도착점 기둥, 보조 기둥
    if n == 1:
        print(from_pos, to_pos)
    else: #recursive
        # 원판 n-1개를 from 에서 aux로 옮긴다 (to를 보조기둥으로)
        hanoi(n - 1, from_pos, aux_pos, to_pos)
        # n번째 원판 = 제일 밑에 있는 원판을 목적지 to로 이동
        print(from_pos, to_pos)
        # aux에 있는 원반 n-1개를 목적지to로 이동 (from을 보조기둥으로)
        hanoi(n - 1, aux_pos, to_pos, from_pos)

sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 3, 2)