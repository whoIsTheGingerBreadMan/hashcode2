from parser import parse_input
from stats import library_score

def main(input_file):
    B, L, D, N, T, M, BS, LB = parse_input(input_file)
    LBS = library_score(LB,BS)
    print('blah')


if __name__ == '__main__':
    main('data/a_example.txt')
