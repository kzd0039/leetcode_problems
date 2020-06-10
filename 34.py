def searchRange(nums,target):
    if not nums or (target < nums[0] and target > nums[len(nums)-1]):
        return [-1, -1]

    def binarysearch(nums, target, start, end):
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        mid = (end + start) // 2
        if mid == start:
            return -1
        if target == nums[mid]:
            return mid
        
        if target < nums[mid]:
            return binarysearch(nums, target, start, mid-1)
        else:
            return binarysearch(nums, target, mid+1, end)


    left = right = binarysearch(nums, target, 0, len(nums)-1)
    while left > 0 and nums[left-1] == target:
        left = left - 1
    while right < len(nums) - 1 and nums[right+1] == target:
        right = right + 1
    
    return [left, right]


def main():
    lists = [5,7,7,8,8,10]
    target = 8
    print(searchRange(lists, target))

if __name__ == '__main__':
    main()
    
    
