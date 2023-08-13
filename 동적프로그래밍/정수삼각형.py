def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    
    for i in range(n-1):
        for j in range(i+1):
            dp[i+1][j] = max(dp[i][j] + triangle[i+1][j], dp[i+1][j])
            dp[i+1][j+1] = max(dp[i][j] + triangle[i+1][j+1], dp[i+1][j+1])
        
            
    return max(dp[n-1])