import argparse
import decimal
import os


def save_data(file: str, amount: decimal):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{amount}\n')


parser = argparse.ArgumentParser(description='Bakery accounting script.')
parser.add_argument('amount', type=str, help='Amount of the operation.')
parser.add_argument('file', type=str, help='File to save data.')
args = parser.parse_args()

amount = args.amount
file = args.file
save_data(file, amount)
