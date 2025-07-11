import sys

MBTI = ["ISTJ", "ISFJ", "INFJ", "INTJ",
        "ISTP", "ISFP", "INFP", "INTP",
        "ESTP", "ESFP", "ENFP", "ENTP",
        "ESTJ", "ESFJ", "ENFJ", "ENTJ"]

nest_data = {i : False for i in MBTI}

T = int(input())

for i in range(T):
    N = int(input())
    Data = sys.stdin.readline().strip().split()

    for elem in Data:
        if elem in MBTI:
            nest_data[elem] = True
        else:
            continue



