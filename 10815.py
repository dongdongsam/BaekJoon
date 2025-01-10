import sys

n = int(input())

num_cards = sys.stdin.readline().strip()
num_cards = list(map(int, num_cards.split()))

infos = {i: True for i in num_cards}

m = int(input())

det_cards = sys.stdin.readline().strip()
det_cards = list(map(int, det_cards.split()))

for k in range(0, m):
    end_key = " "
    if k == m-1:
        end_key = ""

    if det_cards[k] in infos :
        sys.stdout.write("1" + end_key)
    else :
        sys.stdout.write("0" + end_key)

