
def Sol( data, a,b,c,d ):
    seen = set()
    Q = [ (a,b,0) ]
    while Q:
        a,b,dist = Q.pop(0)
        if (a,b) == (c,d): return dist
        if (a,b) in seen: continue
        seen.add( (a,b) )
        temp = a-1
        while temp >= 0:
            if data[ temp ][ b ] == 'X': break
            Q.append( (temp,b,dist+1) )
            temp-=1
        temp = a+1
        while temp < len(data):
            if data[ temp ][ b ] == 'X': break
            Q.append( (temp,b,dist+1) )
            temp+=1
        temp = b-1
        while temp >= 0:
            if data[ a ][ temp ] == 'X': break
            Q.append( (a,temp,dist+1) )
            temp-=1
        temp = b+1
        while temp < len(data):
            if data[ a ][ temp ] == 'X': break
            Q.append( (a,temp,dist+1) )
            temp+=1

N = int(input())
data = []
for _ in range(N):
    data.append( input() )
a,b,c,d = map(int,input().split())
print(Sol(data,a,b,c,d))
