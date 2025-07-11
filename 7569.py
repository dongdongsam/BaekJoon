import sys
import queue

#basic variables
M, N, H= map(int, input().split())
count_of_empty = 0
count_of_day = 0
count_of_tomato = 0
count_of_total_tomato = 0

# datas
data = [] # y -> z -> x
tomato_index = queue.Queue()

for k in range(H):
    temp_floor = []
    for j in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        for i in range(M):
            if row[i] == 1:
                tomato_index.put((i, k, j)) # x, y, z, minecraft.
            elif row[i] == -1:
                count_of_empty += 1
        temp_floor.append(row)
    data.append(temp_floor)

temp_data = []
count_of_total_tomato += tomato_index.qsize()

#main logic
while True:
    if tomato_index.qsize() != 0:
        selected_tomato = tomato_index.get() # x, y, z
        det_l, det_r, det_f, det_b, det_u, det_d = True, True, True, True, True, True

        if selected_tomato[0] == 0:
            det_l = False
        if selected_tomato[0] == M - 1:
            det_r = False

        if selected_tomato[2] == 0:
            det_f = False
        if selected_tomato[2] == N - 1:
            det_b = False

        if selected_tomato[1] == 0:
            det_u = False
        if selected_tomato[1] == H - 1:
            det_d = False

        idx, idy, idz = selected_tomato[0], selected_tomato[1], selected_tomato[2]
        if det_l:
            if data[idy][idz][idx-1] == 0:
                temp_data.append((idx-1, idy, idz))
                data[idy][idz][idx-1] = 1
                count_of_tomato += 1
                count_of_total_tomato += 1
        if det_r:
            if data[idy][idz][idx+1] == 0:
                temp_data.append((idx+1, idy, idz))
                data[idy][idz][idx+1] = 1
                count_of_tomato += 1
                count_of_total_tomato += 1
        if det_f:
            if data[idy][idz-1][idx] == 0:
                temp_data.append((idx, idy, idz-1))
                data[idy][idz-1][idx] = 1
                count_of_tomato += 1
                count_of_total_tomato += 1
        if det_b:
            if data[idy][idz+1][idx] == 0:
                temp_data.append((idx, idy, idz+1))
                data[idy][idz+1][idx] = 1
                count_of_tomato += 1
                count_of_total_tomato += 1
        if det_u:
            if data[idy-1][idz][idx] == 0:
                temp_data.append((idx, idy-1, idz))
                data[idy-1][idz][idx] = 1
                count_of_tomato += 1
                count_of_total_tomato += 1
        if det_d:
            if data[idy+1][idz][idx] == 0:
                temp_data.append((idx, idy+1, idz))
                data[idy+1][idz][idx] = 1
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
        if (count_of_empty + count_of_total_tomato) == M*N*H:
            print(count_of_day)
        else:
            print(-1)
        break