def isValid(s):
    l = len(s)
    result = []
    
    for i in range(l):
        if s[i] in '({[':
            result.append(s[i])
        else:
            if not result:
                return False
            tem = result.pop()
            if (tem, s[i]) not in [('(',')'),('[',']'),('{','}')]:
                return False
            
    
    if not result:
        return True

def main():
    s = "{[]}"
    ans = isValid(s)
    print(ans)


if __name__=='__main__':
    main()