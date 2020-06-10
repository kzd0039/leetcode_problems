def trap(height):
    ans = 0
    i = 0
    while i < len(height):
        cur = height[i]
        j = i + 1
        s = 0
        maxium = 0
        index_maxium = j
        max_s = 0
        while j < len(height) and height[j] <= cur:
            if height[j] >= maxium:
                maxium = height[j]
                index_maxium = j
                max_s = s
            s += height[j]
            j += 1
        if j < len(height):
            ans += cur*(j-i-1) - s
            i = j
        else:
            ans += maxium*(index_maxium-i-1) - max_s
            i = index_maxium
            
            
    return ans

def main():
    lists = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(lists))

if __name__ == '__main__':
    main()