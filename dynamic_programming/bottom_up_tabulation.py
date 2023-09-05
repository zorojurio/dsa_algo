

def fibonacci(n: int) -> int:
    tb = [0, 1]
    for i in range(2, n+1):
        tb.append(tb[i-1] + tb[i-2])
    return tb[n-1]


print(fibonacci(6))