import os


class Text:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content
        # The task not describes how to handle with
        # empty lines (if they there are) and extra spaces in text,
        # so I decided to keep them.
        self.num_of_lines = self.content.count('\n') + 1

    def __lt__(self, other):
        if isinstance(other, Text):
            return self.num_of_lines < other.num_of_lines
        else:
            return None


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


def task_about_sorting():
    # Represent Task 3.
    dir_path = make_path('task3')
    if dir_path is None:
        return None
    files_in_dir = [
        file for file in os.listdir(dir_path)
        if file.endswith('.txt') and not file.startswith('result')
    ]

    texts_list = []
    for file in files_in_dir:
        # Re-check if file still exists.
        file_path = make_path('task3', file)
        if file_path is None:
            return 'Something wrong with one of files!'
        with open(file_path) as source:
            texts_list.append(Text(file, source.read()))
    texts_list.sort()
    result_path = make_path('task3', 'result.txt', False)
    result_text_list = []
    for file in texts_list:
        result_text_list += str(file.filename), str(file.num_of_lines), str(file.content)
    result_text = '\n'.join(result_text_list)
    with open(result_path, 'w') as result_file:
        result_file.write(result_text)
    return f'Check this for result: {result_path}'


def main():
    print('Task 3. Making sort:')
    print(task_about_sorting())


main()
