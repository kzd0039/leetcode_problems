def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    p = len(nums) - 1
    v = nums[p]
    while p >=0 and nums[p] >= v:
        v = nums[p]
        p -= 1 
        
    if p >= 0:    
        p2 = p + 1
        v = nums[p]
        while p2 < len(nums) and nums[p2] > v:
            p2 += 1
        nums[p], nums[p2 - 1] = nums[p2 - 1], nums[p]
    
    l = p + 1
    r = len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

def main():
    lists = [1,1,5]
    nextPermutation(lists)
    print(lists)

if __name__ == '__main__':
    main()