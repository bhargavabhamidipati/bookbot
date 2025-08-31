from stats import get_num_words, get_num_characters, sort_dict, display_ch_num_list
import sys

def get_book_test(path_to_file):
    print(f'Analyzing book found at {path_to_file}...')
    file_contents ="" 
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    print(f'============ BOOKBOT ============')
    file_contents = get_book_test(sys.argv[1])
    print(f'----------- Word Count ----------')
    num_words = get_num_words(file_contents)
    print(f'Found {num_words} total words')
    print(f'--------- Character Count -------')
    ch_num = get_num_characters(file_contents)
    ch_num_list = sort_dict(ch_num)
    display_ch_num_list(ch_num_list)
    print(f'============= END ===============')


main()