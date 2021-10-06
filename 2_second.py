file = open('My_text.txt')
lines = file.readlines()
print(lines)


class Text:

    def characters(self, line):
        num = 0
        for i in line:
            for j in i:
                num += 1
        return num

    def number_words(self, line):
        num = 1
        for i in line:
            for j in i:
                if j == ' ':
                    num += 1
        return num

    def number_of_offers(self, line):
        num = 0
        for i in line:
            for j in i:
                if j == '.':
                    num += 1
        return num


text = Text()
print(f"Characters: {text.characters(lines)}")
print(f"Number of words: {text.number_words(lines)}")
print(f"Number of offers: {text.number_of_offers(lines)}")
file.close()
