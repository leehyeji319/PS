
# str_arr = input()
# boom_arr = input()
# while boom_arr in str_arr:
#     str_arr = str_arr.replace(boom_arr, "")
# if len(str_arr) == 0:
#     print("FRULA")
# else:
#     print(str_arr)

# from collections import deque

str_arr = input()
boom_arr = input()
# stack = deque([])
stack = []
for i in range(len(str_arr)):
    stack.append(str_arr[i])
    while boom_arr in ''.join(stack[-len(boom_arr):]):
        for _ in range(len(boom_arr)):
            stack.pop()
if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))