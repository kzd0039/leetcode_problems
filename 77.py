def combine(n,k):
    array = [ i for i in range(1,n+1)]
    res = [ ]
    
    def backtrack(k, current, remain, res):
        if k == 0:
            res.append(current)
        else:
            for i in range(len(remain)):
                backtrack(k-1, current+[remain[i]], remain[i+1:], res)
                
    backtrack(k, [ ], array, res)       
    return res

def main():
    n = 4
    k = 2
    print(combine(n,k))

if __name__ == '__main__':
    main()