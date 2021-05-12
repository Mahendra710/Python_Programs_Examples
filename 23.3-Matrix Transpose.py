p=int(input("Enter the row number:"))
q=int(input("Enter the column number:"))

print("Enter the elements for Matrix:")
matrix=[[int(input()) for i in range(q)]for j in range(p)]
print("matrix is:",matrix)
for i in range(p):
    for j in range(q):
        print(format(matrix[i][j],"<4"),end=" ")
    print()

matrix_transpose=[[0 for i in range(p)]for j in range(q)]
print("Matrix Transpose is:")
for i in range(q):
    for j in range(p):
        matrix_transpose[i][j]=matrix[j][i]
        print(format(matrix_transpose[i][j],"<4"),end=" ")
    print()