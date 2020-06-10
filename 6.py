def convert(s, numRows):
    dicts={x:[] for x in range(numRows)}
    count=0
    total=len(s)
    p=numRows*2-2
    result=''
    
    if p != 0:
        while count<total:
            row=count%p
            if row <= p/2:
                dicts[row].append(s[count])
            else:
                dicts[p-row].append(s[count])
            count=count+1

        for ele in dicts:
            for x in dicts[ele]:
                result=result+x
    else:
        result=s
        
    return result

def main():
    s = "PAYPALISHIRING"
    numRows = 3
    ans = convert(s,numRows)
    print(ans)


if __name__=='__main__':
    main()