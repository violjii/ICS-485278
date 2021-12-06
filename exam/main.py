import re
from tabulate import tabulate
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np


def to_float(string: str):
    return float(string.replace(' ', '').replace(',', '.'))


def parse_data(file, regex):
    return_data = []
    with open(file, 'r') as file:
        for line in file.readlines():
            return_data.append(list(re.findall(regex, line)[0]))
    return return_data


def get_table(data, headers):
    return tabulate(data, headers=headers, tablefmt='orgtbl')


def merge_data(movement, directory):
    for i, element in enumerate(movement):
        movement[i].append(list(filter(lambda x: x[0] == element[1], directory))[0][1])
    return sorted(movement, key=lambda x: x[0])


def save_to_txt(file, data, headers):
    with open(file + ".txt", 'w') as file:
        file.write(get_table(data, headers))


def save_to_exel(file, data, headers):
    def __data_to_dict():
        return_dict = {i: [] for i in headers}
        for element in data:
            for key, value in zip(headers, element):
                return_dict[key].append(value)
        return return_dict

    df = pd.DataFrame(__data_to_dict())
    writer = pd.ExcelWriter(file + '.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()


def save_json(file, data, headers):
    return_data = []
    for element in data:
        return_data.append({key: value for key, value in zip(headers, element)})
    with open(file + '.json', 'w', encoding='utf8') as outfile:
        json.dump(return_data, outfile, indent=4, ensure_ascii=False)


def show_plot(data):
    labels = []
    zal = []
    nad = []
    vub = []

    for element in data:
        labels.append(element[0] + f" ({element[1]})")
        zal.append(to_float(element[2]))
        nad.append(to_float(element[3]))
        vub.append(to_float(element[4]))
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()

    zal1 = ax.bar(x - width, zal, width, label='Залишок на 1.01.2018')
    nad1 = ax.bar(x, nad, width, label='Надійшло у 2018')
    vub1 = ax.bar(x + width, vub, width, label='Вибуток у 2018')

    ax.set_xticks(x, labels, rotation=90)
    ax.legend()

    ax.bar_label(zal1, padding=3)
    ax.bar_label(nad1, padding=3)
    ax.bar_label(vub1, padding=3)

    fig.tight_layout()

    plt.show()


if __name__ == '__main__':
    movement_of_fixed_assets_headers = ['Підприємство', 'Код виду основних засобів', 'Залишок на 1.01.2018',
                                        'Надійшло у 2018', 'Вибуток у 2018']
    movement_of_fixed_assets = parse_data('input/movement_of_fixed_assets.txt', r'(.*)	(.*)	(.*)	(.*)	(.*)')

    directory_of_types_of_fixed_assets_headers = ['Код виду основних засобів', 'Вид основних засобів']
    directory_of_types_of_fixed_assets = parse_data('input/directory_of_types_of_fixed_assets.txt', r'(.*)	(.*)')

    print(get_table(movement_of_fixed_assets, movement_of_fixed_assets_headers), end="\n\n")
    print(get_table(directory_of_types_of_fixed_assets, directory_of_types_of_fixed_assets_headers), end="\n\n")

    merge_headers = [*movement_of_fixed_assets_headers, directory_of_types_of_fixed_assets_headers[1]]
    merged_data = merge_data(movement_of_fixed_assets, directory_of_types_of_fixed_assets)

    print(get_table(merged_data, merge_headers))

    save_to_txt('merge', merged_data, merge_headers)

    save_to_exel('merge', merged_data, merge_headers)

    save_json('merge', merged_data, ['PIDPR', 'KVOZ', 'ZAL', 'NAD', 'VUB', 'NAME'])

    show_plot(merged_data)
