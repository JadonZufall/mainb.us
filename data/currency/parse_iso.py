# sourced from https://github.com/fawazahmed0/exchange-api/blob/main/other/currencies.json
import json
import csv

base_path = "\\".join(__file__.split("\\")[:-1])
base_path += "\\"
print(base_path)

with open(base_path + 'iso.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

with open(base_path + 'iso.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Code', 'Currency'])
    for code, currency in data.items():
        writer.writerow([code, currency])
