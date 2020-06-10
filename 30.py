def findSubstring(s, words):
    result = [ ]
    try:
        window = len(words[0])
    except:
        return result
    
    l = len(s)
    total = window*len(words)
    if l < total:
        return result
    
    library = { }
    for x in words:
        if x in library:
            library[x] += 1
        else:
            library[x] = 1
    
    for i in range(0, l - total + 1):
        temp = library.copy()
        j = i
        key = s[j:j+window]
        if key in temp:
            while key in temp and temp[key] > 0:
                temp[key] -= 1
                j += window
                key = s[j:j+window]
            if sum(temp.values()) == 0 and j == i + total:
                result.append(i)
        
    return result

def main():
    s = 'barfoothefoobarman'
    words = ["foo","bar"]
    print(findSubstring(s,words))

if __name__ == '__main__':
    main()