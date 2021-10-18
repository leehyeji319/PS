# https://www.acmicpc.net/problem/1316
n = int(input())
error = 0
for i in range(n):
    word=input()
    for j in range(len(word) - 1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            error += 1
            break
print(n - error)

