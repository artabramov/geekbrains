import argparse
import decimal
import os


def update_data(file: str, line_num: int, amount: decimal):
    line_num = line_num - 1
    tmp_file = file + '.tmp'
    with open(file, 'r+', encoding='utf-8') as f, open(tmp_file, 'w+', encoding='utf-8') as t:

        i = 0
        for line in f:
            t.write(str(amount) + '\n' if i == line_num else line)
            i = i + 1

    os.remove(file)
    os.rename(tmp_file, file)


parser = argparse.ArgumentParser(description='Bakery accounting script.')
parser.add_argument('file', type=str, help='File with the data.')
parser.add_argument('line_num', type=int, help='Line of the number.')
parser.add_argument('amount', type=int, help='A new sum.')
args = parser.parse_args()

_file = args.file
_line_num = args.line_num
_amount = args.amount

update_data(_file, _line_num, _amount)
