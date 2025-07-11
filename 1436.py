value = int(input())

data = ["666"]


for i in range(0, value):
    if i > 0:
        data_L = str(i % 10) + data[i - 1]
        data_R = data[i-1] + str(i % 10)

        if int(data_R) < int(data_L):
            data.append(data_R)
        else:
            data.append(data_L)

if value == 1:
    print(data[0])

print(data[value-1])