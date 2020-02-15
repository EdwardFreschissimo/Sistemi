m = [[0,1,0,1,0], [1,0,1,1,1], [0,1,0,1,0], [1,1,1,0,0],[0,1,0,0,0]]

k = 0
i = 0
nNodi = 5

for k in range(nNodi):
    for i in range(nNodi):
        if m[k][i] == 1:
            print(str(k) + "è adiacente a" + str(1))