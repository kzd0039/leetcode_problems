def largestRectangleArea(heights):
    heights = [0] + heights + [0]
    ans = 0
    stack = [ ]
    
    for i,num in enumerate(heights):
        while stack and heights[stack[-1]] > num:
            last = stack.pop()
            ans = max(ans,(i-stack[-1]-1)*heights[last])
        stack.append(i)
        
    return ans

def main():
    heights = [1,2,3,4,2]
    ans = largestRectangleArea(heights)
    print(ans)


if __name__=='__main__':
    main()