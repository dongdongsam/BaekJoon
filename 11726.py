
DP = [1, 2, 3]

n = int(input())

if n <= 3:
    print(DP[n-1] % 10007)
else:
    for i in range(3, n):
        DP.append(DP[i-1] + DP[i-2])
    print(DP[n-1] % 10007)
