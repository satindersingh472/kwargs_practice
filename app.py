tables =[
    {
        'name': 'satinder',
        'vip_status': True,
        'order_items': [
            {
                'food': 'noodles'
            },
            {
                'drinks':'apple juice'
            }
        ]
    }
]

# this function will grab the values and 

def assign_table_food(**table):
    eachTable = {}
    eachTable['name'] = table.get('name')
    eachTable['vip_status'] = table.get('vip_status')
    # eachTable['order_items'][0]['food'] = table.get('food')
    # eachTable['order_items'][1]['drinks'] = table.get('drinks')

    tables.append(eachTable)
    return tables


print(assign_table_food(name='sam',vip_status=True,food="samosa",drinks='beer'))
