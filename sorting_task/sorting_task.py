""""
algorithm
1. to create a list of number of dictionary in purchase_settings[]
2. to sort in order to PURCHASE_SETTINGS_ORDER[]
3. to put values by keys from dictionary WAGER_TYPES in another list (something like result[])
"""

WAGER_TYPES = {
    'LOTTO_WAGER': 'Lucky Numbers',
    'WAGER': 'Sports',
    'LIVE_WAGER': 'Live Sports',
    'BETGAMES_WAGER': 'Betgames',
    'EVOLUTION_WAGER': 'Evolution Games',
    'EZUGI_WAGER': 'Ezugi Games',
    'PRAGMATIC_WAGER': 'Pragmatic Play Games'
}

PURCHASE_SETTINGS_ORDER = [
    'LOTTO_WAGER',
    'WAGER',
    'LIVE_WAGER',
    'BETGAMES_WAGER',
    'EVOLUTION_WAGER',
    'EZUGI_WAGER',
    'PRAGMATIC_WAGER'
]

purchase_settings = [
    {
        'wagerType': 'PRAGMATIC_WAGER',
        'minTotalOdds': '',
        'wageredPercent': '15',
        'sameEventAllowed': True
    },
    {
        'wagerType': 'BETGAMES_WAGER',
        'minTotalOdds': '2',
        'wageredPercent': '100',
        'sameEventAllowed': True
    },
    {
        'wagerType': 'LIVE_WAGER',
        'minTotalOdds': '3',
        'wageredPercent': '100',
        'sameEventAllowed': False
    },
    {
        'wagerType': 'LOTTO_WAGER',
        'minTotalOdds': '4',
        'wageredPercent': '100',
        'sameEventAllowed': False
    },
    {
        'wagerType': 'WAGER',
        'minTotalOdds': '',
        'wageredPercent': '100',
        'sameEventAllowed': False
    },
]

list_of_wager_type_in_purchase_settings = [item["wagerType"] for item in purchase_settings]
print(list_of_wager_type_in_purchase_settings)

order_dict = dict((v, i) for i, v in enumerate(PURCHASE_SETTINGS_ORDER))
list_sorted = sorted(list_of_wager_type_in_purchase_settings, key=lambda v: order_dict.get(v, float('inf')))
print(list_sorted)

result_list = []
iterator = 0
while iterator < len(list_sorted):
    if list_sorted[iterator] in WAGER_TYPES:
        i = list_sorted[iterator]
        result_list.append(WAGER_TYPES[i])
        iterator += 1
    else:
        iterator += 1

print(result_list)