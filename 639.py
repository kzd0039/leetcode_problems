def numDecodings(s):
    end = len(s)
    mem = [-1 for x in range(end)] 
    
    def dp(s,i,end,mem):
        if i == end:
            return 1
        if mem[i] != -1:
            return mem[i]
        
        if s[i] == '*':
            temp = 9*dp(s,i+1,end,mem)
            if i+1 < end: 
                if s[i+1] == '*':
                    temp += 15 * dp(s,i+2,end,mem)
                elif int(s[i+1]) <= 6:
                    temp += 2*dp(s, i+2,end,mem)
                else:
                    temp += dp(s, i+2,end,mem)
        elif int(s[i]) == 1:
            temp = dp(s,i+1,end,mem)
            if i+1 < end: 
                if s[i+1] == '*':
                    temp += 9*dp(s,i+2,end,mem)
                else:
                    temp += dp(s,i+2,end,mem)
        elif int(s[i]) == 2:
            temp = dp(s,i+1,end,mem)
            if i+1 < end:
                if s[i+1] == '*':
                    temp += 6*dp(s,i+2,end,mem)
                elif int(s[i+1]) <= 6:
                    temp += dp(s, i+2,end,mem)
                else:
                    pass
        elif int(s[i]) == 0:
            temp = 0
        else:
            temp = dp(s,i+1,end,mem)
            
        mem[i] = temp
        return temp
        
    a = dp(s,0,end,mem)
    return  a%(10**9 + 7)

def main():
    s = "1*"
    print(numDecodings(s))

if __name__ == '__main__':
    main()