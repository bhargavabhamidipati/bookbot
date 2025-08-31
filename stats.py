def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def get_num_characters(file_contents):
    ch_num = {}
    for ch in file_contents:
        ch = ch.lower()
        if ch in ch_num:
            ch_num[ch] += 1
        else:
            ch_num[ch] = 1
    return ch_num

def sort_on(ch_num):
    return ch_num['num']

def sort_dict(ch_num):
    ch_num_list = []
    for ch in ch_num:
        if ch.isalpha():
            ch_num_list.append({'char': ch, 'num': ch_num[ch]})
    ch_num_list.sort(reverse=True, key=sort_on)
    return ch_num_list

def display_ch_num_list(ch_num_list):
    for ch_num in ch_num_list:
        print(f'{ch_num['char']}: {ch_num['num']}')
