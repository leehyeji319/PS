alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dict = {}
for i, a in enumerate(alphabet):
    dict[a] = str(i + 1)
answer_arr = [dict[n] for n in input()]

print(" ".join(answer_arr))
