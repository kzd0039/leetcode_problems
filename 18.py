def fourSum(nums,target):   
    nums.sort()
    result = set()
    for i in range(len(nums)-3):
        tar = target - nums[i]
        for j in range(i+1, len(nums)-2):
            
            r = len(nums)-1
            l = j + 1
            while l < r:
                s = nums[l] + nums[r] + nums[j]
                if s == tar:
                    result.add(str([nums[i],nums[j],nums[l],nums[r]]))
                    l += 1
                    r -= 1
                elif s > tar:
                    r -=1
                else:
                    l += 1
                    
    return [[int(x) for x in element[1:-1].split(',')] for element in result]

def main():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    ans = fourSum(nums,target)
    print(ans)

if __name__ == '__main__':
    main()