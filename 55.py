def canJump(nums):
    l = len(nums)   
    for i in range(l):
        if i != l-1 and nums[i] == 0:
            j = i
            while j >= 0:
                if nums[j] > i:
                    break
                j = j - 1
            if j < 0:
                return False   
        nums[i] = nums[i] + i
    
    return True

def main():
    nums = [2,3,1,1,4]
    print(canJump(nums))

if __name__ == '__main__':
    main()