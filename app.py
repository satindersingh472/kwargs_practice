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
    columns = ['food','drinks']
    eachTable['order_items'] = []
    row = [table.get('food'), table.get('drinks')]
    eachTable['order_items'].append(dict(zip(columns,row)))
    # eachTable['order_items'][1]['drinks'] = table.get('drinks')

    tables.append(eachTable)
    return tables


print(assign_table_food(name='sam',vip_status=True,food="samosa",drinks='beer'))
