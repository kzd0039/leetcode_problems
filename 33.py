def search(nums,target):
    if not nums:
        return -1

    def binarysearch( nums, target, start, end):
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        mid = (end + start) // 2
        if mid == start:
            return -1
        if target == nums[mid]:
            return mid
        
        if nums[start] < nums[mid]:
            if target < nums[mid] and target > nums[start]:
                return binarysearch(nums, target, start, mid-1)
            else:
                return binarysearch(nums, target, mid+1, end)
        if nums[start] > nums[mid]:
            if target > nums[mid] and target < nums[end]:
                return binarysearch(nums, target, mid+1, end)
            else:
                return binarysearch(nums, target, start, mid-1)


    return binarysearch(nums, target, 0, len(nums) - 1)

def main():
    lists = [4,5,6,7,0,1,2]
    target = 0 
    print(search(lists,target))

if __name__ == '__main__':
    main()
    
