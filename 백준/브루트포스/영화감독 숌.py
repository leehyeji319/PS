n = int(input())
hell_num = 666
cnt = 0 

while True:
    if '666' in str(hell_num): # n번째 수에 '666'이 포함되어 있다면
        cnt += 1 # 카운트 증가
    if cnt == n:   # 카운트랑 n번째 수가 같다면
        print(hell_num) # hell숫자 출력
        break
    hell_num += 1 # 666이 포함된 숫자가 나올때까지 hellnum 1씩 증가
