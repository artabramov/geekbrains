def print_intervals(duration: int):
    """Print time intervals from the number of seconds.
    Let 365 days in one year and 30 days in one month."""

    data, output = {}, ""

    if not isinstance(duration, int) or duration < 0:
        duration = 0

    data["Y"] = duration // (365 * 24 * 60 * 60)
    duration -= data["Y"] * 365 * 24 * 60 * 60

    data["M"] = duration // (30 * 24 * 60 * 60)
    duration -= data["M"] * 30 * 24 * 60 * 60

    data["d"] = duration // (24 * 60 * 60)
    duration -= data["d"] * 24 * 60 * 60

    data["h"] = duration // (60 * 60)
    duration -= data["h"] * 60 * 60

    data["m"] = duration // 60
    data["s"] = duration - data["m"] * 60

    for i in data:
        if data[i] > 0 or output:
            output += " <" + i + "> " + str(data[i])

    print(output)
    return True


print_intervals(365 * 24 * 60 * 60)
