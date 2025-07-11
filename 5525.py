O_Count = int(input())
string_length = int(input())
data = str(input())

i = 0
total_count = 0

sample = "IO" * O_Count + "I"

while i < string_length:
    if data[i:i+(2*O_Count + 1)] == sample:
        total_count += 1
        i += 2
    else:
        i += 1

print(total_count)
