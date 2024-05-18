from main import logger
# Задача 3
# Применить написанный логгер к приложению из любого предыдущего д/з.

# Функция из ДЗ по чтению и записи в файл

cook_book = {'Омлет': [{'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'}, {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'}, {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}], 'Утка по-пекински': [{'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'}, {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'}, {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'}, {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}], 'Запеченный картофель': [{'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'}, {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'}, {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}], 'Фахитос': [{'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'}, {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'}, {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'}, {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'}, {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}]}


@logger
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            i = {ing['ingredient_name']: {'measure': ing['measure'], 'quantity': ing['quantity'] * person_count}}
            for k, v in shop_list.items():
                for key, value in i.items():
                    if k == key:
                        value['quantity'] += v['quantity']
            shop_list.update(i)
    return shop_list


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

