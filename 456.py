def find132pattern(nums):
    k=float('-inf')
    st=[]
    for nm in nums[::-1]:  #traversing nums in reverse order
        if nm<k:                
            return True

        while st and st[-1]<nm:
            k=st.pop()

        st.append(nm)
    return False   

def main():
    nums = [3, 1, 4, 2]
    ans = find132pattern(nums)
    print(ans)


if __name__=='__main__':
    main()