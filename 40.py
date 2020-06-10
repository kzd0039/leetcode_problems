def combinationSum2(candidates,target):
    candidates.sort()
    combinations = []
    
    def backtrack(nums, curr_sum, i):
        if curr_sum == target and nums not in combinations:
            combinations.append(nums)
        elif curr_sum < target:
            for j in range(i+1, len(candidates)):
                backtrack(nums + [candidates[j]], curr_sum + candidates[j], j)
    
    for i in range(len(candidates)):
        backtrack([candidates[i]], candidates[i], i) 
        
    return combinations

def main():
    candidates =[10,1,2,7,6,1,5]
    target = 8

    print(combinationSum2(candidates,target))

if __name__ == '__main__':
    main()