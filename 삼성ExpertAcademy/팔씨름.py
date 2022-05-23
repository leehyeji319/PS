T = int(input())
for t in range(1, T + 1):
    fight = input()
    virtual_fight = fight + ('o' * (15 - len(fight)))
    if virtual_fight.count('o') >= 8:
        print(f"#{t} YES")
    else:
        print(f"#{t} NO")
