
import argparse
import time
from datetime import datetime

DATA_FILE = '/Users/plude/.scripts/time_keeper/time_data.txt'
DT_FORMAT = '%Y-%m-%d %H:%M:%S.%f'

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', action='store_true')
    parser.add_argument('--stop', action='store_true')
    return parser

def punch_time(log_line):
    time_now = datetime.fromtimestamp(time.time())
    time_str = time_now.strftime(DT_FORMAT)
    with open(DATA_FILE, 'a') as df:
        df.write(log_line.format(time_str))

def main():
    parser = init_parser()
    args = parser.parse_args()
    if args.start:
        punch_time('IN {}\n')
    elif args.stop:
        punch_time('OUT {}\n')
    
if __name__ == '__main__':
    main()
