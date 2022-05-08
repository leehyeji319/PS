# 맨하탄 거리 = 수평거리 + 수직거리

def solution(line):
    answer = []
    keyboard = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']]
    left_keyboard = ['1', '2', '3', '4', '5', 'Q', 'W', 'E', 'R', 'T']
    left = 'Q'
    right = 'P'
    find_list = []
    for i in line:
        find_list.append(i)
    
    print(find_list)
    
    for x in range(len(find_list)):
        print(left)
        print(right)
        newlist=[(i,j) for i in range(2) for j in range(10) if keyboard[i][j]==find_list[x]]
        leftlist=[(i,j) for i in range(2) for j in range(10) if keyboard[i][j]==left]
        rightlist=[(i,j) for i in range(2) for j in range(10) if keyboard[i][j]==right]
        left_man = abs(newlist[0][0] - leftlist[0][0]) + abs(newlist[0][1] - leftlist[0][1])
        right_man = abs(newlist[0][0] - rightlist[0][0]) + abs(newlist[0][1] - rightlist[0][1])
        left_hori =  abs(newlist[0][1] - leftlist[0][1])
        right_hori = abs(newlist[0][1] - rightlist[0][1])
        
        if left_man < right_man:
            answer.append(0)
            left = find_list[x]
        elif left_man > right_man:
            answer.append(1)
            right = find_list[x]
        elif left_man == right_man:
            if left_hori > right_hori:
                answer.append(1)
                left = find_list[x]
            elif left_hori < right_hori:
                answer.append(0)
                right = find_list[x]
            elif left_hori == right_hori:
                if find_list[x] in left_keyboard:
                    answer.append(0)
                    left = find_list[x]
                else: 
                    answer.append(1)
                    right = find_list[x]
    
    return answer

print(solution("64E2"))
# 	[0,0,1,0,1,1]

# "Q4OYPI"	[0,0,1,0,1,1]
# "RYI76"	[0,0,1,1,0]
# "64E2"	[1,1,1,0]