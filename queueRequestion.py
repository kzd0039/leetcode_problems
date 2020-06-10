def reconstructQueue(people):
    lib = { }
    for h, k in people:
        if h not in lib:
            lib[h] = [k]
        else:
            lib[h].append(k)
    
    res = [ ]
    keys = [x for x in lib.keys()]
    keys.sort()
    
    for key in reversed(keys):
        cur = lib[key]
        cur.sort()
        if not res:
            for k in cur:
                res.append([key,k])
        else:
            temp = [1] * (len(res) + len(cur))
            
            for k in cur:
                temp[k] = [key, k]
                
            i, j = 0, 0
            while i < len(temp):
                if temp[i] == 1:
                    temp[i] = res[j]
                    j += 1
                i += 1
            res = temp
                    
    return res


def main():

    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    res = reconstructQueue(people)
    print(res)
    

if __name__ == '__main__':
    main()