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



# Function to unify path making in this module.
def make_path(target_task_dir, target_file=None, check_existence=True):
    root_path = os.getcwd()
    payload_dir = 'payload'

    # If target file not set, path ends on dir.
    if target_file:
        result_path = os.path.join(root_path, payload_dir, target_task_dir, target_file)
    else:
        result_path = os.path.join(root_path, payload_dir, target_task_dir)

    # If we do not need to check existence of path.
    if not check_existence:
        return result_path
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
        if isinstance(e, str) and e.isnumeric() or e == '':
            continue
        elif '|' in e:
            ing = Ingredient()
            ing.ingredient_name, ing.quantity, ing.measure = e.split(' | ')
            cook_book[dish_name_temp].ingredients[ing.ingredient_name] = ing
        elif isinstance(e, str):
            cook_book[e] = Dish(e)
            dish_name_temp = e
        else:
            continue
    return cook_book['Запеченный картофель'].ingredients['Картофель']


def get_shop_list_by_dishes(dishes, person_count):
    # Represents Task 2.
    cook_book = make_cook_book_from_file()
    if cook_book is None:
        return None

    shopping_dict = {}
    for dish in dishes:
        if dish not in cook_book.keys():
            continue
        for ingredient in cook_book[dish]:
            ing_name = ingredient['ingredient_name']
            ing_meas = ingredient['measure']
            ing_qt = int(ingredient['quantity'])
            shopping_dict.setdefault(ing_name, {'measure': ing_meas, 'quantity': 0})
            shopping_dict[ing_name]['quantity'] += ing_qt * person_count
    if shopping_dict:
        return shopping_dict
    else:
        return None

#
# def task_about_sorting():
#     # Represent Task 3.
#     dir_path = make_path('task3')
#     if dir_path is None:
#         return None
#     files = [
#         file for file in os.listdir(dir_path)
#         if file.endswith('.txt') and not file.startswith('result')
#     ]
#     files_dict = {}

    # for file in files:
    #     # Re-check if file still exists.
    #     file_path = make_path('task3', file)
    #     if file_path is None:
    #         return 'Something wrong with one of files!'
    #     with open(file_path) as text:
    #         # The task not describes how to handle with empty lines (if they there are) and extra spaces in text,
    #         # so I decided to keep them.
    #         files_dict[file] = text.read().split('\n')
    # result_path = make_path('task3', 'result.txt', False)
    # sorted_files_text = sorted(files_dict.items(), key=lambda x: len(x[1]))
    # result_text_list = []
    #
    # for file in sorted_files_text:
    #     result_text_list += file[0], str(len(file[1])), *file[1]
    # result_text = '\n'.join(result_text_list)
    #
    # with open(result_path, 'w') as result_file:
    #     result_file.write(result_text)
    # return f'Check this for result: {result_path}'
    #

def main():
    print('Task 1. Making cook book:')
    print(make_cook_book_from_file())
    print('Task 2. Making shop list:')
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Блюдо которого нет в списке'], 2))
    # print('Task 3. Making sort:')
    # print(task_about_sorting())


main()
