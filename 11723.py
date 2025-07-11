import sys

M = int(input())

S = set()

for i in range(M):
    instruction = sys.stdin.readline().strip().split()

    if instruction[0] == 'add':
        S.add(instruction[1])
    elif instruction[0] == 'remove':
        if instruction[1] in S:
            S.discard(instruction[1])
    elif instruction[0] == 'check':
        if instruction[1] in S:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif instruction[0] == 'toggle':
        if instruction[1] in S:
            S.discard(instruction[1])
        else:
            S.add(instruction[1])
    elif instruction[0] == 'all':
        S = {str(i) for i in range(1, 21)}
    elif instruction[0] == 'empty':
        S = set()