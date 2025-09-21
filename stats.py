
def get_wordcount(path):
    with open(path) as f:
        words = f.read()
        wordlist = words.split()
        return len(wordlist)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(path):
    with open(path) as f:
        text = f.read().lower()
        words = list(text)
        char_count_dictionary = {}
        for char in words:
            if char not in char_count_dictionary:
               char_count_dictionary[char]=1
            else:
                char_count_dictionary[char]+=1
        return char_count_dictionary

def sort_char_count(char_counts):
     # list_items = list(get_char_count.items())
     # return list_items
    entries = []
    for ch, cnt in char_counts.items():
         entry = {"char":ch,"num":cnt}
         entries.append(entry)
    entries.sort(reverse=True, key=lambda item: item["num"])
    return entries
