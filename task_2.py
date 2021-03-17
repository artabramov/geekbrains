def nginx_ban(log_file: str):
    stats, ban = {}, ['', 0]

    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            ip = line.split(' - - ')[0]
            stats[ip] = stats[ip] + 1 if ip in stats else 1

            if stats[ip] > ban[1]:
                ban[0], ban[1] = ip, stats[ip]

    return ban


results = nginx_ban('c:/_delete/nginx_logs.txt')
print(results)
