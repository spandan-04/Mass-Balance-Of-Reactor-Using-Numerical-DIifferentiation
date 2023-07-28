import numpy as np
import func
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

D = 2
U = 1
dx = 2.5
k = 0.2
cin = 100
dt = 0.3
lmbda = (U*dt)/dx
n = 7
x = np.arange(0, 10, 10/n)

c = n*[0]
c1 = n*[0]
for i in range(n):
    c1[0] = c[0] - lmbda*(-(D/(U*dx) + 0.5)*(c[1] + 2*dx*U*cin/D - 2*dx*U*c[0]/D) + (2*D/(U*dx) + k*dx/U)*c[0] - (D/(U*dx) - 0.5)*c[1])
    for j in range(1, n-1):
        c1[j] = c[j] - lmbda*(-(D/(U*dx) + 0.5)*c[j-1] + (2*D/(U*dx) + k*dx/U)*c[j] - (D/(U*dx) - 0.5)*c[j+1])
    c1[n-1] = c[n-1] - lmbda*(-(2*D/(U*dx))*c[n-2] + (2*D/(U*dx) + k*dx/U)*c[n-1])
    # plt.plot(x, c1)
    spline = make_interp_spline(x, c1)
    X = np.linspace(x[0], x[-1], 500)
    Y = spline(X)
    plt.plot(X, Y)
    for j in range(n):
        c[j] = c1[j]

A = [n*[0] for i in range(n)]
A[0][0] = (2*D/(U*dx)) + (k*dx/U) + 2 + (dx*U/D)
A[0][1] = -2*D/(U*dx)
for i in range(2, n):
    A[i-1][i-2] = -(D/(U*dx) + 0.5)
    A[i-1][i-1] =  (2*D/(U*dx) + k*dx/U)
    A[i-1][i]   = -(D/(U*dx) - 0.5)
A[n-1][n-2] = -2*D/(U*dx)
A[n-1][n-1] = (2*D/(U*dx) + k*dx/U)

B = n*[0]
B[0] = (2 + dx*U/D)*cin

aug_mat = A
for i in range(n):
    aug_mat[i].append(B[i])
# print(np.array(aug_mat))

c_inf = func.gauss_eli(aug_mat)

plt.plot(x, c_inf)
plt.show()