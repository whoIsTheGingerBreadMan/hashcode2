import numpy as np
def parse_input(file_location):
    """
    B - number of books
    L- number of libraries
    D - total numebr of days

    N[i] - number of books in library i
    T[i] - days to sign up for library i
    M[i] - number of books library i can ship per day
    BS[i] - score of book i
    LB[ı] - Books in library i
    :param file_location:
    :return:
    """
    with open(file_location,'r') as f:

        B,L,D = list(map(int,f.readline().strip().split(' ')))
        S = list(map(int,f.readline().strip().split(' ')))

        N = np.zeros(len(L))  #number of books in library
        T = np.zeros(len(L)) #days to sign up
        M = np.zeros(len(L)) # number of books that we can ship per day
        BS = dict.fromkeys(range(B),S) #book score
        LB = dict.fromkeys(range(L))

        for i in range(L):
            N[i],T[i],M[i] = list(map(int,f.readline().strip().split(' ')))
            LB[i] =  np.array(map(int,f.readline().strip().split(' ')))

        return B,L,D,N,T,M,BS,LB




