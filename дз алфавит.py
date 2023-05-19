class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))


import string

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)
        self.__letters_num = len(string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def exemple():
      return 'You are a good student!'


object = EngAlphabet()
object.print()
print(object.letters_num())
print(object.is_en_letter('F'))
print(object.is_en_letter('Щ'))
print(object.exemple())