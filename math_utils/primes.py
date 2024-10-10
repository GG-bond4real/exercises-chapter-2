def isprime(n):
    if n<=1:
        return False
    for r in range(2, int(n**0.5)+1):
        if n%r == 0:
            return False
    return True