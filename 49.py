def groupAnagrams(strs):
    result = { }
    
    for s in strs:
        key = ''.join(sorted(s))
        if key in result:
            result[key].append(s)
        else:
            result[key] = [s]
            
    return result.values()


def main():
    lists = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(lists))

if __name__ == '__main__':
    main()