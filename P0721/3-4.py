# 그리디 문제 
# 모험가 길드의 공포도 문제 


n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가 수

for i in data: #공포도를 낮은거부터 하나씩 확인하기
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i: #사람수가 공포도 보다 높으면
        result += 1 # 그룹결성
        count = 0 #현재 그룹에 포함된 모험가의 수 초기화
print(result) # 총 그룹의 수 출력

