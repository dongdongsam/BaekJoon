import sys
import queue

#basic variables
M, N = map(int, input().split())
count_of_empty = 0
count_of_day = 0
count_of_tomato = 0
count_of_total_tomato = 0

# datas
data = []
tomato_index = queue.Queue()

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if row[j] == 1:
            tomato_index.put((j, i))
        elif row[j] == -1:
            count_of_empty += 1
    data.append(row)

temp_data = []
count_of_total_tomato += tomato_index.qsize()

while True:
    if tomato_index.qsize() != 0:
        selected_tomato = tomato_index.get()
        det_l, det_r, det_u, det_d = True, True, True, True

        if selected_tomato[0] == 0:
            det_l = False
        elif selected_tomato[0] == M - 1:
            det_r = False
        if selected_tomato[1] == 0:
            det_u = False
        elif selected_tomato[1] == N - 1:
            det_d = False

        idx, idy = selected_tomato[0], selected_tomato[1]
        if det_l:
            if data[idy][idx - 1] == 0:
                temp_data.append((idx - 1, idy))
                data[idy][idx - 1] = 1
                count_of_tomato += 1
                count_of_total_tomato += 1
        if det_r:
            if data[idy][idx + 1] == 0:
                temp_data.append((idx + 1, idy))
                data[idy][idx + 1] = 1
                count_of_tomato += 1
                count_of_total_tomato += 1
        if det_u:
            if data[idy - 1][idx] == 0:
                temp_data.append((idx, idy - 1))
                data[idy - 1][idx] = 1
                count_of_tomato += 1
                count_of_total_tomato += 1
        if det_d:
            if data[idy + 1][idx] == 0:
                temp_data.append((idx, idy + 1))
                data[idy + 1][idx] = 1
                count_of_tomato += 1
                count_of_total_tomato += 1

        if count_of_tomato > 0 and tomato_index.qsize() == 0:
            count_of_day += 1
            count_of_tomato = 0
        continue
    elif len(temp_data) != 0:
        for elem in temp_data : tomato_index.put(elem)
        temp_data = []
    else:
        if (count_of_empty + count_of_total_tomato) == M*N:
            print(count_of_day)
        else:
            print(-1)
        break