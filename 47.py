def permuteUnique(nums):
    res = [ ]
    
    def backtrack(current, remain, res):
        if not remain:    
            res.append(current)
        else:
            track = set()
            for i in range(len(remain)):
                if remain[i] not in track:
                    track.add(remain[i])
                    next_remain = remain[:i] + remain[i+1:]
                    backtrack(current+[remain[i]], next_remain, res)
                
    backtrack([], nums, res)

    return res

def main():
    lists = [1,1,2]
   
    print(permuteUnique(lists))

if __name__ == '__main__':
    main()