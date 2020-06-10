def longestCommonPrefix(strs):
    if not strs:
        return ''
    common = strs[0]
    for i in range(1, len(strs)):
        j = 0
        while j < min(len(strs[i]), len(common)) and strs[i][j] == common[j]:
            j += 1
        if j == 0:
            return ''

        common = common[:j]
                        
    return common

def main():
    s = ["flower","flow","flight"]
    ans = longestCommonPrefix(s)
    print(ans)


if __name__=='__main__':
    main()