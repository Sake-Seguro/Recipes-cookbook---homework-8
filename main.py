from pprint import pprint


def create_cookbook():
    cookbook = {}
    with open('our_recipes.txt', encoding='utf-8') as recipe_book:
        for line in recipe_book:
            key = line.strip()
            q_ingredients = recipe_book.readline().strip()
            ingredient_list = []
            for i in range(int(q_ingredients)):
                value = recipe_book.readline().strip()
                split_value = value.split(' | ')
                ingredient_dict = {'ingredient_name': split_value[0],
                                   'quantity': int(split_value[1]), 'measure': split_value[2]}
                ingredient_list.append(ingredient_dict)
            recipe_book.readline()
            cookbook[key] = ingredient_list
    # pprint(cookbook)
    # pprint.pprint(cookbook)
    return cookbook



def get_shop_list_by_dishes(dish_name, person_count, recipes_dict):
    our_shop_list = {}
    cookbook = recipes_dict
    for dish in dish_name:
        for ingredient in cookbook[dish]:
            new_shop_list_ingredient = dict(ingredient)
            new_shop_list_ingredient['quantity'] *= person_count
            if new_shop_list_ingredient['ingredient_name'] not in our_shop_list:
                our_shop_list[new_shop_list_ingredient['ingredient_name']] = new_shop_list_ingredient
            else:
                our_shop_list[new_shop_list_ingredient['ingredient_name']]['quantity'] += new_shop_list_ingredient['quantity']
    print('\n',cookbook)
    return our_shop_list


def print_shop_list(our_shop_list):
    for item in our_shop_list.values():
        print(f"\nOur shopping list includes the follong ingredient  to buy: {item['ingredient_name']} - {item['quantity']} - {item['measure']}")


def person_counting():
    return int(input('\n\nEnter the number of persons you would like to prepare your favorite dish for: '))


def input_dish_name():
    dish_name = input('\n\nEnter the name of a dish from our recipes separated with comma (e.g. Omelette, Fajitas): ').split(', ')
    return [dish.capitalize() for dish in dish_name]




if __name__ == '__main__':
    
    print_shop_list(get_shop_list_by_dishes(input_dish_name(), person_counting(), create_cookbook()))
    





