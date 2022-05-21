'''
A makeshift code that finds the points on the elliptic curve
\[
y^2 = x^3 + 1
\]
over the finite field of $p$ elements for a given input $p$.
Feel free to change `curve` to find points on a different curve.
'''
curve = lambda x : x ** 3 + 1

while True:
    p = int(input())
    quadratic_residues = [0] * p
    for i in range(p):
        r = i ** 2 % p
        if isinstance(quadratic_residues[r], int):
            quadratic_residues[r] = [i]
        else:
            quadratic_residues[r].append(i)

    results = [] * p
    for i in range(p):
        temp = (curve(i)) % p
        if not isinstance(quadratic_residues[temp], int):
            for j in quadratic_residues[temp]:
                result_temp = (i, j)
                results.append(result_temp)


    print(results, f'\nN_p = {len(results) + 1}')
