def maxDotProduct(nums1, nums2):
    mem = [['X' for x in range(len(nums2))] for y in range(len(nums1))]
    def dp(nums1,nums2,i,j,mem,flg):
        if i < 0 or j < 0:
            if flg > 0:
                return 0
            return float('-inf')
        if mem[i][j] != 'X':
            return mem[i][j]
        res = nums1[i] * nums2[j]
        temp = res
        temp = max(res,dp(nums1,nums2,i-1,j,mem,flg),dp(nums1,nums2,i,j-1,mem,flg),res+dp(nums1,nums2,i-1,j-1,mem,flg+1))
        
        mem[i][j] = temp
        return temp
    
    ans = dp(nums1, nums2, len(nums1)-1, len(nums2)-1,mem,0)
    return ans

def main():
    nums1 = [-3,-8,3,-10,1,3,9]
    nums2 = [9,2,3,7,-9,1,-8,5,-1,-1]

    ans = maxDotProduct(nums1,nums2)
    print(ans)


if __name__=='__main__':
    main()