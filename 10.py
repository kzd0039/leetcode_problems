def isMatch(s,p):
    mem = [[-1 for x in range(len(p))] for y in range(len(s))]
    
    def dp(s,p,i,j,mem,flg):
        if i <= -1:
            if j <= -1:
                return True
            elif p[j] == '*':
                return dp(s,p,i,j-2,mem,flg)
            else:
                return False
        if j <= -1:
            return False

        if mem[i][j] != -1:
            return mem[i][j]
        if p[j] == '*':
            temp = dp(s,p,i,j-2,mem,0) or dp(s,p,i,j-1,mem,1)
        elif p[j] == '.' or p[j] == s[i]:
            temp = dp(s,p,i-1,j-1,mem,0)
            if flg == 1:
                temp = temp or dp(s,p,i-1,j,mem,1) or dp(s,p,i-1,j,mem,0)
        else:
            temp = False
            
        mem[i][j] = temp
        return temp
    
    return dp(s,p,len(s)-1,len(p)-1,mem,flg=0)


def main():
    s = "aab"
    p = "c*a*b"
    ans = isMatch(s,p)
    print(ans)


if __name__=='__main__':
    main()