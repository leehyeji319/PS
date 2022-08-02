N = int(input())
status = list(map(int, input().split()))
for s in range(int(input())):
    sex, number = map(int, input().split())
    l = len(status)
    
    if sex == 1:
        idx = 1
        while True:
            new_idx = number * idx - 1
            
            if new_idx >= l:
                break
            if status[new_idx] == 1: 
                status[new_idx] = 0
            else: 
                status[new_idx] = 1
            idx += 1
            
    else: 
        idx = 1
        number -= 1
        while True:
            left = number - idx
            right = number + idx
            if number == 0 or number == len(status) - 1:
               break
               
            if ((left) < 0 or (right) >= len(status)):
                break
            
            if status[left] != status[right]:
                break
            else:
                if status[left] == 0: 
                    status[left] = 1
                    status[right] = 1
                else: 
                    status[left] = 0
                    status[right] = 0
            idx += 1
        if status[number] == 0:
            status[number] = 1
        else: status[number] = 0
            
for i in range(0, N, 20):
    print(*status[i:i+20])