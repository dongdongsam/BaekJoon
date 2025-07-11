
N = int(input())

datas = list(map(int, input().split()))
T_Count = 0

T, P = map(int, input().split())
for elem in datas:
    T_Count += (elem // T) if (elem % T) == 0 else (elem // T) + 1

P_count = N // P

print(T_Count)
print(P_count, (N - (P_count * P)))
