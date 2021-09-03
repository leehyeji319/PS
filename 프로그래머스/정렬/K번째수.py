#https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
def solution(array, commands):
    answer = []
    
    for command in commands:
        arr = array[command[0] - 1:command[1]] #sorted 자체는 납두고 새로운 배열을 생성하고 정렬 후 반환, #sort 
        arr.sort()
        answer.append(arr[command[2] - 1])
    return answer