import sys
n, m = map(int, sys.stdin.readline().split())
s_arr = set([sys.stdin.readline().rstrip() for _ in range(n)])
h_arr = set([sys.stdin.readline().rstrip() for _ in range(m)])

answer = s_arr & h_arr
        
print(len(answer))
for i in sorted(answer):
    print(i)