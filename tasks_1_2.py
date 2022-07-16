import os


class Dish:
    def __init__(self, name):
        self.name = name
        self.ingredients = {}


class Ingredient:
    def __init__(self, ingredient_name='', quantity=0, measure=''):
        self.ingredient_name = ingredient_name
        self.quantity = quantity
        self.measure = measure

    def __add__(self, other):
        if (isinstance(other, Ingredient) and
                self.ingredient_name == other.ingredient_name and
                self.measure == other.measure):
            return Ingredient(self.ingredient_name, int(self.quantity) + int(other.quantity), self.measure)
        else:
            return None


class CookBook:
    def __init__(self, subdir, recipe_file):
        self.content = make_cook_book_from_file(make_path(subdir, recipe_file))

    def return_dict(self):
        if not self.content:
            return 'Empty'
        common_dict = {}
        for key in self.content.keys():
            common_dict[key] = []
            for value in self.content[key].ingredients.values():
                common_dict[key].append({'ingredient_name': value.ingredient_name,
                                         'quantity': value.quantity, 'measure': value.measure})
        return common_dict

    def __str__(self):
        return str(self.return_dict())


class ShopList:
    def __init__(self, cook_book, dishes, person_count):
        self.content = get_shop_list_by_dishes(cook_book, dishes, person_count)

    def return_dict(self):
        if not self.content:
            return 'Empty'
        common_dict = {}
        for key, value in self.content.items():
            common_dict[key] = {'measure': value.measure, 'quantity': value.quantity}
        return common_dict

    def __str__(self):
        return str(self.return_dict())


def make_path(target_task_dir, target_file):
    root_path = os.getcwd()
    payload_dir = 'payload'
    result_path = os.path.join(root_path, payload_dir, target_task_dir, target_file)
    if os.path.exists(result_path):
        return result_path
    else:
        return None


def make_cook_book_from_file(recipes_path):
    # Represents Task 1.
    if not recipes_path:
        return None
    cook_book = {}
    with open(recipes_path) as file:
        recipes_raw = list(map(str.strip, file.readlines()))
    dish_name_temp = ''
    for line in recipes_raw:
        if line.isnumeric() or line == '':
            continue
        elif '|' in line:
            temp_ingr = Ingredient()
            temp_ingr.ingredient_name, temp_ingr.quantity, temp_ingr.measure = line.split(' | ')
            temp_ingr.quantity = int(temp_ingr.quantity)
            cook_book[dish_name_temp].ingredients[temp_ingr.ingredient_name] = temp_ingr
        elif isinstance(line, str):
            cook_book[line] = Dish(line)
            dish_name_temp = line
        else:
            continue
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    # Represents Task 2.
    shopping_dict = {}
    for dish in dishes:
        if dish not in cook_book.content.keys():
            continue
        for ingredient in cook_book.content[dish].ingredients.values():
            if ingredient.ingredient_name in shopping_dict.keys():
                shopping_dict[ingredient.ingredient_name] += ingredient
            else:
                shopping_dict[ingredient.ingredient_name] = ingredient
    for ingredient in shopping_dict:
        shopping_dict[ingredient].quantity *= person_count
    if shopping_dict:
        return shopping_dict
    else:
        return None


def main():
    print('Task 1. Making cook book:')
    cook_book = CookBook('task1', 'recipes.txt')
    print({**cook_book.return_dict()})
    print(cook_book)
    print('Task 2. Making shop list:')
    shop_list = ShopList(cook_book, ['Омлет', 'Фахитос', 'Запеченный картофель', 'Блюдо которого нет в списке'], 2)
    print({**shop_list.return_dict()})
    print(shop_list)


main()
