def solution(picks, minerals):
    answer = 0
    # 캘 수 있는 광물의 수
    if len(minerals) > sum(picks) * 5:
        minerals = minerals[:sum(picks) * 5]

    
    cnt_minerals = [[0, 0, 0]for x in range(10)]

    print(cnt_minerals)

    for i in range(len(minerals)):
        if minerals[i] == 'diamond': 
            cnt_minerals[i//5][0] += 1
        elif minerals[i] == 'iron': 
            cnt_minerals[i//5][1] += 1
        else : 
            cnt_minerals[i//5][2] += 1
            

    print(cnt_minerals)

    sorted_cnt_minerals = sorted(cnt_minerals, key = lambda x: (-x[0], -x[1], -x[2]))


    print(sorted_cnt_minerals)

    for mineral in sorted_cnt_minerals:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p]>0: # dia 곡괭이
                picks[p]-=1
                answer += d + i + s
                break
            elif p == 1 and picks[p]>0: # iron 곡괭이
                picks[p]-=1
                answer += 5*d + i + s
                break
            elif p == 2 and picks[p]>0: # stone 곡괭이
                picks[p]-=1
                answer += 25*d + 5*i + s
                break



    return answer

# print(solution([1, 3, 2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
print(solution([0, 1, 1], ["iron", "iron", "iron", "iron", "iron", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"]))