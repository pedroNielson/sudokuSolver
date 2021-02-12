grid = [
    [1,0,0,3,5,7,4,0,8],
    [4,0,0,1,6,0,2,0,0],
    [7,0,0,4,0,0,0,6,3],
    [0,0,0,0,8,2,0,1,6],
    [0,2,0,5,0,3,0,4,7],
    [0,0,7,0,0,0,0,3,0],
    [0,0,0,2,3,0,0,8,9],
    [0,9,8,0,0,0,0,0,1],
    [0,3,0,8,9,5,7,2,4]
]


def solveGrid(gr):
    find = find_empty(gr)
    if not find:
        return True
    else:
        x,y = find

    for i in range(1,10):
        if possible(gr, i, (x, y)):
            gr[x][y] = i

            if solveGrid(gr):
                return True

            gr[x][y] = 0

    return False


def possible(gr, num, pos):
    for i in range(9):
        if gr[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(9):
        if gr[i][pos[1]] == num and pos[0] != i:
            return False
    x0 = (pos[1] // 3)*3
    y0 = (pos[0] // 3)*3
    for i in range(x0, y0 + 3):
        for j in range(y0, x0 + 3):
            if gr[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty(gr):
    for i in range(9):
        for j in range(9):
            if gr[i][j] == 0:
                return (i, j)  

    return None

def printGrid(gr):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(gr[i][j])
            else:
                print(str(gr[i][j]) + " ", end="")




print("Sudoku challenge: ")
printGrid(grid)
solveGrid(grid)
print("----------------------------------------")
print("Solved: ")
printGrid(grid)