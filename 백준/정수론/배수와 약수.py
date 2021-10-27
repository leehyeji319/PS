a, b = map(int, input().split())

def solve(a, b):
    if b%a == 0: return "factor"
    elif a%b == 0: return "multiple"
    else: return "neither"

while a != 0 and b != 0:
    print(solve(a, b))
    a, b = map(int, input().split())