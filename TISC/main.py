import argparse

from registos import main

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='TISC', description='TISC')

    parser.add_argument('-m, --inst_memory', action='store_true', dest='memory', help='To print instruction memory',
                        required=False)

    parser.add_argument('-l, --lable_memory', action='store_true', dest='lables', help='To print lables memory',
                        required=False)

    parser.add_argument('-f, --file_path', type=str, dest='file_path', help='TISC file to run',
                        required=False)

    args = parser.parse_args()
    main(args.memory, args.lables,args.file_path)
