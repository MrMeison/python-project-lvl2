import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('--format', '-f', help='set format of output')
    parser.parse_args()

if __name__ == '__main__':
    main()
