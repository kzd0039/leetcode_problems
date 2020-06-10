def minReorder(n,connections):
    res = [ -1 for x in connections]
    ans = 0
    cur = set([0])
    while cur:
        temp = set([])
        for i,x in enumerate(connections):
            if res[i] == -1:
                if x[1] in cur:
                    temp.add(x[0])
                    res[i] = 0
                elif x[0] in cur:
                    temp.add(x[1])
                    ans += 1
                    res[i] = 0
                else:
                    pass
        cur = temp
        
    return ans

def main():
    n = 6
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    ans = minReorder(n,connections)
    print(ans)


if __name__=='__main__':
    main()