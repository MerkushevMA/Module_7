import re

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        self.all_word = {}
        lock_symb = [',','.','=','!','?',';',':','-']

        for k in range(len(self.file_names)):
            with open(self.file_names[k], encoding='utf-8') as file:
                one_line = ''
                for line in file:
                    line = line.lower()
                    one_line += line.translate({ord(i): None for i in lock_symb})

            self.all_word[self.file_names[k]] = one_line.split()
        return self.all_word

    def find(self, word):
        find_word = {}
        for k in self.file_names:
            num_find_word = 1
            if word not in self.all_word.get(k):
                continue
            else:
                for i in self.all_word.get(k):
                    if word.lower() == i:
                        break
                    else:
                        num_find_word += 1
            find_word[k] = num_find_word
        if find_word == {}:
            find_word = 'Такого слова не найдено в указанных файлах'
        return find_word


    def count(self, word):
        count_word = {}
        for k in self.file_names:
            sum_find_word = 0
            for i in self.all_word.get(k):
                if word.lower() == i:
                    sum_find_word += 1
            count_word[k] = sum_find_word
        return count_word


p1 = WordsFinder('Test.txt', 'products.txt', 'test_file.txt', 'Walt Whitman - O Captain! My Captain!.txt')

print(p1.get_all_words())
print(p1.find('captaiт'))
print(p1.count('captain'))

