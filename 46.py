def permute(nums):
    res = [ ]
    
    def backtrack(current, remain, res):
        if not remain:
            res.append(current)
        else:
            for i in range(len(remain)):
                next_remain = remain[:i] + remain[i+1:]
                backtrack(current+[remain[i]], next_remain, res)
                
    backtrack([], nums, res)

    return res

def main():
    lists = [1,2,3]
   
    print(permute(lists))

if __name__ == '__main__':
    main()