def create_cook_book():
  with open('cook_book.txt') as f:
    cook_book = {}
    for line in f:
      line = line.strip()
      cook_book[line] = []
      quantity = int(f.readline().strip())
      for i in range(quantity):
        ingredient = f.readline().strip().split(' | ')
        new_dict = {}
        new_dict['ingridient_name'] = ingredient[0]
        new_dict['quantity'] = int(ingredient[1])
        new_dict['measure'] = ingredient[2] + '.'
        cook_book[line].append(new_dict)
  return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count, create_cook_book())
  print_shop_list(shop_list)

create_shop_list()
