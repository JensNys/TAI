import copy

#scalar = b*a^-1
def gauss(A,p):
    for i in range(len(A)):# voor elke rij
        if A[i][i]==0:
            pivot(A,search(A[i]),i)
        multiply(A,i,pow(A[i][i],-1,p),p)
        for j in range(len(A)):
            if i != j and A[j][i]!= 0:
                #a*x=b mod p
                b=A[j][i]
                subtract(A,j,i,b,p)
            printmatrix(A)


def transpose(A):
    #A is an nxm matrix
    n = len(A)
    m=len(A[0])


def search(A,i):
    for j in range(i,len(A)):
        if A[j]!=0:
            return j
    return -1
#switches row i and j
def pivot(A,i,j):
    sub = copy.deepcopy(A[i])
    A[i] = A[j]
    A[j]=sub

#row i -> rowi - scalar * rowj
def subtract(A,i,j,scalar,p):
    sub = copy.deepcopy(A[j])
    for el in range(len(sub)):
        sub[el]=(scalar*sub[el])%p
    for el in range(len(sub)):
        A[i][el]=(A[i][el]-sub[el])%p

def multiply(A,i,scalar,p):

    for el in range(len(A[i])):
        A[i][el]=(scalar*A[i][el])%p


def printmatrix(A):
    for i in range(len(A)):
        print(A[i])
    print()

def main():
    A=[[1, 2, 3, 4], [3, 4, 1,2],[2,3,1,4]]
    gauss(A,5)




    #gauss([[1,2,3,4],[3,4,5,6]])




if __name__ == '__main__':
    main()
