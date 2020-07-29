# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
# должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#     Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#     Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#     Пример json-объекта:[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

with open ('f_5_7.txt') as my_f:
    count_profit = []
    count_profit_all = []
    my_dict1 = {}
    my_dict2 = {}
    my_list = []

    for firm in my_f:
        name_firm, property_form, revenue, costs = firm.split()
        revenue = int(revenue)
        costs = int(costs)

        profit = revenue - costs

        if profit > 0:
            count_profit.append(profit)
            average_profit = sum(count_profit)/len(count_profit)

        count_profit_all.append(profit)
        average_profit_all = sum(count_profit_all) / len(count_profit_all)

        my_dict1.update({name_firm: profit})
        my_dict2.update({"average_profit_all": average_profit_all})
    my_list.append(my_dict1)
    my_list.append(my_dict2)

    print(my_list)

import json
with open("my_file.json", "w") as write_f:
    json.dump(my_list, write_f)
