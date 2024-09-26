def main():
    file_path = "books/frankenstein.txt"
    book_text = read_book(file_path)
    word_count = count_words(book_text)
    char_dict = count_characters(book_text)
    sorted_list = dict_to_sorted_list(char_dict)
    print_report(sorted_list, file_path, word_count)


def read_book(path):
    with open(path, 'r') as book:
        return book.read()

def count_words(string):
    split_string = string.split()
    return len(split_string)

def count_characters(string):
    count_dictionary = {}
    for letter in string.lower():
        if letter in count_dictionary:
            count_dictionary[letter] = count_dictionary[letter] + 1
        else:
            count_dictionary[letter] = 1
    return count_dictionary

def dict_to_sorted_list(dic):
    sorted_list = []
    for key in dic:
        if key.isalpha():
            sorted_list.append({"letter": key, "num": dic[key]}) 
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list 


def sort_on(dic):
    return dic["num"]

def print_report(char_list, path, word_count):
    print(f"--- Begin report of ${path} ---")
    print(f"{word_count} words found in the document")
    print()
    for item in char_list:
        print(f"The '{item['letter']}' character was found {item['num']} times")
    print("--- End report ---")

main()
