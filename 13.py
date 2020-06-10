def romanToInt(s):
    dicts={'I':1,'V':5,'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 
            'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM': 900}
    
    l = len(s)
    i = 0
    result = 0
    
    while i<l:
        if i+1 < l and s[i:i+2] in dicts:
            result += dicts[s[i:i+2]]
            i += 2
        else:
            result += dicts[s[i]]
            i += 1
    
    return result

def main():
    s = "MCMXCIV"
    ans = romanToInt(s)
    print(ans)


if __name__=='__main__':
    main()