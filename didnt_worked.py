import sys

s1 = list(map(int, input().split())) # s1 is the 4 element array
s2 = list(map(int, input().split())) # s2 is the 3 element array

g = []

for i in s1:
    g.append([])
    for j in s2:
        g[-1].append(abs(j-i))

while True:
    print(g)
    maxx = - sys.maxsize -1
    ind_array = -1 
    ind_elem = -1
    for i in range(len(g)):
        for j in range(len(g[i])):
            #print(maxx)
            if g[i][j] > maxx:
                maxx = g[i][j]
                ind_array = i
                ind_elem = j
    
    del g[ind_array][ind_elem]

    if len(g[ind_array]) == 0:
        break

del s1[ind_array]

print(s1)
print(s2)
