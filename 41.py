def firstMissingPositive(nums):
    s = float('inf')
    m = 0
    lib = set([])
    for ele in nums:
        if ele > 0:
            if ele > m:
                m = ele
            if ele < s:
                s = ele
            lib.add(ele)
            
    for i in range(1,m+2):
        if i not in lib:
            return i

def main():
    lists = [7,8,9,11,12]
    print(firstMissingPositive(lists))

if __name__ == '__main__':
    main()