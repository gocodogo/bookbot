def get_num_words(text):
    word_list = text.split()
    word_count = 0

    for word in word_list:
        word_count += 1
     
    return word_count

def get_num_characters(text):
    character_count = {}
    
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    
    return character_count


def sort_dict(dict):
    sorted_list = []

    for key, val in dict.items():
        new_item = {'name': key, 'value': val}
        sorted_list.append(new_item)
     
    # return sorted_list.sort(reverse=False, key=sort_on)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict['value']