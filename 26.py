def removeDuplicates(nums):
    if not nums:
        return 0
    
    r = 1
    j = 1
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            r += 1
            nums[j] = nums[i]
            j += 1
    
    return r

def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    ans = removeDuplicates(nums)
    print(nums[:ans])

if __name__ == '__main__':
    main()