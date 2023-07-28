def gauss_eli(a):
    x = len(a)*[0]
    n = len(a)
    # Elimination
    for i in range(n-1):
        if a[i][i] == 0:
            for j in range(i+1, n):
                if a[j][i] > a[i][i]:
                    a[j], a[i] = a[i], a[j]

    for i in range(n-1):
        for j in range(i,n-1):
                ratio = a[j+1][i]/a[i][i]
                a[j+1] = [sum(x) for x in zip(a[j+1], [-ratio*x for x in a[i]])]

    # Back substitution
    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax = sum_ax + a[i][j]*x[j]
        x[i] = (a[i][n] - sum_ax)/a[i][i]
    print("Solution: " + str(x))
    return x