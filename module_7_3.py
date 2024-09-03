class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names
        # print(file_names)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='UTF-8') as file:
                v = file.read().lower()
                for k in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    v = v.replace(k, "")
            all_words[i] = v.split()
        return all_words

    def find(self, word):
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                index = words.index(word) + 1
                return {name, index}

    def count(self, word):
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                count_ = words.count(word)
                return {name, count_}


f1 = WordsFinder('test_file.txt')
print(f1.get_all_words())
print(f1.find("TEXT"))
print(f1.count("teXT"))

# , 'Walt Whitman - O Captain! My Captain!.txt',
#                  'Mother Goose - Monday’s Child.txt','Rudyard Kipling - If.txt'
