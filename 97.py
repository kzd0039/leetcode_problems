def isInterleave(s1, s2, s3):
    i, j, k = len(s1)-1, len(s2)-1, len(s3)-1
    mem = [[-1 for a in range(j+1)] for b in range(i+1) ] 
    def dp(s1,s2,s3,i,j,k):
        if i == -1 and j == -1 and k == -1:
            return True
        if i == -1:
            if j >= 0 and k >= 0 and s2[j] == s3[k]:
                return dp(s1,s2,s3,i,j-1,k-1)
            return False
        if j == -1:
            if i >= 0 and k >= 0 and s1[i] == s3[k]:
                return dp(s1,s2,s3,i-1,j,k-1)
            return False
        if k == -1:
            return False
        
        if mem[i][j] != -1:
            return mem[i][j]
        if s1[i] == s3[k] and s2[j] == s3[k]:
            temp = dp(s1,s2,s3,i-1,j,k-1) or dp(s1,s2,s3,i,j-1,k-1)
        elif s1[i] == s3[k]:
            temp = dp(s1,s2,s3,i-1,j,k-1)
        elif s2[j] == s3[k]:
            temp =  dp(s1,s2,s3,i,j-1,k-1)
        else:
            temp = False
        
        mem[i][j] = temp
        return temp
        

    return dp(s1,s2,s3,i,j,k)

def main():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac" 
    print(isInterleave(s1,s2,s3))

if __name__ == '__main__':
    main()