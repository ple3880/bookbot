def get_text_count(text):
    split_text = text.split()
    return len(split_text)

def get_char_dict(text):
    dict_list = {}
    for c in text:
        lowered = c.lower()
        if not lowered.isalpha():
            continue
        if lowered in dict_list:
            dict_list[lowered] += 1
        else: dict_list[lowered] = 1
    return dict_list

def sort_on(x):
    return x["count"]

def get_sorted_dict(dictionary):
    sorted_list = []
    for ch in dictionary:
        sorted_list.append({"char": ch, "count": dictionary[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
