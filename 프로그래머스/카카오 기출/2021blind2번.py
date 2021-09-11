import math
def solution(n, k):
    answer = 0
    
    def convert(n, base):
        T = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return T[r]
        else:
            return convert(q, base) + T[r]
    change = convert(n, k)
    
    def isprime(n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
        
    split_change = change.split('0')
    split_change = ' '.join(split_change).split()
    split_change = list(map(int,split_change))
    while 1 in split_change:
        split_change.remove(1)
    answer = [v for v in split_change if isprime(v) or v == 2]

    return len(answer)