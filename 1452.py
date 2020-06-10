import collections

def peopleIndexes(favoriteCompanies):
    temp = collections.defaultdict(list)
    for i,x in enumerate(favoriteCompanies):
        temp[len(x)].append((i,set(x)))
                            
    key = [x for x in temp.keys()]
    key.sort(reverse = True)
    res = [ ]
                            
    for i in range(len(key)):
        if i == 0:
            for j in temp[key[i]]:
                res.append(j[0])
        else:
            for ele in temp[key[i]]:
                if not any(ele[1].issubset(s[1]) for j in range(i) for s in temp[key[j]]):
                    res.append(ele[0])
    res.sort()                    
    return res

def main():
    favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
    ans = peopleIndexes(favoriteCompanies)
    print(ans)

if __name__=='__main__':
    main()
