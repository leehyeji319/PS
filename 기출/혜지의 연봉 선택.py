# 롯정
def solution(list):   
    arr = []
    for ls in list: # ls = ["10/15 11/6 3000"]
        tmp = ls[0].split() # tmp = ["10/15", "11/6", "3000"]
        for i in range(2):
            tmp[i] = tmp[i].split('/') # tmp[0] = "10/15" -> tmp[0] = ["10", "15"]
            tmp[i] = int(tmp[i][0]) * 100 + int(tmp[i][1]) # tmp[0] = int("10") * 100 + int("15")= 1015
        tmp[2] = int(tmp[2])
        # tmp = [1015, 1106, 3000]
        arr.append(tmp)
    # arr = [[1015, 1106, 3000], [1015, 1107, 3000], [307, 319, 10000]]
    arr.sort(key = lambda x:(x[0], -x[2], -x[1])) # x=[1015,1106,3000] / [1015, 1107, 3000] / [307, 319, 10000]
    # arr = [[1015, 1106, 3000], [1015, 1107, 3000], [307, 319, 10000]]
    answer = arr[0]
    # for i in range(1, len(arr)):
    #     if answer[2] < arr[i][2]:
    #         answer = arr[i]
    for sol in arr[1:]:
        if answer[2] < sol[2]:
            answer = sol
    print(answer)
    return answer[2]

solution([["10/15 11/6 3000"], ["2/2 2/3 3000"], ["3/7 3/19 10000"]])

# 롯정 이번