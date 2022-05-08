# 미세먼지 30이하 좋음 80이하 보통 150이하 나쁨 151이상 매우나쁨
# 초미세 15이하 좋음 35이하 보통 75이하 나쁨 76이상 매우나쁨 
# 1. 하나라도 나쁘면 마스크 착용 
# 2. 착용하면 이틀 후 무조건 폐기
# 3. 만일 둘다 매우나쁨 날이라면 그날 마스크는 폐기

def find_dust_density(d):
    if d <= 80:
        return 0
    elif 80 < d <= 150:
        return 1
    else: return 2
    
def find_udust_density(ud):
    if ud <= 35:
        return 0
    elif 35 < ud <= 75:
        return 1
    else: return 2
    
def solution(atmos):
    answer = 0 #마스크 개수
    day = -1 #마스크를 쓰기 시작한 날짜 세기
    for i in range(len(atmos)):
        d = atmos[i][0]
        ud = atmos[i][1]
        if day == 2:
            answer += 1
            day = -1
        if 0 < find_dust_density(d) + find_udust_density(ud) <= 3:
            day += 1
        elif find_dust_density(d) + find_udust_density(ud) == 0 and day > -1:
            day += 1
        elif find_dust_density(d) + find_udust_density(ud) >= 4:
            answer += 1
            day = -1
    
    if day != -1:
        answer +=1
        
    return answer

print(solution([[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]))