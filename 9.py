def isPalindrome(x):
    s=str(x)
    rs=s[::-1]
    return (s==rs)

def main():
    x = -121
    print(isPalindrome(x))

if __name__=='__main__':
    main()