def reverse(x):
    start=str(x)
    l=len(start)
    result=''
    
    if start[0]=='-':
        result='-'
        for i in range(1,l):
            result=result+start[l-i]
    else:
        for i in range(l):
            result=result+start[l-i-1]

    result=int(result)
    
    if result<-2**31 or result>(2**31-1):
        return 0
    
    return result

def main():
    x= -123
    print(reverse(x))

if __name__ == '__main__':
    main()