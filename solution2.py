from parser import parse_input, parse_output
from collections import defaultdict
import time


B, L, D, N, T, M, BS, LB = parse_input('data/e_so_many_books.txt')



master = dict.fromkeys(range(len(LB)))
L_scores = dict.fromkeys(range(len(LB)))
for i in L_scores:
    L_scores[i] = 0
    master[i] = {'is_signed_up':False, 'score':0}

if __name__ == '__main__':
    # [{lib_number:int,num_books:int,list_books:list},...]

    LB_copy = LB.copy()


    my_books = set()
    for day in range(D):
        L_scores_int = {}
        my_books1 = set()
        for i, library in enumerate(LB_copy):
            s = 0
            books_can_send_per_day = M[i]
            k = 0
            while k < books_can_send_per_day:
                if len(LB_copy[i]) == 0:
                    break
                b_id = LB_copy[i][0]
                if b_id not in my_books:
                    s += BS[b_id]
                    LB_copy[i].pop(0)
                k += 1
            print("Library {} has score {} on day {}".format(i, s, day))
            L_scores_int[i] = s
        L_scores_int = {k: v for k, v in sorted(L_scores_int.items(), key=lambda item: item[1], reverse=True)}
        for k in L_scores_int:
            if master[k] is False:

                master[k]['is_signed_up'] = True
                print('Signing up for', k)
                break
        for i in LB:
            if master[k]['is_signed_up'] == True:
                for j in range(M[i]):
                    master[k]['score'] += BS[LB[i]]
                    my_books.add(LB[i].pop(0))
        LB_copy = LB


        print(day)
    for k in master:
        if master[k]['score'] > 0:
            print(master[k])
    # print(master)
