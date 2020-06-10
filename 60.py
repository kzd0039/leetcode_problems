import math
def getPermutation(n, k):
    array  = [ str(i + 1) for i in range(n)]
    result = ''
    i = n
    while k >= 0 and i >= 1:
        tem = math.factorial(i-1)
        index = (k-1) // tem
        result += array[index]
        array.remove(array[index])
        k = k % tem
        i = i-1
        
    return result

def main():
    n = 3
    k = 3
    print(getPermutation(n,k))

if __name__ == '__main__':
    main()