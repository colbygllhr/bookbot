def main():
    print("Gathering data...")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    print("Generating report...")
    print(f"### Begin report of {book_path} ###")
    print(f"{num_words} found in the document")
    char_dict = count_characters(text)
    # Convert to list of dictionaries
    char_list = [{'char': k, 'num': v} for k, v in char_dict.items()]
    char_list.sort(reverse=True, key=sort_on)

    for i in char_list:
        print(f"The '{i['char']}' character was found {i['num']} times")
    
    print("### End Report ###")


def count_characters(text):
    char_dict = {}
    for letter in text:
        if letter.isalpha():

            letter = letter.lower()
            if letter in char_dict:
             char_dict[letter] += 1
            else:
             char_dict[letter] = 1
    

    return char_dict


def sort_on(item):
    return item["num"]


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()