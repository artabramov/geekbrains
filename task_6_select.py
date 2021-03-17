import argparse


def load_data(file: str, start_pos=1, end_pos=1):
    with open(file, 'r', encoding='utf-8') as f:
        start_pos, end_pos = start_pos - 1, end_pos - 1

        for i in range(0, start_pos - 1):
            next(f)

        if end_pos > start_pos:
            for i in range(0, end_pos - start_pos + 1):
                line = next(f)
                print(line.strip('\n'))
            return

        for line in f:
            print(line.strip('\n'))


parser = argparse.ArgumentParser(description='Bakery accounting script.')
parser.add_argument('file', type=str, help='File with the data.')
parser.add_argument('start', default=0, nargs='?', type=int, help='Start of the offset.')
parser.add_argument('end', default=0, nargs='?', type=int, help='End of the offset.')
args = parser.parse_args()

file = args.file
start = args.start
end = args.end

load_data(file, start, end)
