def open_file():
    file_directory = str(input('File Directory: '))
    f = open(file_directory, 'r')
    global user_text
    user_text = f.read()


def count_words():
    res = len(user_text.split())
    print(f'Words:', res)


def count_commas():
    comma_count = 0
    for i in user_text:
        if i == ',':
            comma_count += 1
    print(f'Commas:', comma_count)


def count_spaces():
    space_count = 0
    for i in user_text:
        if i == ' ':
            space_count += 1
    print(f'Spaces:', space_count)


def search():
    user_search = str(input('Search: '))
    search_counter = user_text.lower().count(user_search.lower())
    print(user_search, ' Occurrences: ', search_counter)
