def minPathSum( grid):    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if r > 0 and c > 0:
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
            elif r > 0:
                grid[r][c] += grid[r-1][c]
            elif c > 0:
                grid[r][c] += grid[r][c-1]
            else:
                continue
                
    return grid[-1][-1]

def main():
    lists = [
                [1,3,1],
                [1,5,1],
                [4,2,1]
            ]
  
    print(minPathSum(lists))

if __name__ == '__main__':
    main()