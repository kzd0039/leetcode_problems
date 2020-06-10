def smallestStringWithSwaps(s,pairs): 
    temp = [ ]
    for x,y in pairs:
        if not temp:
            temp.append(set([x,y]))
        for ele in temp:
            pass
 
      
    res = list(s)
    for ele in temp:
        indexs = list(ele)
        indexs.sort()
        cur = [s[i] for i in ele]
        cur.sort()
        i = cur[0]
        for i in range(len(indexs)):
            res[indexs[i]] = cur[i]
    
    return res

def main():
    pairs = [[5,3],[3,0],[5,1],[1,1],[1,5],[3,0],[0,2]]
    s = "pwqlmqm"

    ans = smallestStringWithSwaps(s,pairs)
    print(ans)


if __name__=='__main__':
    main()