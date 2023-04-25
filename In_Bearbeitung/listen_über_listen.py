list = [[1,2,3,4,5,6],[7,8,9,10,11],[12,13,14,15],[16,17,18,19]]

for i in range(len(list)):
    print("|",end=" ")
    for j in range(len(list[i])):
        print(f"{list[i][j]}",end=" ")
    print("|")