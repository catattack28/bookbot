def count_words(file_path):
    list_of_words=get_book_text(file_path).split()
    return len(list_of_words)

def get_book_text(file_path):
    with open(file_path) as f:
        # f is a file object
        file_contents = f.read()
        return file_contents


def count_characters(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        lower=file_contents.lower()
        char_dict={}
        for char in lower:
            current=char_dict.get(char, 0)
            char_dict[char]=current
            char_dict[char] += 1
        return char_dict

def sort_on(item):
    return item['num']  

def create_dict_of_chars(items):
    list_of_char_dicts = []
    for key, value in items.items():
        list_of_char_dicts.append({'char': key, 'num': value})
    list_of_char_dicts.sort(reverse=True, key=sort_on)
    return list_of_char_dicts
