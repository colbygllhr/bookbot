

def main():
    book_path = "bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    print(count)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(txt):
   words = txt.split()
        

main()