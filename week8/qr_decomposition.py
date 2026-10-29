
import numpy as np

# QR Decomposition using Gram-Schmidt Method
# Application: Solving Linear Equations Ax = b

def qr_decomposition(A):
    n = A.shape[0]

    # Initialize orthogonal matrix Q and upper triangular matrix R
    Q = np.zeros((n, n))
    R = np.zeros((n, n))

    for j in range(n):
        # Select the current column of A
        v = A[:, j].copy()

        # Remove projections onto previous columns of Q
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]

        # Normalize the vector to obtain a column of Q
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]

    return Q, R


def solve_qr(Q, R, b):
    # Calculate Q transpose multiplied by b
    y = np.dot(Q.T, b)

    # Solve Rx = y using backward substitution
    n = R.shape[0]
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        sum_value = 0

        for j in range(i + 1, n):
            sum_value += R[i, j] * x[j]

        x[i] = (y[i] - sum_value) / R[i, i]

    return x


# Define coefficient matrix A
A = np.array([
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
], dtype=float)

# Define constant vector b
b = np.array([4, 5, 6], dtype=float)

# Perform QR decomposition
Q, R = qr_decomposition(A)

# Solve the system using QR decomposition
x = solve_qr(Q, R, b)

# Display the results
print("Matrix A:")
print(A)

print("\nOrthogonal Matrix Q:")
print(Q)

print("\nUpper Triangular Matrix R:")
print(R)

print("\nSolution Vector x:")
print(x)
