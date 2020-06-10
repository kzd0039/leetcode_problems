def spiralOrder(matrix):
    result = []
    if not matrix:
        return result
    left = 0
    up = 0
    right = len(matrix) - 1
    down = len(matrix[0]) - 1
    
    
    while left <= right and up <= down:
        
        result += matrix[up][left:right+1]
        up += 1
        result += [matrix[i][right] for i in range(up,down+1)]
        right -= 1
        if up <= down:
            result += [matrix[down][i] for i in range(right,left-1,-1)]
            down -= 1
        if left <= right:
            result += [matrix[i][left] for i in range(down,up-1,-1)]
            left += 1
        
    return result

def main():
    m =[
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
        ]
    print(spiralOrder(m))

if __name__ == '__main__':
    main()