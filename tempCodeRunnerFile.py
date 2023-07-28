A = [n*[0] for i in range(n)]
# A[0][0] = (2*D/(U*dx)) + (k*dx/U) + 2 + (dx*U/D)
# A[0][1] = -2*D/(U*dx)
# for i in range(2, n):
#     A[i-1][i-2] = -(D/(U*dx) + 0.5)
#     A[i-1][i-1] =  (2*D/(U*dx) + k*dx/U)
#     A[i-1][i]   = -(D/(U*dx) - 0.5)
# A[n-1][n-2] = -2*D/(U*dx)
# A[n-1][n-1] = (2*D/(U*dx) + k*dx/U)

# B = n*[0]
# B[0] = (2 + dx*U/D)*cin

# aug_mat = A
# for i in range(n):
#     aug_mat[i].append(B[i])
# print(np.array(aug_mat))

# c = func.gauss_eli(aug_mat)

# plt.plot(x, c)