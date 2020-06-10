def uniquePaths(m, n):
    res = [[1 for x in range(m)] for y in range(n)]
    
    for r in range(1,n):
        for c in range(1,m):
            res[r][c] = res[r-1][c] + res[r][c-1]
            
    return res[n-1][m-1]

def main():
    m = 7
    n = 3
    print(uniquePaths(m,n))

if __name__ == '__main__':
    main()