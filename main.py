# Import everything needed to run the code.
# These will import the function count_words and count_letters from stats.py file
from stats import count_words, count_letters, new_dict
# This will provide access to command line arguments
import sys

def get_book_text(file_path):
    """
    Reads the contents of a text file and returns it as a string.

    Args:
    file_path (str): The path to the text file.

    Returns:
    str: The entire content of the file as a string, or none if an error occurs.
    """
    #try:
    #    with open(file_path) as f:
    #        content = f.read()
    #        return content
    #except FileNotFoundError:
    #    print(f"Error: The file '{file_path}' was not found")
    #    return None
    #except IOError as e:
    #    print(f"Error: Could not read file '{file_path}'. #Reason: {e}")
    #    return None
    #if len(sys.argv) < 2:
    #    print("Usage: python3 main.py <path to book>")
    #    sys.exit(1) # Exit with an error code
    try:
        with open(file_path, "r") as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path} was not found.")
    except Exception as e:
        print(f"An error occured: {e}") 



def main():
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    if content:
        num_words = count_words(content)
    new_letters = count_letters(content)
    report = new_dict(new_letters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # This will go through both sets of key value pairs and determine if the
    # first value is a string and if it is, will determine if it is an alphabetic character
    # then it will look to see if there are more than one key value pairs and if there is, 
    # it will print out the first and second value with a : between them.
    for value in report:
        first_key, first_value = next(iter(value.items()))
        if isinstance(first_value, str) and first_value.isalpha():
            items = list(value.items())
            if len(items)>= 2:
                second_key, second_value = items[1]
                print(f"{first_value}: {second_value}")
        


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit with an error code
    main()