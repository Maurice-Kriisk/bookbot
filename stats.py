def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    char_dict = {}
    words = text.split()
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
    return char_dict
def sort_key(items):
    return items["num"]

def get_sorted_characters(character_dict):
    sorted_characters = []
    for key in character_dict:
        sorted_characters.append({"char":f"{key}", "num":character_dict[key]})
    sorted_characters.sort(reverse=True, key=sort_key)
    return sorted_characters