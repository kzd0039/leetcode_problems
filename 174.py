def calculateMinimumHP(dungeon):
    res = [[0 for c in range(len(dungeon[0]))] for r in range(len(dungeon))]
    
    for r in range(len(dungeon)):
        for c in range(len(dungeon[0])):
            cur = dungeon[r][c]
            if r > 0 and c > 0:
                add_up = 1 - cur - res[r-1][c]
                dun_up = dungeon[r-1][c] + max(0, add_up)
                res_up = res[r-1][c] + cur +  max(0, add_up)
                add_left = 1 - cur - res[r][c-1]
                dun_left = dungeon[r][c-1] + max(0, add_left)
                res_left = res[r][c-1] + cur +  max(0, add_left)
                
                if dun_up > dun_left:
                    dungeon[r][c] = dun_left
                    res[r][c] = res_left
                else:
                    dungeon[r][c] = dun_up
                    res[r][c] = res_up
            elif r > 0:
                add = 1 - cur - res[r-1][c]
                dungeon[r][c] = dungeon[r-1][c] + max(0, add)
                res[r][c] = res[r-1][c] + cur +  max(0, add)
            elif c > 0:
                add = 1 - cur - res[r][c-1]
                dungeon[r][c] = dungeon[r][c-1] + max(0, add)
                res[r][c] = res[r][c-1] + cur +  max(0, add)
            else:
                if dungeon[r][c] <= 0:
                    dungeon[r][c] = 1 - dungeon[r][c] 
                    res[r][c] = 1
                else:
                    res[r][c] = dungeon[r][c] + 1
                    dungeon[r][c] = 1
                    
    return dungeon[-1][-1]

def main():
    grid = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
    print(calculateMinimumHP(grid))

if __name__ == '__main__':
    main()
                        