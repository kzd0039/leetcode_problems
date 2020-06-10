def isValidSudoku(board):
    lib = { }
    
    for i in range(9):
        for j in range(9):
            key = board[i][j]
            if key != '.':
                block = i // 3 * 3 + j // 3
                if  key not in lib:
                    lib[key] = [[i, j, block]]
                else:
                    for x in lib[key]:
                        if x[0] == i or x[1] == j or x[2] == block:
                            return False
                    lib[key].append([i, j, block])
    return True

def main():
    board =   [ 
                ["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
               ]
    print(isValidSudoku(board))

if __name__ == '__main__':
    main()