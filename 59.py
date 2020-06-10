def generateMatrix(n):
    result = [[0 for i in range(n)] for j in range(n)]
    
    left = 0
    up = 0
    right = n - 1
    down = n - 1
    num = 1
    
    while up <= down and left <= right:
        for i in range(left, right + 1):
            result[up][i] = num
            num += 1
        up += 1
        
        for j in range(up, down + 1):
            result[j][right] = num
            num += 1
        right -= 1
        
        for m in range(right, left - 1, -1):
            result[down][m] = num
            num += 1
        down -= 1
        
        for k in range(down, up -1, -1):
            result[k][left] = num
            num +=1
        left += 1
        
    return result

def main():
    n = 3
    print(generateMatrix(n))

if __name__ == '__main__':
    main()