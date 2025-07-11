test_case = int(input())

for _ in range(test_case):
    M, N, K = map(int, input().split())
    garden = [[0 for _ in range(M)] for _ in range(N)]
    visited_place = set()
    bug_counted = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        garden[Y][X] = 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for y in range(N):
        for x in range(M):
            if garden[y][x] == 1 and (y, x) not in visited_place:
                stack = [(y, x)]
                visited_place.add((y, x))
                while stack:
                    cy, cx = stack.pop()
                    for dy, dx in directions:
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < N and 0 <= nx < M:
                            if garden[ny][nx] == 1 and (ny, nx) not in visited_place:
                                stack.append((ny, nx))
                                visited_place.add((ny, nx))
                bug_counted += 1

    print(bug_counted)





