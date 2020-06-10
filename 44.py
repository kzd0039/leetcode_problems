def isMatch(s, p):      
    i = len(s) - 1
    j = len(p) - 1
    r =[[-1 for x in range(j+1)] for y in range(i+1)]
    
    def dp(s,p,i,j,r):
        if i == -1 and j == -1:
            return True   
        if j == -1:
            return False
        if i == -1:
            if  p[j] == '*':
                return dp(s,p,i,j-1,r)
            else:
                return False
        
        if r[i][j] != -1:
            return r[i][j]
        
        if s[i] == p[j] or p[j] == '?':
            temp = dp(s,p,i-1,j-1,r)
        elif p[j] == '*':
            temp = dp(s,p,i-1,j-1,r) or dp(s,p,i-1,j,r) or dp(s,p,i,j-1,r)
        else:
            temp = False   
            
        r[i][j] = temp
        return temp
    
    return dp(s,p,i,j,r)

def main():
    s = "adceb"
    p = "*a*b"
    print(isMatch(s,p))

if __name__ == '__main__':
    main()