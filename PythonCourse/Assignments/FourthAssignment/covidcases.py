import requests
import pandas as pd
from bs4 import BeautifulSoup


def create_request_url(day: int) -> str:
    return f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{day}-aprilie-2020-ora-13-00/'


def fetch_data(date: int, extract_header: bool = False, include_empty_data: bool = False):
    request = requests.get(create_request_url(date))
    response = BeautifulSoup(request.text, features='html.parser')
    article = response.find_all('div', attrs={'class': 'inside-article'})

    if len(tables := article[0].find_all('table')) == 0:
        return {f'{date}-aprilie': []} if include_empty_data else None

    rows = tables[0].find_all('tr')

    headers = [header.get_text().lstrip() for header in rows[0].find_all('td')]
    headers[2] = f'{date}-aprilie'

    data = {}
    if extract_header is True:
        data[headers[0]] = []
        data[headers[1]] = []
    data[headers[2]] = []

    for row in rows[1:len(rows) - 1]:
        info = [info.get_text().lstrip() for info in row.find_all('td')]
        if extract_header is True:
            data[headers[0]].append(info[0])
            data[headers[1]].append(info[1])
        data[headers[2]].append(int(info[2].replace('.', '')))

    data[headers[2]].append(int(rows[-1].find_all('td')[1].get_text().replace('.', '')))
    return data


def find_max_lines(data: dict) -> int:
    return max([len(val) for val in data.values()])


def format_data(data: dict) -> None:
    max_lines = find_max_lines(data)

    headers = list(extracted_data.keys())

    while len(extracted_data[headers[0]]) != max_lines - 1:
        extracted_data[headers[0]].append(str(int(extracted_data[headers[0]][-1].replace('.', '')) + 1) + '.')
    if len(extracted_data[headers[0]]) != max_lines:
        extracted_data[headers[0]].append('')

    while len(extracted_data[headers[1]]) != max_lines - 1:
        extracted_data[headers[1]].append('-')
    if len(extracted_data[headers[1]]) != max_lines:
        extracted_data[headers[1]].append('TOTAL')

    for i in range(2, len(headers)):
        while len(extracted_data[headers[i]]) != max_lines:
            extracted_data[headers[i]].insert(len(extracted_data[headers[i]]) - 1, 0)


def save_to_excel(data: dict) -> None:
    data_frame = pd.DataFrame(data)
    data_frame.to_excel('COVID_STATS.xls', index=0)


def create_table_head(data: dict) -> str:
    headers = str()

    for header in data.keys():
        headers += f'<th>{header}</th>'

    return f"""
    <thead>
        <tr>
            {headers}
        </tr>
    </thead>
    """


def create_table_body_row(data: dict, rownum: int, is_last_line: bool) -> str:
    cols = ''

    if is_last_line:
        keys = list(data)
        cols += f'<td colspan="2" style="text-align : center;">{data[keys[1]][rownum]}</td>'
        for key in keys[2:]:
            cols += f'<td>{data[key][rownum]}</td>'
    else:
        for key in data:
            cols += f'<td>{data[key][rownum]}</td>'

    return f'<tr>{cols}</tr>'


def create_table_body_rows(data: dict) -> str:
    rows = ""
    length = len(data[list(data)[0]])

    for index in range(length):
        rows += create_table_body_row(data, index, index == length - 1)

    return rows


def create_table_body(data: dict) -> str:
    return f"""
    <tbody>
        {create_table_body_rows(data)}
    </tbody>
    """


def create_html_table(data: dict) -> str:
    return f"""
    <html>
        <head>
            <title>
                COVID STATS APRIL 3-24
            </title>
        </head>
        <body>
            <table>
                {create_table_head(data)}
                {create_table_body(data)}
            </table>
        </body>
    </html>"""


def save_to_html(data: dict) -> None:
    file = open('COVID_STATS.html', 'w', encoding='utf-8')
    file.writelines(create_html_table(data))
    file.close()


include_blank_pages = True
start_date = 3
end_date = 25

extracted_data = fetch_data(date=start_date, extract_header=True, include_empty_data=include_blank_pages)
print(extracted_data)

for i in range(start_date + 1, end_date):
    if extracted_data is None:
        extracted_data = fetch_data(date=i, extract_header=True, include_empty_data=include_blank_pages)
    elif (temp := fetch_data(date=i, extract_header=False, include_empty_data=include_blank_pages)) is not None:
        extracted_data.update(temp)
        print(temp)

if len(extracted_data) == 0:
    exit()

format_data(extracted_data)
save_to_html(extracted_data)
save_to_excel(extracted_data)
