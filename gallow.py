import random
WORDS = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
def random_word(WORDS):
    return random.choice(WORDS)


class GallowGame():

    def __init__(self, name):
        if name:
            self.name = name
        else:
            self.name = input('Как к тебе можно обращаться? ')
        self.hidden_word = random_word(WORDS)
        self.MAX_WRONG_ATTEMPTS = 4
        self.current_wrong_attempts = 0
        self.user_letters = []
        self.guessed = []

    def valid_user_input(self, user_letter):
        if len(user_letter) > 1 or not user_letter.isalpha():
            print('Неправильный ввод. Введите одну букву')
            self.current_wrong_attempts += 1
            print('{} из {} попыток использованы. Будьте внимательней'.format(self.current_wrong_attempts, self.MAX_WRONG_ATTEMPTS))
        elif user_letter in self.user_letters:
            print('Буква уже была использована')
            self.current_wrong_attempts += 1
            print('{} из {} попыток использованы. Хорошенько подумайте'.format(self.current_wrong_attempts, self.MAX_WRONG_ATTEMPTS))
        else:
            return True

    def show_result(self, user_letter):
        self.user_letters.append(user_letter)
        word = []
        for letter in self.hidden_word:
            if letter in self.user_letters:
                word.append(letter)
            else:
                word.append('_')

        show_result = ''
        for l in word:
            show_result += l

        self.guessed = show_result
        print('Текущий статус -',self.guessed)
        return self.guessed

    def check_letter(self,user_letter):
        if user_letter.lower() in self.hidden_word:
            print('Вы угадали букву')
            self.show_result(user_letter)
            return True
        else:
            print('Увы, вы ошиблись')
            self.current_wrong_attempts += 1
            print('Допущена {} ошибка из {} возможных'.format(self.current_wrong_attempts, self.MAX_WRONG_ATTEMPTS))
            self.show_result(user_letter)
            return False

    def check_attemps(self):
        if self.current_wrong_attempts == self.MAX_WRONG_ATTEMPTS:
            print('=======================================')
            print("GameOver. В следующий раз тебе повезет, {}!".format(self.name).upper())
            print('Загаданное слово -',self.hidden_word)
            print('=======================================')
            return True
        elif self.hidden_word == self.guessed:
            print('=======================================')
            print('Поздравляю, {}, это победа! А ты силен!'.format(self.name).upper())
            print('Загаданное слово -', self.hidden_word)
            print('=======================================')
            return True
        else:
            print('Продолжаем угадывать')
            print('*********')
            return False






def main():
    game = GallowGame()
    print("Привет, {}. Давай поиграем!".format(game.name))
    print("У тебя есть 4 попытки угадать загаданное слово. Поееехаллии!")
    print("Загадано слово из",len(game.hidden_word), "букв.")
    while True:
        user_letter = input("Введите букву: ")
        valid = game.valid_user_input(user_letter)
        if not valid:
            result = game.check_attemps()
            if result:
                break
            else:
                continue
        game.check_letter(user_letter)
        result = game.check_attemps()
        if result:
            break


if __name__ == '__main__':
    main()