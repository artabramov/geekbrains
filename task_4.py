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


fetch_dict('c:/_delete/users.csv', 'c:/_delete/hobby.csv', 'c:/_delete/_temp.csv')
