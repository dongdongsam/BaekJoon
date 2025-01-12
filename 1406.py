import sys

inputted_text = sys.stdin.readline().strip()

N = len(inputted_text)

M = int(sys.stdin.readline().strip())

inputted_text = [i for i in inputted_text]
remained_text = []

for i in range(M):
    text = sys.stdin.readline().strip()

    if text[0] == "L" and len(inputted_text) > 0:
        remained_text.append(inputted_text.pop())
    elif text[0] == "D" and len(remained_text) > 0:
        inputted_text.append(remained_text.pop())
    elif text[0] == "B" and len(inputted_text) > 0:
        inputted_text.pop()
    elif text[0] == "P":
        inputted_text.append(text[2])

remained_text.reverse()

sys.stdout.write("".join(inputted_text) + "".join(remained_text))
