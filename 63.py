def uniquePathsWithObstacles(obstacleGrid):
    
    for r in range(len(obstacleGrid)):
        for c in range(len(obstacleGrid[0])):
            if r == 0 and c == 0:
                obstacleGrid[r][c] = 1
            elif obstacleGrid[r][c] == 1:
                obstacleGrid[r][c] = 0
            else:
                if c > 0 :
                    obstacleGrid[r][c] +=  obstacleGrid[r][c-1]
                if r > 0 :
                    obstacleGrid[r][c] +=  obstacleGrid[r-1][c]
            
    return obstacleGrid[-1][-1]

def main():
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    print(uniquePathsWithObstacles(grid))

if __name__ == '__main__':
    main()