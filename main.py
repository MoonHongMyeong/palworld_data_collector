import custom_excel_parser


if __name__ == '__main__':
    excel = custom_excel_parser.read_excel("data/data.xlsx")
    dict_list = custom_excel_parser.to_dict_list(excel)
    print(dict_list)
