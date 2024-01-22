#multiply nxn matrix
def multiply(self,a):
    return [[sum(a[i][k]*b[k][j] for k in range(len(a)))
             for j in range(len(b[0]))]
            for i in range(len(a))]
def sum(self,a):
    return [[sum(a[i][k]*b[k][j] for k in range(len(a)))
             for j in range(len(b[0]))]