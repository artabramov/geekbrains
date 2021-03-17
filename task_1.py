import re


def nginx_parse(log_file: str):
    lines = []

    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = re.sub(r'(.*GET|POST|PUT|DELETE|HEAD)( /.*)( HTTP|HTTPS)(.*\d)( \d)', r'\1"\2"\3\4"\5', line)
            lines.append(re.split(r' - - \[|] "| "-" "|" |"', line)[0:-1])

    return lines


results = nginx_parse('c:/_delete/nginx_logs.txt')
for result in results:
    print(result)
