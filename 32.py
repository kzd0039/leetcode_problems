def longestValidParentheses(s):
    lists=[]
    index=[]
    
    for i in range(len(s)):
        if lists:
            temp=lists.pop()
            if (temp,s[i]) == ('(',')'):
                index.pop()
            else:
                lists.append(temp)
                lists.append(s[i])
                index.append(i)
        else:        
            index.append(i)
            lists.append(s[i])
    
    if not index: 
        return len(s)
    else:
        maxlength=max(index[0],len(s)-index[len(index)-1]-1)
        if len(index)>=2:
            for i in range(len(index)-1):
                    if index[i+1]-index[i]-1>maxlength:
                        maxlength=index[i+1]-index[i]-1
        return maxlength

def main():
    s = ")()())"
    print(longestValidParentheses(s))

if __name__ == '__main__':
    main()
