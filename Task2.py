
import json


def write_order_to_json(item, quantity, price, buyer, date):

    with open('orders.json', encoding="utf-8") as fl:
        data = json.loads(fl.read())

        data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

    with open('orders.json', "w", encoding="utf-8") as fl:
        json.dump(data, fl, indent=4, separators=(',', ': '), ensure_ascii=False)

    print(f'Данные добавлены в orders.json')



if __name__ == '__main__':
    write_order_to_json('monitor', '5', '9000', 'Sokolov', '10.11.2023')
    write_order_to_json('monitor', '8', '15000', 'Petrov', '10.04.2023')