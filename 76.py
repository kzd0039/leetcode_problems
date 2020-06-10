import collections
def minWindow(s,t):
    tar = collections.Counter(t)
    cur = collections.Counter()
    
    l, r, dif, res = 0, 0, float('inf'), ''
    
    while l < len(s):
        if all(cur[x] >= tar[x] for x in tar.keys()):
            if r - l < dif:
                res = s[l:r]
                dif = r - l
            cur[s[l]] -= 1
            l += 1
        else:  
            if r < len(s):
                cur[s[r]] += 1
                r += 1
            else:
                l += 1
        
    return res

def main():
    S = "ADOBECODEBANC" 
    T = "ABC"
    print(minWindow(S,T))

if __name__ == '__main__':
    main()