def merge(intervals):
    intervals.sort(key = lambda x:(x[0],x[1]))
    if not intervals:
        return [ ]
    
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        cur = intervals[i]
        if cur[0] > res[-1][1]:
            res.append(cur)
        else:
            last = res.pop()
            res.append([last[0],max(last[1],cur[1])])
            
    return res

def main():
    lists = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(lists))

if __name__ == '__main__':
    main()