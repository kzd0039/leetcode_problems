import math
def numPoints(points, r):
    ans = 1
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x3 = (points[i][0] + points[j][0])/2
            y3 = (points[i][1] + points[j][1])/2
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            q = math.sqrt(dx**2 + dy**2)
            if q > 2.0*r:
                continue

            d = math.sqrt(r**2-(q/2)**2)
            c1x = x3 - d*dy/q
            c1y= y3 + d*dx/q

            c2x = x3 + d*dy/q
            c2y= y3 - d*dx/q

            center = [[c1x,c1y],[c2x,c2y]]
            
            for centerX, centerY in center:
                temp = 0
                for x,y in points:
             
                    if (x-centerX)**2 + (y-centerY)**2  - r**2 < 0.00001:
                        temp += 1
                ans = max(temp, ans) 
                    
    return ans

def main():
    points = [[4,5],[-4,1],[-3,2],[-4,0],[0,2]]
    r = 5
    ans = numPoints(points, r)
    print(ans)


if __name__=='__main__':
    main()
