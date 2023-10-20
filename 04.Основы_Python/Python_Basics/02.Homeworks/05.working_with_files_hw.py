import json

purchases_raw = []
purchases = {}

with open('data/purchase_log.txt', 'r', encoding='utf-8') as f:
    purchases_raw = f.readlines()
    for line in purchases_raw:
            purchases[json.loads(line)['user_id']] = json.loads(line)['category']

    print(purchases)
#
# with open('data/purchases.txt', 'w') as fw:
#     fw.write(json.dumps(purchases))

# print(purchases)


# with open('data/funnel.csv', 'w') as write_funnel:
#     with open('data/visit_log.csv', 'r') as visits_log_list:
#         for vl in visits_log_list:
#             for key in purchases:
#                 if key in vl:
#                     write_funnel.write(vl.strip() + ',' + purchases[key] + '\n')
