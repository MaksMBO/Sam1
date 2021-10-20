import re


class Text:
    def __init__(self, name):
        self.file = name

    def chartes(self):
        file = open(self.file)
        num = 0
        for line in file:
            num += len(re.split(r'.', line)) - 1
        file.close()
        return num

    def number_words(self):
        file = open(self.file)
        num = 0
        for i in file:
            num += len(i.split())
        file.close()
        return num

    def number_of_offers(self):
        file = open(self.file)
        num = 0
        ellipsis = 0
        for i in file:
            num += i.count('.')
            ellipsis += i.count('...')
            num += i.count('!')
            num += i.count('?')
        num -= 2 * ellipsis
        file.close()
        return num


text = Text('My_text.txt')
print(f"Characters: {text.chartes()}")
print(f"Number of words: {text.number_words()}")
print(f"Number of offers: {text.number_of_offers()}")
