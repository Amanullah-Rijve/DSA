def lcs(text1, text2):
    m = len(text1)
    n = len(text2)

    # create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Example
s1 = "abcde"
s2 = "ace"

print("LCS length:", lcs(s1, s2))