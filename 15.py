def threeSum(nums):
    n = len(nums)
    if n < 3:
        return []

    nums.sort()

    triplets = set()

    for i in range(n-2):
        a = nums[i]
        index = set()
        for j in range(i+1, n):
            b = nums[j]
            c = -a-b
            if b not in index:
                index.add(c)
            else:
                triplets.add((a,b,c))

    return triplets

def main():
    lists = [-1, 0, 1, 2, -1, -4]
    print(threeSum(lists))

if __name__ == '__main__':
    main()