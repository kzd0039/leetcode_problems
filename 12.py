def intToRoman(num):
    result = ''
    string = str(num)
    l = len(string)
    if l == 4:
        result += 'M'*(num//1000)
        l -= 1
        num = num%1000
    if l == 3:
        a = num//100
        b = num%100
        if a > 0 and a < 4:
            result += 'C'*a
        if a == 4:
            result += 'CD'
        if a ==9:
            result += 'CM'
        if a < 9 and a > 4:
            result += 'D'
            result += 'C'*(a-5)
        num = b
        l -= 1
    if l == 2:
        a = num//10
        b = num%10
        if a > 0 and a < 4:
            result += 'X'*a
        if a == 4:
            result += 'XL'
        if a ==9:
            result += 'XC'
        if a < 9 and a > 4:
            result += 'L'
            result += 'X'*(a-5)
        num = b
        l -= 1 
    if l == 1:
        a = num
        if a > 0 and a < 4:
            result += 'I'*a
        if a == 4:
            result += 'IV'
        if a == 9:
            result += 'IX'
        if a < 9 and a > 4:
            result += 'V'
            result += 'I'*(a-5)
    return result



def main():
    num = 1994
    ans = intToRoman(num)
    print(ans)


if __name__=='__main__':
    main()