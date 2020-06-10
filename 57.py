def insert(intervals,newInterval):
    ans = [ ]
    c = 0
    for ele in intervals:
        if ele[1] < newInterval[0]:
            ans.append(ele)
        elif ele[0] > newInterval[1] and c==0:
            c = 1
            ans.append(newInterval)
            ans.append(ele)
        elif ele[0] > newInterval[1] and c==1:
            ans.append(ele)
        else:
            newInterval = [min(newInterval[0],ele[0]), max(newInterval[1],ele[1])]
    if c == 0:
        ans.append(newInterval)
    return ans

def main():
    intervals = [[1,3],[6,9]]
    newInterval = [2,5] 
    print(insert(intervals,newInterval))

if __name__ == '__main__':
    main()