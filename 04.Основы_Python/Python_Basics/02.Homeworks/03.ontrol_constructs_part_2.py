def unique_geo_tags(ids_dict: dict):
    unique_geo = []
    for k in ids_dict:
        for val in ids_dict[k]:
            unique_geo.append(val)
    print(set(unique_geo))


def query_sorter(query: list):
    query_length_list = [len(val.split(' ')) for val in query]
    query_length_set = set(query_length_list)
    for qls in query_length_set:
        print(
            f'Поисковых запросов, содержащих {qls} слов(а): '
            f'{round((len([val for val in query_length_list if val % qls == 0]) / len(query_length_list) * 100), 2)}% '
        )


def calculate_roi(ad_results: dict):
    for ad_company in ad_results:
        ad_results[ad_company]['ROI'] = round(
            ((ad_results[ad_company]['revenue'] / ad_results[ad_company]['cost'] - 1) * 100), 2)
    print(ad_results)


def max_sales_calculator(sales_stats: dict):
    sales_stats_sorted_list = list(
        {key: sales_stats[key] for key in sorted(sales_stats, key=sales_stats.get, reverse=True)}.keys()
    )
    print(f'Максимальный объем продаж на рекламном канале: {sales_stats_sorted_list[0]}')


def inserted_dict_creator(primary_list: list):
    last_element = primary_list[-1]
    for el in reversed(primary_list[:-1]):
        last_element = {el: last_element}

    print(last_element)


def cook_book_product_list_combiner(cook_book_list: list):
    multiplier = int(input('Введите количество порций: '))
    items = []
    for cb in cook_book_list:
        for elem in cook_book_list[cb]:
            items.append({'ingridient_name': elem['ingridient_name'], 'quantity': 0, 'measure': elem['measure']})
            for item in items:
                if item['ingridient_name'] == elem['ingridient_name'] and item['measure'] == elem['measure'] and item[
                    'quantity'] != elem['quantity']:
                    item['quantity'] += elem['quantity'] * multiplier
                    break
                    continue

    for item in items:
        if list(item.values())[1] == 0:
            items.remove(item)

    for i, item in enumerate(items):
        print(i + 1, item['ingridient_name'].capitalize(), item['quantity'], item['measure'])


def teacher_s_variant_cook_book_product_list_combiner(cook_book_list: list):
    shop_list = {}
    person = int(input("Введите количество персон: "))
    for dish in cook_book_list.values():
        #     print(dish)
        for ingredient in dish:
            #         print(ingredient)
            if (ingredient['ingridient_name'], ingredient['measure']) not in shop_list:
                shop_list[(ingredient['ingridient_name'], ingredient['measure'])] = ingredient['quantity'] * person
            else:
                shop_list[(ingredient['ingridient_name'], ingredient['measure'])] += ingredient['quantity'] * person
    for name, q in shop_list.items():
        print(f'{name[0].title()}: {q} {name[1]}')

# cook_book = {
#     'салат': [
#         {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
#         {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
#         {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
#         {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
#         {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
#         {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
#         {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
#     ],
#     'пицца': [
#         {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
#         {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
#         {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
#         {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
#         {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
#         {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
#     ],
#     'лимонад': [
#         {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
#         {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
#         {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
#         {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
#     ]
# }
# 
# teacher_s_variant_cook_book_product_list_combiner(cook_book)
#
# cook_book_product_list_combiner(cook_book)

# my_list = ['2018-01-01', 'yandex', 'cpc', 100]
#
# inserted_dict_creator(my_list)

# stats = {'facebook': 55,
#          'yandex': 115,
#          'vk': 120,
#          'google': 99,
#          'email': 42,
#          'ok': 98}
#
# max_sales_calculator(stats)

# results = {
#     'vk': {'revenue': 103, 'cost': 98},
#     'yandex': {'revenue': 179, 'cost': 153},
#     'facebook': {'revenue': 103, 'cost': 110},
#     'adwords': {'revenue': 35, 'cost': 34},
#     'twitter': {'revenue': 11, 'cost': 24},
# }
#
# calculate_roi(results)

# ids = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119],
#        'user3': [213, 98, 98, 35]}
#
# unique_geo_tags(ids)

# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт'
# ]
# query_sorter(queries)
