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

        N = np.zeros(L).astype(int)  #number of books in library
        T = np.zeros(L).astype(int) #days to sign up
        M = np.zeros(L).astype(int) # number of books that we can ship per day
        BS = dict.fromkeys(range(B)) #book score
        for i,book in enumerate(BS):
            BS[book] = S[i]

        LB = dict.fromkeys(range(L))

        for i in range(L):
            N[i],T[i],M[i] = list(map(int,f.readline().strip().split(' ')))
            LB[i] =  np.array(list(set(map(int,f.readline().strip().split(' ')))))

        return B,L,D,N,T,M,BS,LB

def library_score(lb, bs):
    for lib in lb:
        print(lib, sum(bs[i] for i in lb[lib]))


if __name__ == '__main__':
    B,L,D,N,T,M,BS,LB = parse_input('data/a_example.txt')
    print(
    "Number of books", B, '\n',
    "number of libraries", L, '\n',
    "Total number of Days", D, '\n')

    for library, n, t, m in zip(range(L), N, T, M):
        print("Library", library, ", Number of books", n,
              ", Days to sign up", t, ", Books library can ship per day", m)

    print(LB)
    print(BS)
    print(library_score(LB, BS))
