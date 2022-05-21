def pmod(a, k, n): # a^k \pmod n
    b = format(k, 'b')[::-1]
    r = 1
    p = [a % n]
    for i in range(len(b)):
        e = p[i] 
        p.append((e * e) % n)
        if int(b[i]):
            r *= p[i]
    return r % n

while True:
    try:
        a, b, c = [int(i) for i in input().split()]
        print(pmod(a, b, c))
    except Exception as e:
        print(e)
