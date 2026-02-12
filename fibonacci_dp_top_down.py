def fibon(n):
    if n <=1:
        return n
    if n in memo:
        return memo[n]

    memo[n] =fibon(n-1) +fibon(n-2)
    return memo[n] 

memo={}
print(fibon(10))

