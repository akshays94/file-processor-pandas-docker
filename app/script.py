from read_file_by_sheet_name import read_file_by_sheet_name


def run():
    read_some_file()


def read_some_file():
    lpt_1_file_path = './files/LTP_V3.xls'
    count_diff_data = read_file_by_sheet_name(
        lpt_1_file_path, sheet_name='Count Diff')

    for x in count_diff_data:
        print('row:', x)


def main():
    print('=' * 50)
    print('Script started')
    print('=' * 50)

    run()

    print('=' * 50)
    print('Script completed')
    print('=' * 50)


if __name__ == '__main__':
    main()
