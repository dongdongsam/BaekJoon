
N, R, C = map(int, input().split())

Area = 2 ** (2*N)

def determin_area(N:int, F:int, S:int):
    # Var and Index Setting
    global R
    global C
    rowIndex = 1 if R // (2**(N-1)) >= 1 else 0
    colIndex = 1 if C // (2**(N-1)) >= 1 else 0


    #Termination Condition
    if N == 1:
        if rowIndex == 0 and colIndex == 0:
            return F
        elif rowIndex == 0 and colIndex == 1:
            return F + 1
        elif rowIndex == 1 and colIndex == 0:
            return F + 2
        elif rowIndex == 1 and colIndex == 1:
            return F + 3


    # Continuous Condition
    range = int((S - F +1)/4)

    # R, C Trans
    R %= 2 ** (N - 1)
    C %= 2 ** (N - 1)


    if rowIndex == 0 and colIndex == 0:
        return determin_area(N-1, F, F + range - 1)
    elif rowIndex == 0 and colIndex == 1:
        return determin_area(N-1, F + range, F + range*2 - 1)
    elif rowIndex == 1 and colIndex == 0:
        return determin_area(N-1, F + range*2, F + range*3 - 1)
    elif rowIndex == 1 and colIndex == 1:
        return determin_area(N-1, F + range*3, F + range*4 - 1)

print(determin_area(N,0, Area-1))
