def myPow(x, n):
    y = n
    n = abs(n)  
    r = 1
    while n != 0:
        if n % 2 == 1:
            r *= x
            n -= 1 
        n = n // 2
        x = x*x   
    if y >= 0:
        return r
    return 1/r

def main():
    x = 2.00000
    n = 10
    
    print(pow(x,n))

if __name__ == '__main__':
    main()