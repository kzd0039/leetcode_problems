def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = set()
    coloum = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.add(i)
                coloum.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):      
            if i in row or j in coloum:
                matrix[i][j] = 0

def main():
    lists = [
                [1,1,1],
                [1,0,1],
                [1,1,1]
            ]
    setZeroes(lists)
    print(lists)

if __name__ == '__main__':
    main()