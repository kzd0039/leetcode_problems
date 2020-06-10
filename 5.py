def longestPalindrome(s):
    n = len(s)
    r=''
    maxlength=0
    for i in range(n):
        c_right=c_left=i
        while c_right+1<n and s[c_right+1]==s[i]:
            c_right = c_right+1
        while c_right+1<n and c_left-1>=0 and s[c_right+1]==s[c_left-1]:
            c_right = c_right+1
            c_left = c_left-1
        if maxlength<c_right-c_left+1:
            maxlength=c_right-c_left+1
            r=s[c_left:c_right+1]
            
    return r

def main():
    s = 'babad'
    ans = longestPalindrome(s)
    print(ans)


if __name__=='__main__':
    main()