def threeSumClosest(nums, target):
    nums.sort()
    diff = float('inf')
    for i in range(len(nums)):
        to_check = nums[:i] + nums[i+1:]
        current = twosumCloset(to_check, target, nums[i])
        if abs(current - target) < diff:
            result = current
            diff = abs(current - target)    
                    
    return result
                       
def twosumCloset(to_check, target, num):
    i, r = 0, len(to_check)-1
    dif = float('inf')
    while i < r:
        s = to_check[i] + to_check[r] + num
        if abs(s-target) < dif:
            dif = abs(s-target)
            result = s
        if s < target:
            i += 1  
        elif s > target:
            r -= 1
        else:
            break
    return result


def main():
    lists = [1,6,9,14,16,70]
    target = 81 
    print(threeSumClosest(lists,target))

if __name__ == '__main__':
    main()