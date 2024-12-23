from collections import deque
import sys

test_case = int(input())

for i in range(test_case):
    instruction_text = sys.stdin.readline().strip()
    array_length = int(sys.stdin.readline().strip())
    array_element_text = sys.stdin.readline().strip()

    if array_element_text == '[]':
        array_element = []
    else:
        array_element_text = array_element_text[1:len(array_element_text) - 1]
        if array_element_text:
            array_element = list(map(int, array_element_text.split(',')))
        else:
            array_element = []

    queue = deque(array_element)

    isReversed = False
    isError = False

    for n in instruction_text:
        if n == 'R':
            if not isReversed:
                isReversed = True
            else:
                isReversed = False
        elif n == 'D':
            if len(queue) - 1 < 0:
                isError = True
                break
            else:
                if isReversed:
                    queue.pop()
                else:
                    queue.popleft()

    if isError:
        print("error")
        continue
    else:
        if isReversed:
            queue.reverse()
        print('[', end='')
        print(*queue, sep = ',', end='')
        print(']')

