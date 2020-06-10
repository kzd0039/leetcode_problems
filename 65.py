def validateNumber(s):
    lib = s.split(' ')
    c = 0
    for ele in lib:
        if ele != None:
            c += 1
            try:
                float(ele)
            except:
                return False
        if c > 1:
            return False

def main():
    num = " 0.1 "
    ans = validateNumber(num)
    print(ans)


if __name__=='__main__':
    main()