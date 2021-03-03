import random


# 1/2
def num_translate_adv(number_eng: str):
    numbers = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    is_title = True if number_eng.istitle() else False
    number_eng = number_eng.lower()

    if number_eng not in numbers:
        return None
    elif is_title:
        return numbers[number_eng].title()

    return numbers[number_eng]


# 3
def thesaurus(*names):
    result = dict()
    for name in names:
        if not name[0].upper() in result:
            result[name[0].upper()] = list()

        result[name[0].upper()].append(name)

    return result


# 4
def thesaurus_adv(*names):

    # fill the dict by surnames/names
    unsorted_result = dict()
    for name in names:
        name_key, surname_key = name.split()[0][0].upper(), name.split()[1][0].upper()

        if surname_key not in unsorted_result:
            unsorted_result[surname_key] = dict()

        if name_key not in unsorted_result[surname_key]:
            unsorted_result[surname_key][name_key] = list()

        unsorted_result[surname_key][name_key].append(name)

    # sort the dict by keys from 'А' to 'Я'
    sorted_result = dict()
    for surname_code in range(1040, 1072):
        surname_chr = chr(surname_code)

        if surname_chr in unsorted_result:
            sorted_result[surname_chr] = dict()

            for name_code in range(1040, 1072):
                name_chr = chr(name_code)

                if name_chr in unsorted_result[surname_chr]:
                    sorted_result[surname_chr][name_chr] = unsorted_result[surname_chr][name_chr]

    return sorted_result


# 5
def get_jokes(n: int, unique=False) -> list:
    """Generate random n jokes"""

    # words for the jokes
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes = list()
    for i in range(n):

        # create a random joke
        noun = nouns[random.randrange(0, len(nouns), 1)]
        adverb = adverbs[random.randrange(0, len(adverbs), 1)]
        adjective = adjectives[random.randrange(0, len(adjectives), 1)]
        jokes.append(noun + " " + adverb + " " + adjective)

        # remove used words for unique jokes
        if unique:
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)

            # stop the function if words are over
            if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:
                break

    return jokes


# 1/2
print(num_translate_adv('Nine'))

# 3
print(thesaurus("Иван", "Мария", "Петр", "Илья"))

# 4
print(thesaurus_adv('Женя сидоров', 'Юлия Игнатьева', 'Игорь Семенов', 'Стас Крылов', 'Наташа Петухова', 'Сергей Баранов', 'Кирилл Козлов', 'Александр Котов', 'Юрий Собакин', 'Артем Иванов', 'андрей Петров'))

# 5
print(get_jokes(n=4, unique=True))
