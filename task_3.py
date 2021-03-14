# Task 3
def get_pairs(tutors: list, klasses: list):
    for id, tutor in enumerate(tutors):
        yield tutor, klasses[id] if id <= len(klasses) - 1 else None


_tutors =  ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
_klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']
pairs = get_pairs(_tutors, _klasses)
print(type(pairs))
print(list(pairs))
