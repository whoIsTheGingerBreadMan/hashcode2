from parser import parse_input
from stats import library_score, libraries_score

def main(input_file):
    B, L, D, N, T, M, BS, LB = parse_input(input_file)
    LBS = libraries_score(LB,BS)
    greedy_LBS = sorted(LBS, reverse=True)
    print(greedy_LBS)


# Assume no signup time

# For library L0
# Number L0 can send per day N select N highest scoring books from the that library
# Find the total score of that

if __name__ == '__main__':
    main('data/a_example.txt')
