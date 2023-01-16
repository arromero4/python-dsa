#2x2 matrix "X"
X = [[1,2], [2,3]]

#2x2 matrix "Y"
Y = [[2,3],[3,4]]

#2x2 matrix of "0"
result = [[0,0],[0,0]]

#itarates through rows X = m
for i in range(len(X)):
    #itarates through columns Y = n
    for j in range(len(Y[0])):
        #itarates through rows of Y 
        for k in range(len(Y)):
            result[i][j] += X[i][j] * Y[k][j]

for end in result:
    print(end)