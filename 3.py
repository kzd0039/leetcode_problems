def lengthOfLongestSubstring(s):
    i, result, l = 0, 0, len(s)
    
    while i < l:
        j = i
        temp = { }
        while  j < l and s[j] not in temp:
            temp[s[j]] = j
            j += 1
        if j - i > result:
            result = j - i 
        try:
            i = temp[s[j]] + 1
        except:
            i += 1
        
    return result

def main():
    s = "pwwkew"
    ans = lengthOfLongestSubstring(s)
    print(ans)


if __name__=='__main__':
    main()