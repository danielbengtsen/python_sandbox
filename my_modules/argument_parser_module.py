import argparse

def argument_parser():
    parser= argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('url', help='an integer for the accumulator')
    print(parser.parse_args())
    args = parser.parse_args()
    print(args.url)

if __name__ == '__main__':
    argument_parser()