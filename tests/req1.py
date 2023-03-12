import requests
import json

pet1 = 'Кошка'
pet2 = 'Собака'

base_url = 'https://petstore.swagger.io/v2/pet/'
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

date = {
    'id': 0,
    'category':{'id': 0, 'name': 'string'},
    'name': pet1,
    'photoUrls': ['string'],
    'tags': [{'id': 0, 'name': 'string'}],
    'status': 'available'

}


# POST-запрос
res_1 = requests.post(f'https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(date))

print(res_1.status_code)
print('Код ответа - 200\nПитомец создан\n')

pet_id = dict(res_1.json())['id']

date['id'] = pet_id
date['name'] = pet2

# PUT-запрос
res_2 = requests.put(f'https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(date))

print(res_2.status_code)
print(f'Код ответа - 200\nИмя питомца "{pet1}" изменено на "{pet2}"')

print('\nЗапрос с сервера данных о питомце по id - ' + str(pet_id))

# GET-запрос
res_3 = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers=headers)

print(res_3.status_code)
print('Код ответа - 200 \nНа сервере есть данные о питомце')

print('\nУдаление данных о питомце по id - ' + str(pet_id))

# DELETE-запрос
res_4 = requests.delete(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers=headers)

print(res_4.status_code)
print('Код ответа - 200 \nС сервера удалены данные о питомце')










