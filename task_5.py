import argparse


def fetch_dict(users_file: str, hobbies_file: str, output_file: str):
    with open(users_file, 'r', encoding='utf-8') as u, \
            open(hobbies_file, 'r', encoding='utf-8') as h, \
            open(output_file, 'a', encoding='utf-8') as o:

        eof = False
        while not eof:
            user, hobby = u.readline(), h.readline()
            if not user and not hobby:
                eof = True

            user, hobby = user.strip('\n') if user else 'None', hobby.strip('\n') if hobby else 'None'
            o.write(user + ': ' + hobby + '\n')


parser = argparse.ArgumentParser(description='Bakery accounting script.')
parser.add_argument('users_file', type=str, help='File with users data.')
parser.add_argument('hobbies_file', type=str, help='File with hobbies data.')
parser.add_argument('output_file', type=str, help='Output file with all data.')
args = parser.parse_args()

_users_file = args.users_file
_hobbies_file = args.hobbies_file
_output_file = args.output_file

fetch_dict(_users_file, _hobbies_file, _output_file)
