def solution(n):
    dp = [0] * (n+1)
    
    for i in range(n+1):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = 1
        else:
            dp[i] = dp[i-1] + dp[i-2]   
    
    if n < 2:
        return 1 if n == 1 else 0
    
    return dp[n] % 1234567