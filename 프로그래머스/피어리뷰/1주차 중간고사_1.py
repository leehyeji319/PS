import math

# 시간을 분으로 바꿔주는 함수 작성
def timeToMinutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def solution(booked, unbooked):
    answer = []
    # 시각 포맷 분으로 다 바꿔주기
    for b in booked:
        b[0] = timeToMinutes(b[0])
    for ub in unbooked:
        ub[0] = timeToMinutes(ub[0])
    # 분을 기준으로 sort
    booked.sort(key=lambda x: x[0])
    unbooked.sort(key=lambda x: x[0])
    
    #첫번째로 일찍 온사람 먼저 찾아주기
    if booked[0][0] < unbooked[0][0]: # 예약한 사람이 먼저 왔다면
        answer.append(booked[0][1]) # 답에 넣어주고 해당 사람 삭제
        tmp = booked[0][0] + 10 # tmp에 상담이끝난 시간을 저장
        del booked[0]
    else: # 예약안한사람이 먼저 왔다면 
        answer.append(unbooked[0][1]) # 답에 넣어주고 해당 사람 삭제
        tmp = unbooked[0][0] + 10 # tmp에 상담 끝난 시간 저장
        del unbooked[0]
        
            
    while True: 
        if tmp >= booked[0][0]: # 상담 끝난 시각보다 일찍온 예약한 사람이 있다면
            answer.append(booked[0][1]) # 답에 넣어주고 삭제
            tmp = booked[0][0] + 10 # 상담 끝난시간 저장
            del booked[0]
            
        elif tmp >= unbooked[0][0]: # 상담 끝난 시각보다 일찍오고 예약한사람이 없다면
            answer.append(unbooked[0][1]) # 답에 넣어주고 삭제
            tmp = unbooked[0][0] + 10 # 상담 끝난 시간 저장
            del unbooked[0]

        else: # 상담 끝난시각보다 다들 늦게 왔다면, 다시 예약한 사람이랑 안한사람중에 먼저 온사람 찾기
            if booked[0][0] < unbooked[0][0]: 
                answer.append(booked[0][1])
                tmp = booked[0][0] + 10
                del booked[0]
            else:
                answer.append(unbooked[0][1])
                tmp = unbooked[0][0] + 10
                del unbooked[0]
        # 만약 예약자나 예약안한사람이 다 끝났다면 남은 사람들 answer에 넣어주고 break문으로 빠져나가기        
        if len(booked) == 0:
            for i in unbooked:
                answer.append(i[1])
            break
        elif len(unbooked) == 0:
            for i in booked:
                answer.append(i[1])
            break
        
        
    return answer


print(solution([["09:55", "hae"], ["10:05", "jee"]], [["10:04", "hee"], ["14:07", "eom"]]))