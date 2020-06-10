def generateParenthesis(n):
    left = 0
    right = 0
    result = []
    total = n
    tem = ''
    def generate( result, t, l, r, w):
        if l < w and l>=r:
            generate(result, t+'(', l+1, r, w)
            
        if r < l:
            generate(result, t+')', l, r+1, w)

        if l==w and r ==w:
            result.append(t)

    generate(result, tem, left, right, total)
    return result
    
def main():
    n = 3 
    print(generateParenthesis(n))

if __name__ == '__main__':
    main()
    
    



