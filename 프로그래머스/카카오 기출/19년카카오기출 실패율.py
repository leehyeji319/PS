# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
def solution(N, stages):
    answer = []
    stages.sort()
    total_user = len(stages)
    fail = {}
    for stage in range(1, N + 1):
        #실패율 구하기
        if total_user != 0:
            fail_user = stages.count(stage)
            #딕셔너리를 이용하여 값에 실패율 넣는다
            fail[stage] = fail_user/total_user 
            total_user -= fail_user
        else:
            fail[stage] = 0 #0이 나올경우
    
    #딕셔너리의 값에 있는 실패율을 내림차순 정렬한 다음 키 값을 반환한다.
    return sorted(fail, key=lambda x : fail[x], reverse=True)
