from collections import deque

N = int(input())
data = deque()
books = {}

for i in input().split():
    num = int(i)
    data.append(num)
    if num in books:
        books[num] += 1
    else:
        books[num] = 1

variables = len(books)
front = 0
back = N - 1
total_count = 0

while front <= back and variables > 2:
    front_num = data[front]
    books[front_num] -= 1
    if books[front_num] == 0:
        variables -= 1
    total_count += 1
    front += 1

    if front > back or variables <= 2:
        break

    back_num = data[back]
    books[back_num] -= 1
    if books[back_num] == 0:
        variables -= 1
    total_count += 1
    back -= 1

print(N - total_count)