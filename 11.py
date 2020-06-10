def maxArea(height):      
    result, l, r = 0, 0, len(height) - 1
    
    while l < r:
        result = max(result, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
            
    return result

def main():
    height = [1,8,6,2,5,4,8,3,7]
    ans = maxArea(height)
    print(ans)


if __name__=='__main__':
    main()