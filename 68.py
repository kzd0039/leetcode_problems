def fullJustify(words, maxWidth):
    ans = [ ]
    c = 0
    cur = [ ]
    for ele in words:
        if c + len(ele) <= maxWidth and len(cur) - 1 + c + len(ele)<= maxWidth:
            cur.append(ele)
            c += len(ele)
        else:
            blank = maxWidth - c
            divide = len(cur) - 1
            if divide == 0:
                ans.append(cur[0] + ' ' * blank)
            elif blank % divide == 0:
                white = (blank // divide) * ' '
                ans.append(white.join(cur))
            else:
                white = (blank // divide) * ' '
                r = cur[0] + ' '*(blank//divide + blank%divide) + white.join(cur[1:])
                ans.append(r)
                
            c = len(ele)   
            cur = [ele]
                    
    extra_white = (maxWidth - c - len(cur) + 1) * ' '
    ans.append(' '.join(cur) + extra_white)
    
    return ans

def main():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(fullJustify(words,maxWidth))

if __name__ == '__main__':
    main()
               