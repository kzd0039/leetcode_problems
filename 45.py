def jump(nums):
    ans = 0
    i = 0
    res = [i+x for i,x in enumerate(nums)]
    while i < len(nums)-1:
        ans += 1
        if res[i] >= len(nums)-1:
            break
        cur = res[i]
        n = i
        for j in range(i,res[i]+1):
            if j < len(nums) and res[j] > cur:
                n = j
                cur = res[j]
        if n == i:
            i = res[i]
        else:
            i = n
            
    
    return ans


def main():
    lists = [2,3,1,1,4]
    print(jump(lists))

if __name__ == '__main__':
    main()