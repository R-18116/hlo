r=int(input("rows: "))
c=int(input("columns: "))
print("rows with elements :")
matrix=[]
for i in range(r):
    li=list(map(int,input().split()))
    matrix.append(li)
print("original matrix:",matrix)  
transposed=[]
for i in range(len(matrix[0])):
    transposed_row=[]
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print("transposed matrix:",transposed)        

      