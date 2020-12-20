import gspread


def iter_sprdsheet_rows(table_name):
    gc = gspread.service_account(
        filename='C:\desktop\programming\projects\ihub\scrapper\ihub-216c077d43d5.json')

    wks = gc.open(table_name).sheet1

    for line in range(2, 10):
        yield wks.row_values(line)


if __name__ == '__main__':
    print(list(iter_sprdsheet_rows('iHUB заходи')))
