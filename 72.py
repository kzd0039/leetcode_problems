def minDistance(word1,word2):
    i = len(word1) - 1
    j = len(word2) -1
    res = [[-1 for x in range(j+1)] for y in range(i+1)]
    def LCS(s, p, i, j, res):
        if i == -1 or j == -1:
            return max(0,i+1,j+1)
        if res[i][j] != -1:
            return res[i][j]
        if s[i] == p[j]:
            r = LCS(s, p, i-1, j-1,res) 
        else:
            r = min(LCS(s,p,i-1,j,res) + 1, LCS(s,p,i,j-1,res) + 1, LCS(s,p,i-1,j-1,res) + 1)           
        res[i][j] = r
        return r

    return LCS(word1, word2, i, j,res)

def main():
    word1 = "horse"
    word2 = "ros"
    print(minDistance(word1,word2))

if __name__ == '__main__':
    main()