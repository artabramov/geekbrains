import re


EMAIL_RE = re.compile(r'^([0-9a-z-_.]{2,80})@([0-9a-z-_.]{2,80})$')


def parse_email(txt: str):
    return EMAIL_RE.findall(txt)


if __name__ == '__main__':
    print(parse_email('my.domain@geekbrains.ru'))
