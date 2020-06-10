def combinationSum(candidates,target):
    combinations = []
    
    def backtrack(nums, curr_sum, i):
        if curr_sum == target:
            combinations.append(nums)
        elif curr_sum < target:
            for j in range(i, len(candidates)):
                backtrack(nums + [candidates[j]], curr_sum + candidates[j], j)
    
    for i in range(len(candidates)):
        backtrack([candidates[i]], candidates[i], i)
        
    return combinations

def main():
    candidates = [2,3,6,7]
    target = 7
    print(combinationSum(candidates,target))

if __name__ == '__main__':
    main()