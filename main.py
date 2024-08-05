import argparse
import concurrent.futures
import urllib.request



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('file_path')  # positional argument
    parser.add_argument('pattern')  # positional argument
    parser.add_argument('-c', '--count')  # option that takes a value
    parser.add_argument('-v', '--verbose',
                        action='store_true')  # on/off flag

    args = parser.parse_args()
    # print(args.file_path, args.count, args.verbose)
