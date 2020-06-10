import collections

def rearrange(nums):     
    c = collections.defaultdict(list)
    for ele in nums:
        if c[ele-1]:
            c[ele-1].sort()
            r = c[ele-1][0]
            c[ele-1] = c[ele-1][1:]
            c[ele].append(r+1)
        else:
            c[ele].append(1)
                    
    return all(x >= 3 for key in c.keys() for x in c[key])
            

def main():
    nums = [1,2,3,3,4,4,5,5]
    ans = rearrange(nums)
    print(ans)


if __name__=='__main__':
    main()