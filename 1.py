def twoSum(array, target):
    array = list(set(array))
    array.sort()
    result = [ ]
    l, r = 0, len(array) - 1
    while l < r:
        s = array[l] + array[r]
        if s == target:
            result.append([l,r])
            l += 1
            r -= 1
        elif s > target:
            r -= 1
        elif s < target:
            l += 1
    return result

def main():
    lists = [-1, 2, 1, -2, 0, 0, 0]
    target = 0 
    print(twoSum(lists, target))

if __name__ == '__main__':
    main()