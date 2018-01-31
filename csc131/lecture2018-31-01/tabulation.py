#bottom-up approach -> Tabulation
def fib_tab(n : int) -> int:
    f[0] * (n + 1)
    #base case
    f[1] = 1
    for i in range(2,n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return [n]