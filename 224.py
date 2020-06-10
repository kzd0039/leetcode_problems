def calculate(s):
    stack = [ ]
    i = 0
    sign = 1
    while i < len(s):
        ele = s[i]
        j = i + 1
        if ele.isdigit():
            num = 0
            while j < len(s) and s[j].isdigit():
                num = num*10 + int(s[j])
                j += 1
            stack.append(sign*num)
            sign = 1
        elif ele == '-':
            sign = -1
        elif ele == '(':
            stack.append(ele)
        elif ele == ')':
            cur = 0
            while stack[-1] != '(':
                cur += stack.pop()
            stack.pop()
            stack.append(cur)
        else:
            pass
        i = j
        
    return sum(stack)

def main():
    s = " 2-1 + 2 "
    ans = calculate(s)
    print(ans)


if __name__=='__main__':
    main()