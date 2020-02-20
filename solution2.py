from parser import parse_input
from collections import defaultdict
import time


B, L, D, N, T, M, BS, LB = parse_input('data/e_so_many_books.txt')




L_scores = dict.fromkeys(range(len(LB)))
for i in L_scores:
    L_scores[i] = 0

if __name__ == '__main__':
    my_books = set()
    for day in range(D):
        for i, library in enumerate(LB):
            if (T[i] > day) or (len(LB[i]) == 0):
                continue
            s = 0
            books_can_send_per_day = M[i]
            k = 0
            while k < books_can_send_per_day:
                if len(LB[i]) == 0:
                    break
                b_id = LB[i][0]
                if b_id in my_books:
                    LB[i].pop(0)
                    k -= 1
                else:
                    my_books.add(b_id)
                    s += BS[b_id]
                    L_scores[i] += BS[b_id]
                    LB[i].pop(0)
                k += 1
            print("Library {} has score {} on day {}".format(i, s, day))
        print(day)
    ordered_L_scores = {k: v for k, v in sorted(L_scores.items(), key=lambda item: item[1], reverse=True)}
    print(ordered_L_scores)
