def simplifyPath(path):
    ans = [ ]
    for ele in path:
        if ele == '/':
            if not ans or ans[-1] != '/':
                ans.append(ele)
            else:
                continue
        elif ele == '.':
            try:
                ans.pop()
                ans.pop()
            except:
                ans.append('/')
        elif ele.isalpha():
            ans.append(ele)
        else:
            continue
            
    if ans[-1] == '/':
        ans.pop()
        
    return ''.join(ans)

def main():
    path = "/a/../../b/../c//.//"
    ans = simplifyPath(path)
    print(ans)


if __name__=='__main__':
    main()