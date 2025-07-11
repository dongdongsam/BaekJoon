import sys

N, K = map(int, input().split())

variables = []

for i in range(N):
    variables.append(int(sys.stdin.readline().strip()))

removed_token_count = 0

while K != 0:

    gotten_token = variables.pop()
    cal_value = K//gotten_token

    if cal_value >= 1:
        removed_token_count += cal_value
        K -= gotten_token*cal_value

print(removed_token_count)