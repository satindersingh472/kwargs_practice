tables ={
    1: {
    'name': 'satinder',
    'vip_status': True,
    'order_items': {
        'food': "pizza , pasta",
        'drinks': 'apple juice'
    }
},
2: {

}
}

def assign_table_food(table_number,**table):
    name = table.get('name')
    vip_status = table.get('vip_status')
    food = table.get('food')
    drinks = table.get('drinks')

    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['food'] = food
    # tables[table_number]['order_items']['drinks'] = drinks
    return tables


print(assign_table_food(2,name='sam',vip_status=True,food="samosa",drinks='beer'))
