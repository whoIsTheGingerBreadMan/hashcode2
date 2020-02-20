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
            l_id = list(set(map(int,f.readline().strip().split(' '))))
            l_new = sorted([(_id, BS[_id]) for _id in l_id], key=lambda x: x[1], reverse=True)
            LB[i] = [i[0] for i in l_new]

        return B,L,D,N,T,M,BS,LB

def parse_output(output,out_loc='solution.out'):
    """
    Takes in a list of dictionaries and makes a file out of them.
    [{lib_number:int,num_books:int,list_books:list},...]

    :param output:
    :return:
    """
    with open(out_loc,'w') as f:
        num_libraries = len(output)
        f.write(str(num_libraries))
        f.write('\n')
        for lib in output:
            l = f"{lib['lib_number']} {lib['num_books']}"
            f.write(l)
            f.write('\n')
            l = " ".join(map(str,lib['list_books']))
            f.write(l)
            f.write('\n')



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
