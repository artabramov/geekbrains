from requests import get
from datetime import date
from decimal import Decimal

CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
CBR_DATA = {}


def parse_text(source_text: str, open_tag: str, close_tag: str):
    """
    Strip first entry between open and close tags.
    Return inner text and outer text that remains.
    """

    open_pos = source_text.find(open_tag) + len(open_tag)
    close_pos = source_text.find(close_tag)

    inner_text = source_text[open_pos: close_pos]
    outer_text = source_text[close_pos + len(close_tag):]

    return inner_text, outer_text


def currency_rates(currency_code: str):
    """
    Parse an XML file from cbr.ru and return currency rate and date.
    XML will load only one time per script session.
    """

    currency_code = currency_code.upper().strip()
    if not CBR_DATA:

        response = get(CBR_URL)
        if response.status_code == 200:
            outer_text = response.text

            # get the date
            outer_date, outer_text = parse_text(outer_text, '<ValCurs Date="', '" name')
            date_parts = list(map(int, outer_date.split('.')))
            CBR_DATA['_date'] = date(date_parts[2], date_parts[1], date_parts[0])

            # get the currency rates
            while True:
                inner_text, outer_text = parse_text(outer_text, '<Valute', '</Valute')

                if not inner_text:
                    break

                inner_code, inner_text = parse_text(inner_text, 'CharCode>', '</CharCode')
                inner_rate, inner_text = parse_text(inner_text, 'Value>', '</Value')

                if inner_code and inner_rate:
                    CBR_DATA[inner_code] = Decimal(inner_rate.replace(',', '.'))

    if currency_code in CBR_DATA:
        return CBR_DATA[currency_code], CBR_DATA['_date']


if __name__ == '__main__':
    print('USD:', currency_rates('usd'))
    print('EUR:', currency_rates('eur'))
