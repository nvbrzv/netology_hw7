# To make the review easier, I decided to put all tasks of homework in single '.py' file.
# I understand that in real work it should be separate projects or modules.
import os


class Dish:
    def __init__(self, name):
        self.name = name
        self.ingredients = {}


class Ingredient:
    def __init__(self, ingredient_name='', quantity=0, measure=''):
        self.ingredient_name = ingredient_name
        self.quantity = int(quantity)
        self.measure = measure

    def dict_out(self):
        return {self.ingredient_name: {'measure': self.measure, 'quantity': self.quantity}}

    def newobj_with_addition(self, other, multiplier):
        if (isinstance(other, Ingredient) and
                self.ingredient_name == other.ingredient_name and
                self.measure == other.measure):
            return Ingredient(self.ingredient_name, (self.quantity + other.quantity) * int(multiplier), self.measure)
        else:
            return None


# Function to unify path making in this module.
def make_path(target_task_dir, target_file):
    root_path = os.getcwd()
    payload_dir = 'payload'
    result_path = os.path.join(root_path, payload_dir, target_task_dir, target_file)
    if os.path.exists(result_path):
        return result_path
    else:
        return None


def make_cook_book_from_file():
    # Represents Task 1.
    cook_book = {}
    recipes_path = make_path('task1', 'recipes.txt')
    if recipes_path is None:
        return None

    with open(recipes_path) as file:
        recipes_raw = list(map(str.strip, file.readlines()))
    dish_name_temp = ''
    for e in recipes_raw:
        if e.isnumeric() or e == '':
            continue
        elif '|' in e:
            temp_ingr = Ingredient()
            temp_ingr.ingredient_name, temp_ingr.quantity, temp_ingr.measure = e.split(' | ')
            cook_book[dish_name_temp].ingredients[temp_ingr.ingredient_name] = temp_ingr
        elif isinstance(e, str):
            cook_book[e] = Dish(e)
            dish_name_temp = e
        else:
            continue
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    # Represents Task 2.
    cook_book = make_cook_book_from_file()
    if cook_book is None:
        return None

    shopping_dict = {}
    for dish in dishes:
        if dish not in cook_book.keys():
            continue
        for ingredient in cook_book[dish].ingredients.values():
            print(ingredient.ingredient_name)
            print(shopping_dict.keys())
            if ingredient.ingredient_name in shopping_dict.keys():
                shopping_dict[ingredient.ingredient_name] += ingredient.newobj_with_addition(ingredient, person_count)
            else:
                shopping_dict.update(ingredient.dict_out())


        # for ingredient in cook_book[dish]:
        #     ing_name = ingredient['ingredient_name']
        #     ing_meas = ingredient['measure']
        #     ing_qt = int(ingredient['quantity'])
        #     shopping_dict.setdefault(ing_name, {'measure': ing_meas, 'quantity': 0})
        #     shopping_dict[ing_name]['quantity'] += ing_qt * person_count
    if shopping_dict:
        return shopping_dict
    else:
        return None


def main():
    print('Task 1. Making cook book:')
    print(make_cook_book_from_file())
    print('Task 2. Making shop list:')
    out = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Блюдо которого нет в списке'], 2)
    print(out)



main()
