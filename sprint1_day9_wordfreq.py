import re
from collections import Counter

def load_text(path="sample.txt"):
    with open(path, encoding="utf-8") as f:
        return f.read()
    
def list_of_words(text):
    word_list=re.findall(r"\w+",text.lower())
    return Counter(word_list)

def main():
    text= load_text()
    word_count=list_of_words(text)
    
    print('Top 10 most common words found')
    for word, frequency in word_count.most_common(10):
        print(f"{word}: {frequency}")
    

if __name__ == '__main__':
    main()

        