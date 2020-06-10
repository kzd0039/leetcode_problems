import math
import collections

def getProbability(balls):
    total = math.factorial(sum(balls)) 
    for x in balls:
        total = total // math.factorial(x)
    
    def dp(n,cur,remain,r):
        if n == 0:
            c = collections.Counter(cur)
            if len([x for x in c.keys()]) == r:
                return 1
            return 0

        ans = 0
        for i,ele in enumerate(remain):
            if ele > 0:
                if ele == 1:
                    r -= 1
                remain[i] -= 1
                ans += dp(n-1,cur+[ele],remain,r)
                remain[i] += 1
        return ans

    res = dp(sum(balls)//2,[],balls,len(balls))

    return 2 * res / total

def main():
    balls = [1,2,1,2]
    ans = getProbability(balls)
    print(ans)


if __name__=='__main__':
    main()