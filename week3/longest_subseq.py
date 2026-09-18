def lcs_length(x,y):
    m = len(x)
    n = len(y)
    dp= [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[m][n]
seq1="DHANUSH"
seq2="ANUSH"
length = lcs_length(seq1, seq2)
print(f"Length of Longest Common Subsequence between '{seq1}' and '{seq2}' is: {length}")
