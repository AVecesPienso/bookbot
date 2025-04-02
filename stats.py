def count_words(text):
    words = text.split()
    total_words = len(words)
    return total_words

def count_chars(text):
    char_dict = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_dict:
            char_dict[lowercase_char] += 1
        else:
            char_dict[lowercase_char] = 1
    return char_dict

def sort_chars(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    def sort_on(char_dict):
        return char_dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list