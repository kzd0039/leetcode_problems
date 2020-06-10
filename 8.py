def myAtoi(str):
    result=''
    l=len(str)
    num=['0','1','2','3','4','5','6','7','8','9']
    sign=['+','-']
    i=0
    if l==0:
        return 0
    
    while  i<l and str[i] == ' ':
        i=i+1
        
    if i<l and str[i] in num:
        while i<l and str[i] in num:
            result += str[i]
            i += 1
            
    elif i<l-1 and str[i] in sign and str[i+1] in num:
        result=str[i]
        while i+1<l and str[i+1] in num:
            result += str[i+1]
            i += 1

    else:
        return 0
                
    result=int(result)
    
    if result > 2**31-1:
        return 2**31-1
    elif result < -2**31:
        return -2**31
    else:
        return result

def main():
    s = "   -42"
    ans = myAtoi(s)
    print(ans)


if __name__=='__main__':
    main()