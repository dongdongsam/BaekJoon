import sys

N = int(input())
original = [int(sys.stdin.readline().strip()) for _ in range(N)]

data = []
answer = []

current_number = 1 # 어차피 1부터 N까지 한번식 나오 니까 리스트 대체 가능

idx = 0

while idx < N:
    target = original[idx]
    if current_number <= target:
        data.append(current_number)
        answer.append('+\n')
        current_number += 1
    else:
        if data and data[-1] == target:
            data.pop()
            answer.append('-\n')
            idx += 1
        else:
            sys.stdout.write('NO')
            sys.exit()

sys.stdout.write(''.join(answer))