import custom_excel_parser
import json_parser

if __name__ == '__main__':
    excel = custom_excel_parser.read_excel("data/data.xlsx")
    dict_list = custom_excel_parser.to_dict_list(excel)
    json_data = json_parser.of(dict_list)
    json_parser.save("data/data.json", json_data)

