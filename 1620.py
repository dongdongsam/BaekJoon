import sys

N, M = map(int, input().split())

d_numToName, d_nameToNum = dict(), dict()

for i in range(1, N+1):
    d_numToName[i] = sys.stdin.readline().strip()
    d_nameToNum[d_numToName[i]] = i

for k in range(M):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        sys.stdout.write(d_numToName[int(question)])
    else:
        sys.stdout.write(str(d_nameToNum[question]))

    if k != M - 1:
        sys.stdout.write('\n')