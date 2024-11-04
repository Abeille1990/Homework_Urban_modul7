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
        find_d = {name: words.index(word) + 1 for name, words in self.get_all_words().items() if word in words}
        return find_d

    def count(self, word):
        word = word.lower()
        count_d = {name: words.count(word) for name, words in self.get_all_words().items()}
        return count_d


f1 = WordsFinder('test_file.txt', 'Walt Whitman - O Captain! My Captain!.txt')

print(f1.get_all_words())
print(f1.find("FoR"))
print(f1.count("For"))


