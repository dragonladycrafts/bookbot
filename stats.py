import operator
def count_words(text):
    """
    Counts the number of words in the provided text.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)



# This function will look through the document, turn all letters into
# lowercase then adds the letters to a dictionary and counts how many 
# times those letters, spaces, and symbols appear in the document.
def count_letters(letter):
    char_dict = {}
    words = letter.lower()
    for letter in words:
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1
    return char_dict



def new_dict(old_dict):
    sorted_list = []
    for key, value in old_dict.items():
        new_dict = {"char": str(key), "num": int(value)}
        sorted_list.append(new_dict)
        new_sorted_list = sorted(sorted_list, key=operator.itemgetter("num"), reverse=True)
    return new_sorted_list
